"""Gera busca_corpus_cefic.html — ferramenta de busca no corpus, em arquivo unico e autonomo.

    python gerar_busca.py

O arquivo produzido embute o corpus e funciona sem servidor, sem conexao e sem
instalacao: basta baixa-lo e abri-lo no navegador. Nao depende de bibliotecas externas.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

from robustez_varredura import Doc  # noqa: E402

TEXTOS = BASE / "corpus_txt"
DADOS = BASE / "dados"
SAIDA = BASE / "busca_corpus_cefic.html"

CABECALHO = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Corpus CEFIC &middot; busca no texto integral</title>
<style>
  :root{
    --tinta:#1c1a17; --papel:#faf8f4; --linha:#c9c2b6; --linha-forte:#8a8272;
    --apagado:#6b6459; --destaque:#2f5d4f; --destaque-lavado:#e7efea;
    --ausencia:#8a2f2a; --ausencia-lavada:#f0e2e0;
    --sans:"Helvetica Neue",Arial,sans-serif; --serif:Georgia,"Times New Roman",serif;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--serif);
       line-height:1.55;font-size:16px}
  .area{max-width:980px;margin:0 auto;padding:28px 20px 80px}
  header{border-bottom:3px double var(--linha-forte);padding-bottom:18px;margin-bottom:22px}
  .chapeu{font-family:var(--sans);font-size:12px;letter-spacing:.14em;text-transform:uppercase;
          color:var(--apagado);margin-bottom:6px}
  h1{font-size:26px;margin:0 0 8px;font-weight:600}
  .resumo{color:var(--apagado);font-size:15px;max-width:72ch;margin:0}
  .painel{background:#fff;border:1px solid var(--linha);padding:18px;margin-bottom:20px}
  .campo{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
  input[type=search]{flex:1;min-width:260px;font-family:var(--serif);font-size:17px;
       padding:10px 12px;border:1px solid var(--linha-forte);background:var(--papel);color:var(--tinta)}
  input[type=search]:focus{outline:2px solid var(--destaque);outline-offset:1px}
  .opcoes{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;font-family:var(--sans);font-size:13px;
          color:var(--apagado)}
  .opcoes label{display:flex;gap:6px;align-items:center;cursor:pointer}
  .atalhos{margin-top:14px;font-family:var(--sans);font-size:12.5px;color:var(--apagado)}
  .atalhos button{font-family:var(--sans);font-size:12.5px;background:var(--papel);
       border:1px solid var(--linha);color:var(--tinta);padding:4px 9px;margin:3px 4px 0 0;cursor:pointer}
  .atalhos button:hover{background:var(--destaque-lavado);border-color:var(--destaque)}
  .veredito{font-family:var(--sans);font-size:14px;padding:12px 14px;margin:18px 0;
            border-left:4px solid var(--destaque);background:var(--destaque-lavado)}
  .veredito.vazio{border-left-color:var(--ausencia);background:var(--ausencia-lavada)}
  .doc{border-top:1px solid var(--linha);padding:14px 0 4px}
  .doc h2{font-family:var(--sans);font-size:13.5px;font-weight:600;margin:0 0 8px;letter-spacing:.01em}
  .doc h2 span{font-weight:400;color:var(--apagado)}
  .oc{margin:0 0 10px;padding-left:14px;border-left:2px solid var(--linha);font-size:15px}
  .oc .pag{font-family:var(--sans);font-size:11.5px;color:var(--apagado);
           text-transform:uppercase;letter-spacing:.08em;display:block;margin-bottom:2px}
  mark{background:#f6e27a;padding:0 2px}
  .nota{font-family:var(--sans);font-size:12.5px;color:var(--apagado);
        border-top:1px solid var(--linha);margin-top:34px;padding-top:14px}
  .nota p{margin:0 0 7px;max-width:78ch}
  code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92em;background:#f0ece4;padding:1px 4px}
</style>
</head>
<body>
<div class="area">
<header>
  <div class="chapeu">Corpus CEFIC &middot; material de verifica&ccedil;&atilde;o</div>
  <h1>Busca no texto integral do corpus</h1>
  <p class="resumo">__RESUMO__</p>
</header>

<div class="painel">
  <div class="campo">
    <input type="search" id="q" placeholder="digite um termo ou express&atilde;o" autocomplete="off" autofocus>
  </div>
  <div class="opcoes">
    <label><input type="checkbox" id="inteiras" checked> palavras inteiras</label>
    <label><input type="checkbox" id="acentos" checked> ignorar acentos e caixa</label>
    <label><input type="checkbox" id="socefic"> apenas documentos da CEFIC</label>
  </div>
  <div class="atalhos">
    <div>Termos cuja aus&ecirc;ncia sustenta conclus&otilde;es do artigo:</div>
    __ATALHOS__
  </div>
</div>

<div id="veredito"></div>
<div id="saida"></div>

<div class="nota">
__NOTA__
</div>
</div>
<script id="corpus" type="application/json">__DADOS__</script>
<script>
__SCRIPT__
</script>
</body>
</html>
"""

SCRIPT = r"""
const CORPUS = JSON.parse(document.getElementById('corpus').textContent);
// deriva o texto normalizado preservando alinhamento 1:1 com o de exibicao
function dobraAlinhada(t){
  let saida = '';
  for (const ch of t){
    const b = ch.normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase().slice(0,1);
    saida += (b >= 'a' && b <= 'z') || (b >= '0' && b <= '9') ? b : ' ';
  }
  return saida;
}
for (const doc of CORPUS.d) doc.n = dobraAlinhada(doc.t);
const q = document.getElementById('q');
const saida = document.getElementById('saida');
const veredito = document.getElementById('veredito');
const opInteiras = document.getElementById('inteiras');
const opAcentos = document.getElementById('acentos');
const opCefic = document.getElementById('socefic');

function dobra(s){
  return s.normalize('NFKD').replace(/[\u0300-\u036f]/g,'').toLowerCase()
          .replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();
}
function escapaRe(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'); }
function escapaHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function paginaDe(doc, pos){
  let i = 0;
  while (i + 1 < doc.c.length && doc.c[i+1][0] <= pos) i++;
  return doc.c.length ? doc.c[i][1] : 1;
}

function buscar(){
  const bruto = q.value.trim();
  saida.innerHTML = '';
  if (!bruto){ veredito.innerHTML = ''; return; }

  const usarDobra = opAcentos.checked;
  const alvo = usarDobra ? dobra(bruto) : bruto;
  if (!alvo){ veredito.innerHTML = ''; return; }
  let padrao = escapaRe(alvo).replace(/ /g, usarDobra ? ' ' : '\\s+');
  if (opInteiras.checked) padrao = '(?<![a-z0-9\\u00c0-\\u024f])' + padrao + '(?![a-z0-9\\u00c0-\\u024f])';
  let rx;
  try { rx = new RegExp(padrao, usarDobra ? 'g' : 'gi'); }
  catch(e){ veredito.className='veredito vazio';
            veredito.textContent='Express\u00e3o de busca inv\u00e1lida.'; return; }

  let totalOc = 0, totalDocs = 0;
  const blocos = [];
  for (const doc of CORPUS.d){
    if (opCefic.checked && !doc.k) continue;
    const base = usarDobra ? doc.n : doc.t;
    rx.lastIndex = 0;
    const achados = [];
    let m;
    while ((m = rx.exec(base)) !== null){
      achados.push([m.index, m.index + m[0].length]);
      if (m.index === rx.lastIndex) rx.lastIndex++;
      if (achados.length > 300) break;
    }
    if (!achados.length) continue;
    totalDocs++; totalOc += achados.length;
    let html = '<div class="doc"><h2>' + escapaHtml(doc.a) +
               (doc.k ? '' : ' <span>&middot; documento de contexto</span>') + '</h2>';
    for (const [a,b] of achados){
      const ini = Math.max(a-110, 0), fim = Math.min(b+110, doc.t.length);
      const antes = escapaHtml(doc.t.slice(ini, a)).replace(/\s+/g,' ');
      const meio  = escapaHtml(doc.t.slice(a, b)).replace(/\s+/g,' ');
      const dep   = escapaHtml(doc.t.slice(b, fim)).replace(/\s+/g,' ');
      html += '<p class="oc"><span class="pag">p&aacute;gina ' + paginaDe(doc, a) + '</span>' +
              (ini>0?'&hellip;':'') + antes + '<mark>' + meio + '</mark>' + dep +
              (fim<doc.t.length?'&hellip;':'') + '</p>';
    }
    blocos.push(html + '</div>');
  }

  const escopo = opCefic.checked ? CORPUS.kc : CORPUS.n;
  if (!totalOc){
    veredito.className = 'veredito vazio';
    veredito.innerHTML = 'Nenhuma ocorr&ecirc;ncia de <strong>' + escapaHtml(bruto) +
      '</strong> nos ' + escopo + ' documentos pesquisados.';
  } else {
    veredito.className = 'veredito';
    veredito.innerHTML = '<strong>' + totalOc + '</strong> ocorr&ecirc;ncia' + (totalOc>1?'s':'') +
      ' de <strong>' + escapaHtml(bruto) + '</strong> em <strong>' + totalDocs +
      '</strong> documento' + (totalDocs>1?'s':'') + ', de um total de ' + escopo + '.';
  }
  saida.innerHTML = blocos.join('');
}

let timer;
function agenda(){ clearTimeout(timer); timer = setTimeout(buscar, 140); }
q.addEventListener('input', agenda);
for (const el of [opInteiras, opAcentos, opCefic]) el.addEventListener('change', buscar);
document.querySelectorAll('.atalhos button').forEach(b => {
  b.addEventListener('click', () => { q.value = b.dataset.t || b.textContent; buscar(); q.focus(); });
});
"""


def prepara(raw: str) -> tuple[str, str, list[list[int]]]:
    """raw -> (texto de exibicao, texto normalizado, cortes de pagina).

    Os dois textos tem o mesmo comprimento, caractere a caractere, de modo que
    uma posicao encontrada no normalizado recorta o trecho certo no de exibicao.
    Ligaduras tipograficas sao expandidas no texto de exibicao ("gra\ufb01cas" ->
    "graficas"), o que corrige a extracao e mantem a busca previsivel.
    """
    import unicodedata

    marcas = {m.start(): (m.end(), int(m.group(1)))
              for m in re.finditer(r"===== \[pag (\d+)\] =====", raw)}
    # hifenizacao de fim de linha: "inte-\nroperabilidade" e costurada, como no pipeline
    suprime = set()
    for m in re.finditer(r"-[ \t]*\r?\n[ \t]*", raw):
        suprime.update(range(m.start(), m.end()))
    exib: list[str] = []
    norm: list[str] = []
    cortes: list[list[int]] = []
    i = 0
    while i < len(raw):
        if i in marcas:
            fim, pagina = marcas[i]
            cortes.append([len(exib), pagina])
            i = fim
            continue
        if i in suprime:
            i += 1
            continue
        ch = raw[i]
        base = "".join(c for c in unicodedata.normalize("NFKD", ch)
                       if not unicodedata.combining(c))
        saida = base if (len(base) > 1 and base.isalnum() and base.isascii()) else ch
        for x in saida:
            exib.append(x)
            b = "".join(c for c in unicodedata.normalize("NFKD", x)
                        if not unicodedata.combining(c)).lower()[:1]
            norm.append(b if (b.isalnum() and b.isascii()) else " ")
        i += 1
    return "".join(exib), "".join(norm), (cortes or [[0, 1]])


def main() -> None:
    num = json.loads((DADOS / "numeros_verificados.json").read_text(encoding="utf-8"))
    docs = []
    for f in sorted(TEXTOS.glob("*.txt")):
        raw = f.read_text(encoding="utf-8", errors="replace")
        exib, norm, cortes = prepara(raw)
        assert len(exib) == len(norm), f"desalinhamento em {f.stem}"
        eh_cefic = bool(re.search(r"\bcefic\b|camara executiva federal de identificacao",
                                  norm[:3000]))
        # "n" nao e embutido: o navegador o deriva de "t" com o mesmo algoritmo,
        # caractere a caractere, o que mantem o alinhamento e reduz o arquivo a metade
        docs.append({"a": f.stem, "t": exib, "c": cortes, "k": 1 if eh_cefic else 0})

    ausentes = ["margem de prefer\u00eancia", "conte\u00fado local", "encomenda tecnol\u00f3gica",
                "transfer\u00eancia de tecnologia", "c\u00f3digo-fonte", "software livre",
                "padr\u00e3o aberto", "aprisionamento", "substitui\u00e7\u00e3o de fornecedor",
                "desenvolvimento nacional"]
    presentes = ["credenciamento", "interoperabilidade", "territ\u00f3rio nacional",
                 "preferencialmente", "soberania"]
    atalhos = "".join(f'<button data-t="{t}">{t}</button>' for t in ausentes)
    atalhos += '<div style="margin-top:10px">Termos presentes, para compara&ccedil;&atilde;o:</div>'
    atalhos += "".join(f'<button data-t="{t}">{t}</button>' for t in presentes)

    resumo = (f"Pesquisa direta nos {num['documentos_canonicos']} documentos distintos do corpus da "
              f"C&acirc;mara Executiva Federal de Identifica&ccedil;&atilde;o do Cidad&atilde;o "
              f"(CEFIC), {num['paginas']} p&aacute;ginas, com corte em {num['corte']}. "
              "Cada ocorr&ecirc;ncia &eacute; exibida com o documento, a p&aacute;gina e o "
              "trecho em que aparece.")

    nota = f"""  <p><strong>FIGURA 1</strong><br>Ferramenta de busca no texto integral do corpus CEFIC</p>
  <p>Fonte: corpus documental da CEFIC, {num['documentos_canonicos']} documentos distintos,
     {num['paginas']} p&aacute;ginas, corte em {num['corte']}.</p>
  <p>Elabora&ccedil;&atilde;o dos autores.</p>
  <p>Nota: a busca percorre o texto integral dos documentos. Com a op&ccedil;&atilde;o
     <em>ignorar acentos e caixa</em> ativada, <code>resolucao</code> encontra
     &ldquo;Resolu&ccedil;&atilde;o&rdquo;. Com <em>palavras inteiras</em> ativada,
     <code>NIB</code> deixa de casar dentro de &ldquo;disponibilidade&rdquo;. As ligaduras
     tipogr&aacute;ficas dos PDFs s&atilde;o expandidas antes da compara&ccedil;&atilde;o,
     de modo que <code>gr&aacute;ficas</code> encontra tamb&eacute;m as ocorr&ecirc;ncias
     grafadas com o caractere &uacute;nico &ldquo;&#64257;&rdquo;.</p>
  <p>Obs.: dos {num['documentos_canonicos']} documentos, {num['documentos_cefic']} s&atilde;o atos
     ou registros da pr&oacute;pria CEFIC e {num['documentos_contexto']} s&atilde;o documentos de
     contexto de outros &oacute;rg&atilde;os; o filtro permite restringir a busca aos primeiros.
     Dois documentos n&atilde;o possuem camada de texto e n&atilde;o s&atilde;o alcan&ccedil;ados
     por nenhuma busca, conforme <code>dados/lacunas_cobertura.csv</code>.</p>"""

    html = (CABECALHO
            .replace("__RESUMO__", resumo)
            .replace("__ATALHOS__", atalhos)
            .replace("__NOTA__", nota)
            .replace("__SCRIPT__", SCRIPT)
            .replace("__DADOS__", json.dumps(
                {"d": docs, "n": len(docs), "kc": sum(x["k"] for x in docs)},
                ensure_ascii=False, separators=(",", ":"))))
    SAIDA.write_text(html, encoding="utf-8")
    print(f"busca_corpus_cefic.html gerado: {len(html)//1024} KB, {len(docs)} documentos")



if __name__ == "__main__":
    main()
