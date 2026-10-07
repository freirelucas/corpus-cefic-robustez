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
            for f in sorted(TEXTOS.glob("*.txt"))}

    print("Corpus")
    confere("documentos", len(docs), ref["documentos_canonicos"])
    paginas = sum(len(re.findall(r"===== \[pag \d+\] =====", d.raw)) or 1 for d in docs.values())
    confere("paginas", paginas, ref["paginas"])
    confere("linhas", sum(d.raw.count("\n") + 1 for d in docs.values()), ref["linhas"])

    print("Integridade do corpus")
    vistos: dict[str, str] = {}
    for nome, d in docs.items():
        h = hashlib.sha256(d.raw.encode("utf-8")).hexdigest()
        if h in vistos:
            falhas.append(f"duplicata residual: {nome} identico a {vistos[h]}")
        vistos[h] = nome
    print(f"  ok  nenhuma duplicata residual ({len(vistos)} conteudos distintos)")

    print("Qualidade do texto")
    corrompidos = {n: d.raw.count("\ufffd") for n, d in docs.items() if "\ufffd" in d.raw}
    declarados = set()
    caminho_versoes = DADOS / "versoes_mesmo_documento.csv"
    if caminho_versoes.exists():
        with caminho_versoes.open(encoding="utf-8-sig") as f:
            declarados = {r["arquivo"] for r in csv.DictReader(f)
                          if int(r["caracteres_corrompidos"]) > 0}
    nao_declarados = set(corrompidos) - declarados
    if nao_declarados:
        falhas.append("texto corrompido nao declarado: " + ", ".join(sorted(nao_declarados)))
    else:
        print(f"  ok  {len(corrompidos)} documento(s) com caractere corrompido, todos declarados")

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

    print("Cobertura da documentacao")
    dp = json.loads((BASE / "datapackage.json").read_text(encoding="utf-8"))
    for r in dp["resources"]:
        if not (BASE / r["path"]).exists():
            falhas.append(f"datapackage declara recurso inexistente: {r['path']}")
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
