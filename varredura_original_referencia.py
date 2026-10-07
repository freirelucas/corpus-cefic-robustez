import csv
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
TEXTOS = BASE / "corpus_cefic" / "textos"
ANALISE = BASE / "analise_cefic"

# padroes casados sobre esqueleto ASCII (minusculas, nao-alfanumerico vira espaco)
FAMILIAS = {
    "interoperabilidade": r"interoperab",
    "multifornecedor_segundo_motor": r"multifornecedor|mais de um fornecedor|segundo motor",
    "padrao_aberto": r"padr[a-z ]{0,4}o?s? abert",
    "substituicao_fornecedor": r"substitui[a-z ]{0,3}o de fornecedor",
    "concorrencia": r"concorr\s?ncia",
    "desenvolvimento_nacional": r"desenvolvimento (tecnol[a-z ]{0,4}gico )?nacional",
    "empresa_industria_nacional": r"empresa nacional|ind[a-z ]{0,3}stria nacional",
    "nova_industria_brasil": r"nova ind[a-z ]{0,3}stria (do )?brasil|\bnib\b",
    "margem_preferencia": r"margem de prefer[a-z ]{0,3}ncia",
    "conteudo_local": r"conte[a-z ]{0,3}do local",
    "encomenda_tecnologica": r"encomenda (tecnol[a-z ]{0,4}gica|p[a-z ]{0,4}blica)",
    "software_livre_codigo_aberto": r"software livre|c[a-z ]{0,2}digo aberto",
    "codigo_fonte": r"c[a-z ]{0,2}digo[a-z -]{0,2}fonte",
    "propriedade_intelectual": r"propriedade intelectual",
    "transferencia_tecnologia": r"transfer[a-z ]{0,3}ncia de tecnologia",
    "capacitacao_tecnologica": r"capacita[a-z ]{0,3}o tecnol[a-z ]{0,4}gica",
    "aprisionamento_lockin": r"aprisionamento|lock[\s-]{1,2}in\b|lockin\b|depend[a-z ]{0,3}ncia de (um |qualquer )?fornecedor",
    "blockchain": r"block[a-z ]{0,1}chain",
    "soberania": r"soberan",
    "territorio_nacional": r"territ[a-z ]{0,3}rio nacional",
    "bancos": r"febraban|banc[a-z ]{0,4}ri|serasa",
    "fomento": r"fomento",
    "acuracia": r"acur[a-z ]{0,3}cia",
    "nist_nfiq": r"nfiq|\bnist\b",
    "policiafederal_aditivo": r"aditiv\w*",
    "graficas": r"gr[a-z ]{0,3}ficas",
    "fala_brasil": r"fala\.br",
    "tier_iii": r"tier\s{0,2}iii",
    "sitios_operacionais": r"s[a-z ]{0,3}tios operacionais",
}

CITACOES = {
    "E4_segundo_motor": r"segundo motor",
    "E5_apenas_uma_digital": r"apenas uma digital",
    "E6_migracao_sugerida": r"sugerindo[a-z ]{0,3}se sua migra[a-z ]{0,3}o",
    "E7_aditivar_pf": r"aditivar?\s+(o\s+)?contrato",
    "E8_teste_nacional": r"teste nacional",
    "E9_graficas": r"gr[a-z ]{0,3}ficas",
    "E11_banco_interesse": r"sistema banc[a-z ]{0,4}rio",
    "migracao": r"migra[a-z ]{0,3}o",
}

MARCA = re.compile(r"===== \[pag (\d+)\] =====")


def esqueleto(t: str) -> str:
    t = t.lower()
    t = re.sub(r"[^a-z0-9./]+", " ", t)
    return re.sub(r"\s+", " ", t)


def normaliza(t: str) -> str:
    return re.sub(r"\s+", " ", t)


def contexto(t: str, a: int, b: int, n: int = 90) -> str:
    ini, fim = max(a - n, 0), min(b + n, len(t))
    return normaliza(t[ini:fim]).strip()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ANALISE.mkdir(parents=True, exist_ok=True)
    docs, n_pags = [], 0
    fam_total, fam_docs = defaultdict(int), defaultdict(set)
    kwic_rows, cit_rows = [], []
    for txt in sorted(TEXTOS.glob("*.txt")):
        raw = txt.read_text(encoding="utf-8")
        partes = MARCA.split(raw)
        pages = [(int(partes[i]), esqueleto(partes[i + 1])) for i in range(1, len(partes), 2)]
        if not pages:
            pages = [(1, esqueleto(raw))]
        n_pags += len(pages)
        docs.append(txt.stem)
        for fam, pat in FAMILIAS.items():
            rx = re.compile(pat)
            for pag, t in pages:
                for m in rx.finditer(t):
                    fam_total[fam] += 1
                    fam_docs[fam].add(txt.stem)
                    kwic_rows.append({"familia": fam, "arquivo": txt.stem, "pagina": pag, "trecho": contexto(t, m.start(), m.end())})
        for cid, pat in CITACOES.items():
            rx = re.compile(pat)
            for pag, t in pages:
                for m in rx.finditer(t):
                    cit_rows.append({"citacao": cid, "arquivo": txt.stem, "pagina": pag, "trecho": contexto(t, m.start(), m.end())})

    freq_rows = [{"familia": f, "total": fam_total[f], "docs": len(fam_docs[f])} for f in FAMILIAS]
    with (ANALISE / "freq_termos_cefic.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["familia", "total", "docs"])
        w.writeheader()
        w.writerows(freq_rows)
    with (ANALISE / "kwic_cefic.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["familia", "arquivo", "pagina", "trecho"])
        w.writeheader()
        w.writerows(kwic_rows)
    with (ANALISE / "citacoes_fichas.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["citacao", "arquivo", "pagina", "trecho"])
        w.writeheader()
        w.writerows(cit_rows)

    linhas = sum(raw.count("\n") + 1 for raw in (t.read_text(encoding="utf-8") for t in TEXTOS.glob("*.txt")))
    with (ANALISE / "relatorio_varredura.md").open("w", encoding="utf-8") as f:
        f.write(f"# Varredura do corpus CEFIC v2 - esqueleto ASCII ({date.today().isoformat()})\n\n")
        f.write(f"Documentos: {len(docs)} | paginas: {n_pags} | linhas: {linhas:,} | kwic: {len(kwic_rows)}\n\n".replace(",", "."))
        f.write("## 1. Familias (total / docs)\n\n| familia | total | docs |\n|---|---|---|\n")
        for r in freq_rows:
            f.write(f"| {r['familia']} | {r['total']} | {r['docs']} |\n")
        f.write("\n## 2. Citacoes das fichas E\n\n| citacao | ocorrencias |\n|---|---|\n")
        for cid in CITACOES:
            f.write(f"| {cid} | {sum(1 for c in cit_rows if c['citacao'] == cid)} |\n")
    print(f"docs={len(docs)} pags={n_pags} linhas={linhas} kwic={len(kwic_rows)} citas={len(cit_rows)}")
    print("familias:", ", ".join(f"{k}={v}" for k, v in sorted(fam_total.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
