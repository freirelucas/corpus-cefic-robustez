"""Regenera os resultados do teste de robustez a partir de corpus_txt/.

    python reproduzir.py

Sem dependencias alem da biblioteca padrao (Python 3.10+).
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from robustez_varredura import LEXICO, ZERADAS, Doc  # noqa: E402

TEXTOS = BASE / "corpus_txt"
DADOS = BASE / "dados"

# Vocabulario empregado pelos proprios documentos e nao coberto pelo recorte declarado.
# Os padroes ancoram no inicio da palavra: "licitac" nao deve casar dentro de "solicitacao".
SONDA = {
    "dados pessoais": r"\bdados\s+pessoais",
    "credenciamento": r"\bcredenciament",
    "custo": r"\bcustos?\b",
    "contrato": r"\bcontratos?\b",
    "exterior": r"\bexterior\b",
    "auditoria": r"\bauditorias?\b",
    "infraestrutura": r"\binfraestrutura",
    "dispensa": r"\bdispensa",
    "orçamento": r"\borcament",
    "certificação": r"\bcertificac",
    "convênio": r"\bconvenios?\b",
    "homologação": r"\bhomologac",
    "contratação": r"\bcontratac",
    "estrangeiro": r"\bestrangeir",
    "autonomia": r"\bautonomia",
    "acordo de cooperação": r"\bacordos?\s+de\s+cooperacao",
    "investimento": r"\binvestiment",
    "nuvem": r"\bnuvem\b",
    "licitação": r"\blicitac",
    "licitatório": r"\blicitatori",
    "capacidade técnica": r"\bcapacidade\s+tecnica",
    "importação": r"\bimportac",
}


def dobra(texto: str) -> str:
    return Doc(texto).norm


def carrega() -> dict[str, Doc]:
    return {f.stem: Doc(f.read_text(encoding="utf-8", errors="replace"))
            for f in sorted(TEXTOS.glob("*.txt"), key=lambda f: f.name.lower())}


def inventario() -> dict[str, dict]:
    with (DADOS / "inventario_documentos.csv").open(encoding="utf-8-sig") as f:
        return {r["arquivo"]: r for r in csv.DictReader(f)}


def varre(docs: dict[str, Doc], nivel: str) -> list[dict]:
    linhas = []
    for fam, d in LEXICO.items():
        if nivel not in d:
            continue
        rx = re.compile("|".join(d[nivel]))
        for stem, doc in docs.items():
            for m in rx.finditer(doc.norm):
                linhas.append({"familia": fam, "arquivo": stem,
                               "pagina": doc.pagina(m.start()),
                               "termo": doc.termo(m.start(), m.end()),
                               "trecho": doc.kwic(m.start(), m.end())})
    return linhas


def escreve(nome: str, linhas: list[dict], campos: list[str]) -> None:
    with (DADOS / nome).open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)


def documenta() -> None:
    """Escreve DICIONARIO_DE_DADOS.md e dados/README.md a partir de datapackage.json."""
    dp = json.loads((BASE / "datapackage.json").read_text(encoding="utf-8"))
    tipos = {"string": "texto", "integer": "inteiro", "number": "número", "boolean": "booleano"}

    def linhas(path: str) -> int:
        with (BASE / path).open(encoding="utf-8-sig") as f:
            return sum(1 for _ in csv.reader(f)) - 1

    dic = ["# Dicionário de dados", "",
           "Significado de cada tabela publicada em `dados/` e de cada uma de suas colunas.",
           "Gerado por `reproduzir.py` a partir de `datapackage.json`.", ""]
    idx = ["# Dados", "",
           "Tabelas de resultado, inventário, proveniência e verificação do corpus.", "",
           "O significado de cada coluna consta de "
           "[DICIONARIO_DE_DADOS.md](../DICIONARIO_DE_DADOS.md).", "",
           "| arquivo | conteúdo | linhas |", "|---|---|---|"]
    for r in dp["resources"]:
        nome = r["path"].split("/")[-1]
        n = linhas(r["path"])
        dic += [f"## `{nome}`", "", r["description"], "", f"{n} linhas.", "",
                "| coluna | tipo | descrição |", "|---|---|---|"]
        dic += [f"| `{c['name']}` | {tipos.get(c['type'], c['type'])} | {c['description']} |"
                for c in r["schema"]["fields"]]
        dic.append("")
        idx.append(f"| [`{nome}`]({nome}) | {r['description']} | {n} |")
    idx += ["", "`numeros_verificados.json` guarda os números-âncora conferidos por "
            "`teste_reproducao.py`.", ""]
    (BASE / "DICIONARIO_DE_DADOS.md").write_text("\n".join(dic), encoding="utf-8", newline="\r\n")
    (DADOS / "README.md").write_text("\n".join(idx), encoding="utf-8", newline="\r\n")


def main() -> None:
    DADOS.mkdir(exist_ok=True)
    docs = carrega()
    inv = inventario()
    est = varre(docs, "estrito")
    amp = varre(docs, "ampliado")
    campos = ["familia", "arquivo", "pagina", "termo", "trecho"]
    escreve("kwic_estrito.csv", est, campos)
    escreve("kwic_ampliado.csv", amp, campos)


    def agrega(linhas):
        tot, dd = {}, {}
        for r in linhas:
            tot[r["familia"]] = tot.get(r["familia"], 0) + 1
            dd.setdefault(r["familia"], set()).add(r["arquivo"])
        return tot, dd

    def situacao(fam, estrito, ampliado):
        if estrito:
            return ("presente; família acrescentada ao léxico no teste de robustez"
                    if fam == "preferencia_normativa" else "presente")
        if not ampliado:
            return "ausência robusta a sinônimos e variantes"
        return "sintagma ausente; termos vizinhos presentes em ocorrências marginais"

    te, de = agrega(est)
    ta, da = agrega(amp)
    freq = [{"familia": f,
             "estrito_ocorrencias": te.get(f, 0), "estrito_documentos": len(de.get(f, ())),
             "estrito_documentos_cefic": sum(1 for a in de.get(f, ()) if inv[a]["orgao"] == "CEFIC"),
             "ampliado_ocorrencias": ta.get(f, 0), "ampliado_documentos": len(da.get(f, ())),
             "sem_ocorrencia_no_recorte_declarado": f in ZERADAS,
             "situacao": situacao(f, te.get(f, 0), ta.get(f, 0))} for f in LEXICO]
    escreve("resultados_por_familia.csv", freq, list(freq[0]))

    termos = []
    with (DADOS / "termos_buscados_conferencia.csv").open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            # forma literal, palavra inteira, sobre o texto normalizado
            rx = re.compile(r"(?<![a-z0-9])" + r"\s+".join(map(re.escape, dobra(r["termo"]).split()))
                            + r"(?![a-z0-9])")
            por_doc = {a: len(rx.findall(d.norm)) for a, d in docs.items()}
            por_doc = {a: n for a, n in por_doc.items() if n}
            termos.append({"conceito": r["conceito"], "termo": r["termo"],
                           "situacao": "presente" if por_doc else "ausente",
                           "ocorrencias": sum(por_doc.values()), "documentos": len(por_doc),
                           "aviso": r["aviso"]})
    escreve("termos_buscados_conferencia.csv", termos,
            ["conceito", "termo", "situacao", "ocorrencias", "documentos", "aviso"])

    sonda = []
    for termo, padrao in SONDA.items():
        rx = re.compile(padrao)
        por_doc = {a: len(rx.findall(d.norm)) for a, d in docs.items()}
        por_doc = {a: n for a, n in por_doc.items() if n}
        cefic = {a: n for a, n in por_doc.items() if inv[a]["orgao"] == "CEFIC"}
        sonda.append({"termo": termo, "padrao": padrao,
                      "ocorrencias": sum(por_doc.values()), "documentos": len(por_doc),
                      "ocorrencias_cefic": sum(cefic.values()), "documentos_cefic": len(cefic)})
    sonda.sort(key=lambda r: -r["ocorrencias"])
    escreve("sonda_vocabulario_nativo.csv", sonda,
            ["termo", "padrao", "ocorrencias", "documentos", "ocorrencias_cefic",
             "documentos_cefic"])

    documenta()

    paginas = sum(len(re.findall(r"===== \[pag \d+\] =====", d.raw)) or 1 for d in docs.values())
    linhas_txt = sum(d.raw.count("\n") + 1 for d in docs.values())
    resumo = {"documentos": len(docs), "paginas": paginas, "linhas": linhas_txt,
              "familias": len(LEXICO), "kwic_estrito": len(est), "kwic_ampliado": len(amp),
              "familias_zeradas_no_recorte_original": len(ZERADAS),
              "familias_que_seguem_zeradas_no_nivel_ampliado":
                  sum(1 for f in ZERADAS if ta.get(f, 0) == 0)}
    for k, v in resumo.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
