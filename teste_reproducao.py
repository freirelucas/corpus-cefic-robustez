"""Verifica que a reproducao produz os numeros-ancora registrados.

    python teste_reproducao.py

Falha com codigo de saida 1 se qualquer valor divergir de dados/numeros_verificados.json.
Nao depende de bibliotecas externas.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from robustez_varredura import LEXICO, ZERADAS, Doc  # noqa: E402

DADOS = BASE / "dados"
TEXTOS = BASE / "corpus_txt"
falhas: list[str] = []


def confere(rotulo: str, obtido, esperado) -> None:
    if obtido != esperado:
        falhas.append(f"{rotulo}: obtido {obtido!r}, esperado {esperado!r}")
    else:
        print(f"  ok  {rotulo} = {obtido}")


def main() -> int:
    ref = json.loads((DADOS / "numeros_verificados.json").read_text(encoding="utf-8"))
    docs = {f.stem: Doc(f.read_text(encoding="utf-8", errors="replace"))
            for f in sorted(TEXTOS.glob("*.txt"), key=lambda f: f.name.lower())}

    print("Corpus")
    confere("documentos", len(docs), ref["documentos"])
    paginas = sum(len(re.findall(r"===== \[pag \d+\] =====", d.raw)) or 1 for d in docs.values())
    confere("paginas", paginas, ref["paginas"])
    confere("linhas", sum(d.raw.count("\n") + 1 for d in docs.values()), ref["linhas"])
    ligaduras = {n: sum(1 for ch in d.raw if "\ufb00" <= ch <= "\ufb06") for n, d in docs.items()}
    confere("ligaduras tipograficas", sum(ligaduras.values()), ref["ligaduras_tipograficas"])
    confere("documentos com ligadura", sum(1 for v in ligaduras.values() if v),
            ref["documentos_com_ligadura"])

    print("Composicao")
    with (DADOS / "inventario_documentos.csv").open(encoding="utf-8-sig") as f:
        inv = {r["arquivo"]: r for r in csv.DictReader(f)}
    if set(inv) != set(docs):
        falhas.append("inventario_documentos.csv nao corresponde a corpus_txt/: "
                      + ", ".join(sorted(set(inv) ^ set(docs))))
    if len({r["documento"] for r in inv.values()}) != len(inv):
        falhas.append("o mesmo documento consta em mais de um arquivo do corpus")
    cefic = [a for a in inv if inv[a]["orgao"] == "CEFIC"]
    confere("documentos da CEFIC", len(cefic), ref["documentos_cefic"])
    confere("documentos de outros orgaos ou de autoria nao determinada", len(inv) - len(cefic),
            ref["documentos_outros"])
    numeros = sorted(int(r["numero"]) for r in inv.values() if r["categoria"] == "resolucao")
    confere("resolucoes, numeros distintos", len(set(numeros)), ref["resolucoes_numeros_distintos"])
    if len(numeros) != len(set(numeros)):
        falhas.append("resolucao com mais de um documento no corpus")
    confere("serie de resolucoes", f"{numeros[0]}-{numeros[-1]}"
            if numeros == list(range(numeros[0], numeros[-1] + 1)) else "com lacuna",
            ref["serie_resolucoes"])
    with (DADOS / "inventario_reunioes.csv").open(encoding="utf-8-sig") as f:
        reunioes = list(csv.DictReader(f))
    confere("reunioes com registro", len(reunioes), ref["reunioes_com_registro"])
    registros = [r["arquivos_registro"] for r in reunioes]
    apresentacoes = [r["arquivo_apresentacao"] for r in reunioes if r["arquivo_apresentacao"]]
    confere("documentos de registro de reuniao", len(registros), ref["documentos_registro_reuniao"])
    confere("documentos de apresentacao de reuniao", len(apresentacoes),
            ref["documentos_apresentacao_reuniao"])
    por_categoria = {c: {a for a, r in inv.items() if r["categoria"] == c}
                     for c in ("registro_reuniao", "apresentacao_reuniao")}
    if set(registros) != por_categoria["registro_reuniao"]:
        falhas.append("inventario_reunioes.csv e inventario_documentos.csv divergem nos registros")
    if set(apresentacoes) != por_categoria["apresentacao_reuniao"]:
        falhas.append("inventario_reunioes.csv e inventario_documentos.csv divergem nas apresentacoes")
    datas = sorted(r["data"][6:] + r["data"][3:5] + r["data"][:2] for r in reunioes)
    confere("primeira reuniao", f"{datas[0][6:]}/{datas[0][4:6]}/{datas[0][:4]}", ref["primeira_reuniao"])
    confere("ultima reuniao", f"{datas[-1][6:]}/{datas[-1][4:6]}/{datas[-1][:4]}", ref["ultima_reuniao"])

    print("Constituicao do corpus")
    with (DADOS / "copias_identicas.csv").open(encoding="utf-8-sig") as f:
        copias = len(list(csv.DictReader(f)))
    with (DADOS / "capturas_preteridas.csv").open(encoding="utf-8-sig") as f:
        preteridas = len(list(csv.DictReader(f)))
    confere("copias identicas descartadas", copias, ref["copias_identicas"])
    confere("capturas preteridas", preteridas, ref["capturas_preteridas"])
    confere("PDFs coletados", len(docs) + copias + preteridas, ref["pdfs_coletados"])

    print("Integridade do corpus")
    vistos: dict[str, str] = {}
    for nome, d in docs.items():
        h = hashlib.sha256(d.raw.encode("utf-8")).hexdigest()
        if h in vistos:
            falhas.append(f"duplicata residual: {nome} identico a {vistos[h]}")
        vistos[h] = nome
    print(f"  ok  nenhuma duplicata residual ({len(vistos)} conteudos distintos)")

    print("Qualidade do texto")
    corrompidos = sorted(n for n, d in docs.items() if "\ufffd" in d.raw)
    if corrompidos:
        falhas.append("texto com caractere nao decodificado: " + ", ".join(corrompidos))
    else:
        print("  ok  nenhum documento com caractere nao decodificado")

    print("Varredura")
    zerad_ampl = 0
    for fam in ZERADAS:
        rx = re.compile("|".join(LEXICO[fam]["ampliado"]))
        if not any(rx.search(d.norm) for d in docs.values()):
            zerad_ampl += 1
    confere("familias zeradas no recorte original", len(ZERADAS),
            ref["familias_zeradas_recorte_original"])
    confere("familias ainda zeradas no nivel ampliado", zerad_ampl,
            ref["familias_ainda_zeradas_nivel_ampliado"])

    print("Lacunas declaradas")
    sem_texto = sum(1 for d in docs.values()
                    if len(re.sub(r"\s|=+ \[pag \d+\] =+", "", d.raw)) < 300)
    confere("documentos sem camada de texto", sem_texto, ref["documentos_sem_camada_texto"])

    print("Termos de conferencia")
    with (DADOS / "termos_buscados_conferencia.csv").open(encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    confere("termos literais", len(linhas), ref["termos_literais"])
    confere("termos ausentes", sum(1 for r in linhas if r["situacao"] == "ausente"),
            ref["termos_ausentes"])

    print("Listas do README")
    from reproduzir import MARCA_FIM, MARCA_INICIO, listas
    readme = (BASE / "README.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    bloco = readme[readme.index(MARCA_INICIO):readme.index(MARCA_FIM) + len(MARCA_FIM)]
    if bloco != listas():
        falhas.append("listas de resolucoes e reunioes no README divergem dos inventarios")
    else:
        print("  ok  listas de resolucoes e reunioes conferem com os inventarios")

    print("Cobertura da documentacao")
    dp = json.loads((BASE / "datapackage.json").read_text(encoding="utf-8"))
    declarados = {r["path"] for r in dp["resources"]}
    for p in sorted(DADOS.glob("*.csv")):
        if f"dados/{p.name}" not in declarados:
            falhas.append(f"tabela publicada sem declaracao no datapackage: dados/{p.name}")
    for r in dp["resources"]:
        if not (BASE / r["path"]).exists():
            falhas.append(f"datapackage declara recurso inexistente: {r['path']}")
            continue
        with (BASE / r["path"]).open(encoding="utf-8-sig") as f:
            cabecalho = next(csv.reader(f))
        if cabecalho != [c["name"] for c in r["schema"]["fields"]]:
            falhas.append(f"colunas divergem do datapackage: {r['path']}")
        for campo in r["schema"]["fields"]:
            if not campo["description"] or campo["description"] == "\u2014":
                falhas.append(f"coluna sem descricao: {r['path']}:{campo['name']}")
    print(f"  ok  {len(dp['resources'])} recursos declarados e documentados")

    if falhas:
        print("\nFALHOU:")
        for f_ in falhas:
            print("  -", f_)
        return 1
    print("\nTodos os numeros-ancora conferem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
