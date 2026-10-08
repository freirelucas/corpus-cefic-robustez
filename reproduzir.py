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


CATEGORIAS_ARTIGO = ("resolucao", "registro_reuniao")


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


NOMES = {
    "territorio_nacional": "Território nacional", "interoperabilidade": "Interoperabilidade",
    "preferencia_normativa": "Preferência normativa",
    "multifornecedor_segundo_motor": "Multifornecedor / segundo motor",
    "soberania": "Soberania", "concorrencia": "Concorrência",
    "capacitacao_tecnologica": "Capacitação tecnológica",
    "propriedade_intelectual": "Propriedade intelectual",
    "aprisionamento_lockin": "Aprisionamento / lock-in", "codigo_fonte": "Código-fonte",
    "conteudo_local": "Conteúdo local", "desenvolvimento_nacional": "Desenvolvimento nacional",
    "empresa_industria_nacional": "Empresa/indústria nacional",
    "encomenda_tecnologica": "Encomenda tecnológica", "margem_preferencia": "Margem de preferência",
    "nova_industria_brasil": "Nova Indústria Brasil", "padrao_aberto": "Padrão aberto",
    "software_livre_codigo_aberto": "Software livre / código aberto",
    "substituicao_fornecedor": "Substituição de fornecedor",
    "transferencia_tecnologia": "Transferência de tecnologia",
    "nist_nfiq": "NIST / NFIQ", "tier_iii": "Tier III", "sitios_operacionais": "Sítios operacionais",
    "graficas": "Gráficas", "fala_brasil": "Fala.BR", "blockchain": "Blockchain",
    "bancos": "Bancos / sistema financeiro", "acuracia": "Acurácia", "fomento": "Fomento",
    "policiafederal_aditivo": "Polícia Federal / aditivo",
}
DIMENSOES_PRESENTES = ["territorio_nacional", "interoperabilidade", "preferencia_normativa",
                       "multifornecedor_segundo_motor", "soberania", "concorrencia"]
AUXILIARES = ["nist_nfiq", "tier_iii", "sitios_operacionais"]
MARCA_RES_INICIO = "<!-- resultados: gerado por reproduzir.py a partir de dados/ -->"
MARCA_RES_FIM = "<!-- fim dos resultados -->"


def tabelas_resultados() -> str:
    with (DADOS / "resultados_por_familia.csv").open(encoding="utf-8-sig") as f:
        res = {r["familia"]: r for r in csv.DictReader(f)}
    zeradas = sorted((f for f in res if res[f]["sem_ocorrencia_no_recorte_declarado"] == "True"),
                     key=lambda f: (res[f]["situacao_artigo"] != "presente"
                                    and res[f]["artigo_ampliado_ocorrencias"] == "0", NOMES[f]))
    outras = sorted((f for f in res if f not in DIMENSOES_PRESENTES + AUXILIARES + zeradas),
                    key=lambda f: (-int(res[f]["artigo_estrito_ocorrencias"]), NOMES[f]))
    cab = ["| família | ocorrências (artigo) | documentos (artigo) | ocorrências (completo) "
           "| documentos (completo) | situação no corpus do artigo |",
           "|---|---|---|---|---|---|"]

    def linha(f):
        r = res[f]
        return (f"| {NOMES[f]} | {r['artigo_estrito_ocorrencias']} | {r['artigo_estrito_documentos']} | "
                f"{r['corpus_estrito_ocorrencias']} | {r['corpus_estrito_documentos']} | "
                f"{r['situacao_artigo']} |")

    out = [MARCA_RES_INICIO, "",
           "Nível estrito de busca. Corpus do artigo: 33 resoluções e 40 registros de reunião (73 "
           "documentos). Corpus completo: 105 documentos.", "",
           "### Famílias das duas dimensões analíticas do artigo", ""] + cab
    out += [linha(f) for f in DIMENSOES_PRESENTES + zeradas]
    out += ["", "### Termos que sustentam afirmações do texto fora do quadro", ""] + cab
    out += [linha(f) for f in AUXILIARES]
    out += ["", "### Demais famílias do levantamento", "",
            "Famílias auxiliares do levantamento, fora das dimensões analíticas do artigo.", ""] + cab
    out += [linha(f) for f in outras]
    out += ["", MARCA_RES_FIM]
    return "\n".join(out)


def substitui_bloco(caminho, inicio: str, fim: str, bloco: str) -> None:
    texto = caminho.read_text(encoding="utf-8").replace("\r\n", "\n")
    if inicio not in texto:
        return
    ini, fi = texto.index(inicio), texto.index(fim) + len(fim)
    caminho.write_text(texto[:ini] + bloco + texto[fi:], encoding="utf-8", newline="\n")


MARCA_TERMOS_INICIO = "<!-- termos: gerado por reproduzir.py a partir de dados/ -->"
MARCA_TERMOS_FIM = "<!-- fim dos termos -->"


def tabelas_termos() -> str:
    with (DADOS / "termos_buscados_conferencia.csv").open(encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    out, atual = [MARCA_TERMOS_INICIO], None
    for r in linhas:
        if r["conceito"] != atual:
            atual = r["conceito"]
            out += ["", f"**{atual}**", "", "| termo | documentos (artigo) | documentos (completo) |",
                    "|---|---|---|"]
        art = r["documentos_artigo"] if r["documentos_artigo"] != "0" else "—"
        cor = r["documentos_corpus"] if r["documentos_corpus"] != "0" else "—"
        out.append(f"| {r['termo']} | {art} | {cor} |")
    out += ["", MARCA_TERMOS_FIM]
    return "\n".join(out)


def atualiza_readme() -> None:
    substitui_bloco(BASE / "README.md", MARCA_INICIO, MARCA_FIM, listas())
    for nome in ("README.md", "TERMOS_BUSCADOS.md"):
        substitui_bloco(BASE / nome, MARCA_RES_INICIO, MARCA_RES_FIM, tabelas_resultados())
    substitui_bloco(BASE / "TERMOS_BUSCADOS.md", MARCA_TERMOS_INICIO, MARCA_TERMOS_FIM,
                    tabelas_termos())


def main() -> None:
    DADOS.mkdir(exist_ok=True)
    docs = carrega()
    inv = inventario()
    est = varre(docs, "estrito")
    amp = varre(docs, "ampliado")

    # corpus do artigo: as resolucoes e os registros de reuniao da CEFIC
    artigo = {a for a, r in inv.items() if r["categoria"] in CATEGORIAS_ARTIGO}
    for linha in est + amp:
        linha["corpus_do_artigo"] = linha["arquivo"] in artigo
    campos = ["familia", "arquivo", "pagina", "termo", "trecho", "corpus_do_artigo"]
    escreve("kwic_estrito.csv", est, campos)
    escreve("kwic_ampliado.csv", amp, campos)

    def conta(linhas, fam, escopo):
        sel = [r for r in linhas if r["familia"] == fam and (escopo is None or r["arquivo"] in escopo)]
        return len(sel), len({r["arquivo"] for r in sel})

    def situacao(estrito, ampliado):
        if estrito:
            return "presente"
        if not ampliado:
            return "ausente nos dois níveis"
        return "ausente no nível estrito; termos vizinhos no ampliado"

    freq = []
    for f in LEXICO:
        r = {"familia": f}
        for nome, escopo in (("artigo", artigo), ("corpus", None)):
            r[f"{nome}_estrito_ocorrencias"], r[f"{nome}_estrito_documentos"] = conta(est, f, escopo)
            r[f"{nome}_ampliado_ocorrencias"], r[f"{nome}_ampliado_documentos"] = conta(amp, f, escopo)
        r["sem_ocorrencia_no_recorte_declarado"] = f in ZERADAS
        r["situacao_artigo"] = situacao(r["artigo_estrito_ocorrencias"], r["artigo_ampliado_ocorrencias"])
        r["situacao_corpus"] = situacao(r["corpus_estrito_ocorrencias"], r["corpus_ampliado_ocorrencias"])
        freq.append(r)
    escreve("resultados_por_familia.csv", freq, list(freq[0]))

    termos = []
    with (DADOS / "termos_buscados_conferencia.csv").open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            # forma literal, palavra inteira, sobre o texto normalizado
            rx = re.compile(r"(?<![a-z0-9])" + r"\s+".join(map(re.escape, dobra(r["termo"]).split()))
                            + r"(?![a-z0-9])")
            por_doc = {a: len(rx.findall(d.norm)) for a, d in docs.items()}
            por_doc = {a: n for a, n in por_doc.items() if n}
            no_artigo = [a for a in por_doc if a in artigo]
            termos.append({"conceito": r["conceito"], "termo": r["termo"],
                           "documentos_artigo": len(no_artigo), "documentos_corpus": len(por_doc),
                           "situacao_artigo": "presente" if no_artigo else "ausente",
                           "situacao_corpus": "presente" if por_doc else "ausente",
                           "aviso": r["aviso"]})
    escreve("termos_buscados_conferencia.csv", termos,
            ["conceito", "termo", "situacao_artigo", "documentos_artigo", "situacao_corpus",
             "documentos_corpus", "aviso"])

    sonda = []
    for termo, padrao in SONDA.items():
        rx = re.compile(padrao)
        por_doc = {a: len(rx.findall(d.norm)) for a, d in docs.items()}
        por_doc = {a: n for a, n in por_doc.items() if n}
        no_artigo = {a: n for a, n in por_doc.items() if a in artigo}
        sonda.append({"termo": termo, "padrao": padrao,
                      "ocorrencias_artigo": sum(no_artigo.values()), "documentos_artigo": len(no_artigo),
                      "ocorrencias_corpus": sum(por_doc.values()), "documentos_corpus": len(por_doc)})
    sonda.sort(key=lambda r: (-r["ocorrencias_artigo"], -r["ocorrencias_corpus"]))
    escreve("sonda_vocabulario_nativo.csv", sonda, list(sonda[0]))

    documenta()
    atualiza_readme()

    paginas = sum(len(re.findall(r"===== \[pag \d+\] =====", d.raw)) or 1 for d in docs.values())
    linhas_txt = sum(d.raw.count("\n") + 1 for d in docs.values())
    resumo = {"documentos": len(docs), "paginas": paginas, "linhas": linhas_txt,
              "familias": len(LEXICO), "kwic_estrito": len(est), "kwic_ampliado": len(amp),
              "familias_zeradas_no_recorte_original": len(ZERADAS),
              "familias_que_seguem_zeradas_no_nivel_ampliado":
                  sum(1 for r in freq if r["sem_ocorrencia_no_recorte_declarado"]
                      and not r["corpus_ampliado_ocorrencias"])}
    for k, v in resumo.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
