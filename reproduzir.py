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
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
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
    (BASE / "DICIONARIO_DE_DADOS.md").write_text("\n".join(dic), encoding="utf-8", newline="\n")
    (DADOS / "README.md").write_text("\n".join(idx), encoding="utf-8", newline="\n")


MARCA_INICIO = "<!-- listas: gerado por reproduzir.py a partir de dados/ -->"
MARCA_FIM = "<!-- fim das listas -->"


def listas() -> str:
    """Listas das resolucoes e das reunioes, com link para o texto de cada uma."""
    def le(nome: str) -> list[dict]:
        with (DADOS / nome).open(encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))

    def link(arq: str) -> str:
        return f"[`{arq}`](corpus_txt/{arq.replace(' ', '%20')}.txt)"

    res = le("inventario_resolucoes.csv")
    out = [MARCA_INICIO, "", "### As 33 resoluções", "",
           "| nº | data | ementa | publicação no DOU | texto |", "|---|---|---|---|---|"]
    for r in res:
        if r["tipo"] != "resolução":
            continue
        dou = (f"{r['publicacao_dou']}, ed. {r['edicao_dou']}, seç. {r['secao_dou']}, "
               f"p. {r['pagina_dou']}")
        out.append(f"| {r['numero']} | {r['data']} | {r['ementa']} | {dou} | {link(r['arquivo'])} |")
    out += ["", "Retificações publicadas:", ""]
    for r in res:
        if r["tipo"] == "retificação":
            out.append(f"- Resolução nº {r['numero']}: DOU de {r['publicacao_dou']}, "
                       f"ed. {r['edicao_dou']}, seç. {r['secao_dou']}, p. {r['pagina_dou']} — "
                       f"{link(r['arquivo'])}")
    reunioes = sorted(le("inventario_reunioes.csv"),
                      key=lambda r: (r["data"][6:], r["data"][3:5], r["data"][:2], r["ordem_declarada"]))
    out += ["", "### As 40 reuniões com registro", "",
            "Ordem e tipo tais como declarados no cabeçalho de cada registro.", "",
            "| | data | ordem e tipo declarados | modalidade | registro | observação |",
            "|---|---|---|---|---|---|"]
    for i, r in enumerate(reunioes, 1):
        decl = " ".join(x for x in (r["ordem_declarada"], r["tipo_declarado"]) if x) or "não declarados"
        out.append(f"| {i} | {r['data']} | {decl} | {r['modalidade']} | "
                   f"{link(r['arquivos_registro'])} | {r['observacao']} |")
    out += ["", MARCA_FIM]
    return "\n".join(out)


def atualiza_readme() -> None:
    caminho = BASE / "README.md"
    texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
    ini, fim = texto.index(MARCA_INICIO), texto.index(MARCA_FIM) + len(MARCA_FIM)
    caminho.write_text(texto[:ini] + listas() + texto[fim:], encoding="utf-8", newline="\n")


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
            return "presente"
        if not ampliado:
            return "ausente nos dois níveis"
        return "ausente no nível estrito; termos vizinhos no ampliado"

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
    atualiza_readme()

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
