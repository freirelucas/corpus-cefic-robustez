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


def carrega() -> dict[str, Doc]:
    return {f.stem: Doc(f.read_text(encoding="utf-8", errors="replace"))
            for f in sorted(TEXTOS.glob("*.txt"))}


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


def main() -> None:
    DADOS.mkdir(exist_ok=True)
    docs = carrega()
    est = varre(docs, "estrito")
    amp = varre(docs, "ampliado")
    campos = ["familia", "arquivo", "pagina", "termo", "trecho"]
    escreve("kwic_cefic_corrigido.csv", est, campos)
    escreve("kwic_cefic_ampliado.csv", amp, campos)

    def agrega(linhas):
        tot, dd = {}, {}
        for r in linhas:
            tot[r["familia"]] = tot.get(r["familia"], 0) + 1
            dd.setdefault(r["familia"], set()).add(r["arquivo"])
        return tot, dd

    te, de = agrega(est)
    ta, da = agrega(amp)
    freq = [{"familia": f, "estrito_total": te.get(f, 0), "estrito_docs": len(de.get(f, ())),
             "ampliado_total": ta.get(f, 0), "ampliado_docs": len(da.get(f, ())),
             "zerada_no_recorte_original": f in ZERADAS} for f in LEXICO]
    escreve("freq_termos_robusto.csv", freq,
            ["familia", "estrito_total", "estrito_docs", "ampliado_total", "ampliado_docs",
             "zerada_no_recorte_original"])

    paginas = sum(len(re.findall(r"===== \[pag \d+\] =====", d.raw)) or 1 for d in docs.values())
    linhas_txt = sum(d.raw.count("\n") + 1 for d in docs.values())
    resumo = {"documentos": len(docs), "paginas": paginas, "linhas": linhas_txt,
              "familias": len(LEXICO), "kwic_estrito": len(est), "kwic_ampliado": len(amp),
              "familias_zeradas_no_recorte_original": len(ZERADAS),
              "familias_que_seguem_zeradas_no_nivel_ampliado":
                  sum(1 for f in ZERADAS if ta.get(f, 0) == 0)}
    (DADOS / "resumo_reproducao.json").write_text(
        json.dumps(resumo, indent=1, ensure_ascii=False), encoding="utf-8")
    for k, v in resumo.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
