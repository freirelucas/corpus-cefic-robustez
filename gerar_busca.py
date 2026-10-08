"""Gera busca_corpus_cefic.html — ferramenta de busca no corpus, em arquivo unico e autonomo.

    python gerar_busca.py

O arquivo produzido embute o corpus e funciona sem servidor, sem conexao e sem
instalacao: basta baixa-lo e abri-lo no navegador. Nao depende de bibliotecas externas.
"""
from __future__ import annotations

import csv
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
REPOSITORIO = "https://github.com/freirelucas/corpus-cefic-robustez/blob/main/corpus_txt/"

CABECALHO = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Corpus CEFIC &middot; busca no texto integral</title>
<style>
  :root{
    --tinta:#1c1a17; --papel:#faf8f4; --linha:#d6cfc3; --linha-forte:#8a8272;
    --apagado:#6b6459; --destaque:#2f5d4f; --destaque-lavado:#e7efea;
    --ausencia:#8a2f2a; --ausencia-lavada:#f3e6e4; --marca:#f6e27a; --marca-ativa:#e8a33d;
    --sans:"Helvetica Neue",Arial,sans-serif; --serif:Georgia,"Times New Roman",serif;
  }
  *{box-sizing:border-box}
  html,body{height:100%}
  body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--serif);
       line-height:1.5;font-size:15px;display:flex;flex-direction:column}
  header{padding:14px 20px 12px;border-bottom:1px solid var(--linha);background:#fff}
  .linha-topo{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
  h1{font-size:19px;margin:0;font-weight:600}
  .resumo{font-family:var(--sans);font-size:12.5px;color:var(--apagado)}
  .controles{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-top:10px}
  input[type=search]{flex:1;min-width:220px;font-family:var(--serif);font-size:16px;
       padding:8px 11px;border:1px solid var(--linha-forte);background:var(--papel);color:var(--tinta)}
  input[type=search]:focus{outline:2px solid var(--destaque);outline-offset:1px}
  .seg{display:inline-flex;border:1px solid var(--linha-forte);font-family:var(--sans);font-size:12.5px}
  .seg button{border:0;background:#fff;padding:7px 11px;cursor:pointer;color:var(--tinta)}
  .seg button+button{border-left:1px solid var(--linha-forte)}
  .seg button[aria-pressed=true]{background:var(--destaque);color:#fff}
  .opcoes{display:flex;gap:14px;font-family:var(--sans);font-size:12.5px;color:var(--apagado)}
  .opcoes label{display:flex;gap:5px;align-items:center;cursor:pointer}
  .atalhos{margin-top:9px;font-family:var(--sans);font-size:12px;color:var(--apagado);
           display:flex;flex-wrap:wrap;gap:5px;align-items:center}
  .atalhos .rot{margin-right:2px}
  .atalhos .rot+button{margin-left:0}
  .atalhos button{font-family:var(--sans);font-size:12px;background:var(--papel);
       border:1px solid var(--linha);color:var(--tinta);padding:3px 8px;cursor:pointer}
  .atalhos button.aus{border-color:#d9b8b4}
  .atalhos button:hover{border-color:var(--destaque)}
  .sep{width:12px}
  main{flex:1;min-height:0;display:grid;grid-template-columns:minmax(320px,2fr) 3fr}
  .esq{min-height:0;display:flex;flex-direction:column;border-right:1px solid var(--linha)}
  .abas{display:flex;font-family:var(--sans);font-size:13px;border-bottom:1px solid var(--linha);background:#fff}
  .abas button{flex:1;border:0;background:transparent;padding:9px;cursor:pointer;color:var(--apagado);
               border-bottom:2px solid transparent}
  .abas button[aria-selected=true]{color:var(--tinta);border-bottom-color:var(--destaque);font-weight:600}
  .painel{flex:1;overflow:auto;padding:12px 16px 30px}
  .veredito{font-family:var(--sans);font-size:13px;padding:9px 12px;margin:0 0 12px;
            border-left:4px solid var(--destaque);background:var(--destaque-lavado)}
  .veredito.vazio{border-left-color:var(--ausencia);background:var(--ausencia-lavada)}
  .grupo{border-top:1px solid var(--linha);padding:10px 0 4px}
  .grupo h2{font-family:var(--sans);font-size:13px;font-weight:600;margin:0;cursor:pointer}
  .grupo h2:hover{color:var(--destaque)}
  .grupo h2 .n{font-weight:400;color:var(--apagado)}
  .grupo .sub{font-family:var(--sans);font-size:12px;color:var(--apagado);margin:2px 0 6px}
  .oc{margin:0 0 6px;padding:4px 8px;border-left:2px solid var(--linha);font-size:14px;cursor:pointer}
  .oc:hover,.oc.sel{background:var(--destaque-lavado);border-left-color:var(--destaque)}
  .oc .pag{font-family:var(--sans);font-size:11px;color:var(--apagado);margin-right:6px}
  mark{background:var(--marca);padding:0 1px}
  .lista h3{font-family:var(--sans);font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;
            color:var(--apagado);margin:14px 0 6px;font-weight:600}
  .item{display:block;width:100%;text-align:left;border:0;border-bottom:1px solid #ebe5da;background:none;
        padding:7px 4px;cursor:pointer;font-family:var(--serif);font-size:14px;color:var(--tinta)}
  .item:hover,.item.sel{background:var(--destaque-lavado)}
  .item b{font-family:var(--sans);font-size:12.5px}
  .item span{display:block;font-size:13px;color:var(--apagado)}
  .visor{min-height:0;display:flex;flex-direction:column;background:#fff}
  .visor-topo{padding:12px 18px;border-bottom:1px solid var(--linha);font-family:var(--sans);font-size:12.5px}
  .visor-topo h3{margin:0 0 3px;font-size:15px}
  .visor-topo .meta{color:var(--apagado)}
  .visor-topo .meta a{color:var(--destaque)}
  .nav{display:flex;gap:8px;align-items:center;margin-top:8px;flex-wrap:wrap}
  .nav button{font-family:var(--sans);font-size:12px;background:var(--papel);border:1px solid var(--linha);
              padding:3px 9px;cursor:pointer;color:var(--tinta)}
  .nav button:hover{border-color:var(--destaque)}
  .fechar{display:none}
  .texto{position:relative;flex:1;overflow:auto;padding:14px 22px 40px;white-space:pre-wrap;
         font-size:14.5px;line-height:1.6}
  .texto .pg{display:block;font-family:var(--sans);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;
             color:var(--apagado);border-top:1px dashed var(--linha);margin:14px 0 6px;padding-top:4px}
  .texto mark.ativa{background:var(--marca-ativa);outline:2px solid #b4741a}
  .vazio-visor{color:var(--apagado);font-family:var(--sans);font-size:13px;padding:22px;white-space:normal}
  footer{font-family:var(--sans);font-size:11.5px;color:var(--apagado);padding:7px 20px;
         border-top:1px solid var(--linha);background:#fff}
  footer code{font-size:11px;background:#f0ece4;padding:0 3px}
  @media (max-width:900px){
    body{height:auto}
    main{display:block}
    .esq{border-right:0}
    .painel{overflow:visible}
    .visor{display:none;position:fixed;inset:0;z-index:10}
    .visor.aberto{display:flex}
    .fechar{display:inline-block}
  }
</style>
</head>
<body>
<header>
  <div class="linha-topo">
    <h1>Corpus CEFIC &middot; busca no texto integral</h1>
    <span class="resumo">__RESUMO__</span>
  </div>
  <div class="controles">
    <input type="search" id="q" placeholder="termo ou express&atilde;o" autocomplete="off" autofocus>
    <div class="seg" role="group" aria-label="escopo">
      <button id="escArtigo" aria-pressed="true">corpus do artigo (__NA__)</button>
      <button id="escCompleto" aria-pressed="false">corpus completo (__NC__)</button>
    </div>
    <div class="opcoes">
      <label><input type="checkbox" id="inteiras" checked> palavras inteiras</label>
      <label><input type="checkbox" id="acentos" checked> ignorar acentos e caixa</label>
    </div>
  </div>
  <div class="atalhos">__ATALHOS__</div>
</header>
<main>
  <section class="esq">
    <div class="abas" role="tablist">
      <button id="abaBusca" role="tab" aria-selected="true">Ocorr&ecirc;ncias</button>
      <button id="abaDocs" role="tab" aria-selected="false">Documentos</button>
    </div>
    <div class="painel" id="painelBusca"><div id="veredito"></div><div id="saida"></div></div>
    <div class="painel lista" id="painelDocs" hidden></div>
  </section>
  <aside class="visor" id="visor">
    <div class="visor-topo" id="visorTopo"></div>
    <div class="texto" id="visorTexto"></div>
  </aside>
</main>
<footer>__NOTA__</footer>
<script id="corpus" type="application/json">__DADOS__</script>
<script>
__SCRIPT__
</script>
</body>
</html>
"""

SCRIPT = r"""
const CORPUS = JSON.parse(document.getElementById('corpus').textContent);
// texto normalizado com alinhamento 1:1 ao texto de exibicao
function dobraAlinhada(t){
  let saida = '';
  for (const ch of t){
    const b = ch.normalize('NFKD').replace(/[̀-ͯ]/g,'').toLowerCase().slice(0,1);
    saida += (b >= 'a' && b <= 'z') || (b >= '0' && b <= '9') ? b : ' ';
  }
  return saida;
}
for (const doc of CORPUS.d) doc.n = dobraAlinhada(doc.t);

const $ = id => document.getElementById(id);
const q = $('q'), saida = $('saida'), veredito = $('veredito');
const opInteiras = $('inteiras'), opAcentos = $('acentos');
const visor = $('visor'), visorTopo = $('visorTopo'), visorTexto = $('visorTexto');
const estado = {escopo: 'artigo', aba: 'busca', di: null, k: 0};
let resultados = {};

function dobra(s){
  return s.normalize('NFKD').replace(/[̀-ͯ]/g,'').toLowerCase()
          .replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();
}
function escapaRe(s){ return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'); }
function escapaHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function paginaDe(doc, pos){
  let i = 0;
  while (i + 1 < doc.c.length && doc.c[i+1][0] <= pos) i++;
  return doc.c.length ? doc.c[i][1] : 1;
}
function noEscopo(doc){ return estado.escopo === 'completo' || doc.ar; }
function totalEscopo(){ return CORPUS.d.filter(noEscopo).length; }

function expressao(){
  const bruto = q.value.trim();
  if (!bruto) return null;
  const usarDobra = opAcentos.checked;
  const alvo = usarDobra ? dobra(bruto) : bruto;
  if (!alvo) return null;
  let padrao = escapaRe(alvo).replace(/ /g, usarDobra ? ' ' : '\\s+');
  if (opInteiras.checked) padrao = '(?<![a-z0-9\\u00c0-\\u024f])' + padrao + '(?![a-z0-9\\u00c0-\\u024f])';
  try { return {rx: new RegExp(padrao, usarDobra ? 'g' : 'gi'), usarDobra, bruto}; }
  catch(e){ return {erro: true, bruto}; }
}

function procura(doc, ex){
  const base = ex.usarDobra ? doc.n : doc.t, achados = [];
  ex.rx.lastIndex = 0;
  let m;
  while ((m = ex.rx.exec(base)) !== null){
    achados.push([m.index, m.index + m[0].length]);
    if (m.index === ex.rx.lastIndex) ex.rx.lastIndex++;
    if (achados.length >= 500) break;
  }
  return achados;
}

function trecho(doc, a, b){
  const ini = Math.max(a - 90, 0), fim = Math.min(b + 90, doc.t.length);
  const f = s => escapaHtml(s).replace(/\s+/g, ' ');
  return (ini > 0 ? '&hellip;' : '') + f(doc.t.slice(ini, a)) + '<mark>' + f(doc.t.slice(a, b)) +
         '</mark>' + f(doc.t.slice(b, fim)) + (fim < doc.t.length ? '&hellip;' : '');
}

function buscar(){
  resultados = {};
  saida.innerHTML = '';
  const ex = expressao();
  if (!ex){
    veredito.className = ''; veredito.innerHTML = '';
    saida.innerHTML = '<p class="vazio-visor">Digite um termo ou escolha um dos atalhos acima. ' +
      'A aba <em>Documentos</em> lista as resolu&ccedil;&otilde;es e as reuni&otilde;es.</p>';
    if (estado.di !== null) abre(estado.di, 0, false);
    sincroniza(); return;
  }
  if (ex.erro){
    veredito.className = 'veredito vazio';
    veredito.textContent = 'Expressão de busca inválida.'; return;
  }
  let totalOc = 0;
  const blocos = [];
  CORPUS.d.forEach((doc, di) => {
    if (!noEscopo(doc)) return;
    const achados = procura(doc, ex);
    if (!achados.length) return;
    resultados[di] = achados;
    totalOc += achados.length;
    let html = '<div class="grupo"><h2 data-d="' + di + '">' + escapaHtml(doc.ti) +
               ' <span class="n">&middot; ' + achados.length + '</span></h2>' +
               '<div class="sub">' + escapaHtml(doc.su) + '</div>';
    achados.forEach(([a, b], k) => {
      html += '<p class="oc" data-d="' + di + '" data-k="' + k + '"><span class="pag">p. ' +
              paginaDe(doc, a) + '</span>' + trecho(doc, a, b) + '</p>';
    });
    blocos.push(html + '</div>');
  });
  const nDocs = Object.keys(resultados).length, tot = totalEscopo();
  if (!totalOc){
    veredito.className = 'veredito vazio';
    veredito.innerHTML = 'Nenhuma ocorr&ecirc;ncia de <strong>' + escapaHtml(ex.bruto) +
      '</strong> nos ' + tot + ' documentos do ' + rotuloEscopo() + '.';
  } else {
    veredito.className = 'veredito';
    veredito.innerHTML = '<strong>' + totalOc + '</strong> ocorr&ecirc;ncia' + (totalOc > 1 ? 's' : '') +
      ' de <strong>' + escapaHtml(ex.bruto) + '</strong> em <strong>' + nDocs + '</strong> de ' + tot +
      ' documentos do ' + rotuloEscopo() + '.';
  }
  saida.innerHTML = blocos.join('');
  if (estado.di !== null && resultados[estado.di]) abre(estado.di, Math.min(estado.k, resultados[estado.di].length - 1), false);
  else if (nDocs && window.innerWidth > 900) abre(+Object.keys(resultados)[0], 0, false);
  else if (estado.di !== null && noEscopo(CORPUS.d[estado.di])) abre(estado.di, 0, false);
  else limpaVisor();
  sincroniza();
}

function rotuloEscopo(){ return estado.escopo === 'artigo' ? 'corpus do artigo' : 'corpus completo'; }

function renderiza(doc, achados){
  const ops = [];
  for (const [pos, pag] of doc.c) ops.push([pos, 1, '<span class="pg">p&aacute;gina ' + pag + '</span>']);
  achados.forEach(([a, b], k) => { ops.push([a, 2, '<mark id="m' + k + '">']); ops.push([b, 0, '</mark>']); });
  ops.sort((x, y) => x[0] - y[0] || x[1] - y[1]);
  let html = '', pos = 0;
  for (const [p, , tag] of ops){ html += escapaHtml(doc.t.slice(pos, p)) + tag; pos = p; }
  return html + escapaHtml(doc.t.slice(pos));
}

function limpaVisor(){
  estado.di = null;
  visorTopo.innerHTML = '';
  visorTexto.innerHTML = '<div class="vazio-visor">Selecione uma ocorr&ecirc;ncia ou um documento ' +
    'para ler o texto integral, com as ocorr&ecirc;ncias assinaladas e a indica&ccedil;&atilde;o das p&aacute;ginas.</div>';
}

function abre(di, k, abrirNoCelular = true){
  const doc = CORPUS.d[di], achados = resultados[di] || [];
  const mesmo = estado.di === di && visorTexto.dataset.q === q.value + estado.escopo;
  estado.di = di; estado.k = k;
  if (abrirNoCelular) visor.classList.add('aberto');
  if (!mesmo){
    visorTexto.innerHTML = renderiza(doc, achados);
    visorTexto.dataset.q = q.value + estado.escopo;
    visorTexto.scrollTop = 0;
  }
  const n = achados.length;
  visorTopo.innerHTML = '<h3>' + escapaHtml(doc.ti) + '</h3><div class="meta">' + escapaHtml(doc.su) +
    '</div><div class="meta">' + escapaHtml(doc.g) + ' &middot; <a href="' + CORPUS.u + encodeURIComponent(doc.a) +
    '.txt" target="_blank" rel="noopener">' + escapaHtml(doc.a) + '.txt</a>' +
    (doc.o ? ' &middot; ' + escapaHtml(doc.o) : '') + '</div><div class="nav">' +
    (n ? '<button id="ant">&larr; anterior</button><span>ocorr&ecirc;ncia ' + (k + 1) + ' de ' + n +
         ' &middot; p&aacute;gina ' + paginaDe(doc, achados[k][0]) + '</span><button id="prox">pr&oacute;xima &rarr;</button>'
       : '<span>' + doc.c.length + ' p&aacute;gina' + (doc.c.length > 1 ? 's' : '') + '</span>') +
    '<button class="fechar" id="fechar">fechar</button></div>';
  if (n){
    $('ant').onclick = () => abre(di, (k - 1 + n) % n);
    $('prox').onclick = () => abre(di, (k + 1) % n);
    visorTexto.querySelectorAll('mark.ativa').forEach(m => m.classList.remove('ativa'));
    const alvo = $('m' + k);
    if (alvo){ alvo.classList.add('ativa'); visorTexto.scrollTop = alvo.offsetTop - visorTexto.clientHeight / 3; }
  }
  $('fechar').onclick = () => visor.classList.remove('aberto');
  document.querySelectorAll('.oc.sel, .item.sel').forEach(e => e.classList.remove('sel'));
  const oc = saida.querySelector('.oc[data-d="' + di + '"][data-k="' + k + '"]');
  if (oc) oc.classList.add('sel');
  const item = $('painelDocs').querySelector('.item[data-d="' + di + '"]');
  if (item) item.classList.add('sel');
  sincroniza();
}

function listaDocumentos(){
  const grupos = [['res', 'Resoluções'], ['reu', 'Reuniões'], ['out', 'Demais documentos']];
  let html = '';
  for (const [g, rot] of grupos){
    const itens = CORPUS.d.map((doc, di) => [doc, di]).filter(([doc]) => doc.ca === g && noEscopo(doc));
    if (!itens.length) continue;
    html += '<h3>' + rot + ' (' + itens.length + ')</h3>';
    for (const [doc, di] of itens){
      const n = resultados[di] ? ' &middot; ' + resultados[di].length + ' ocorr.' : '';
      html += '<button class="item" data-d="' + di + '"><b>' + escapaHtml(doc.ti) + '</b>' + n +
              '<span>' + escapaHtml(doc.su) + '</span></button>';
    }
  }
  $('painelDocs').innerHTML = html;
}

function mostraAba(aba){
  estado.aba = aba;
  $('abaBusca').setAttribute('aria-selected', aba === 'busca');
  $('abaDocs').setAttribute('aria-selected', aba === 'docs');
  $('painelBusca').hidden = aba !== 'busca';
  $('painelDocs').hidden = aba !== 'docs';
  if (aba === 'docs') listaDocumentos();
  sincroniza();
}

function defineEscopo(esc){
  estado.escopo = esc;
  $('escArtigo').setAttribute('aria-pressed', esc === 'artigo');
  $('escCompleto').setAttribute('aria-pressed', esc === 'completo');
  if (estado.di !== null && !noEscopo(CORPUS.d[estado.di])) estado.di = null;
  buscar();
  if (estado.aba === 'docs') listaDocumentos();
}

// estado no endereco, para compartilhar uma busca: #q=...&escopo=...&doc=...
function sincroniza(){
  const p = new URLSearchParams();
  if (q.value.trim()) p.set('q', q.value.trim());
  if (estado.escopo !== 'artigo') p.set('escopo', estado.escopo);
  if (estado.di !== null) p.set('doc', CORPUS.d[estado.di].a);
  if (estado.aba === 'docs') p.set('aba', 'documentos');
  const h = p.toString();
  history.replaceState(null, '', h ? '#' + h : location.pathname + location.search);
}
function restaura(){
  const p = new URLSearchParams(location.hash.slice(1));
  if (p.get('q')) q.value = p.get('q');
  if (p.get('escopo') === 'completo') estado.escopo = 'completo';
  $('escArtigo').setAttribute('aria-pressed', estado.escopo === 'artigo');
  $('escCompleto').setAttribute('aria-pressed', estado.escopo === 'completo');
  const di = CORPUS.d.findIndex(d => d.a === p.get('doc'));
  if (di >= 0) estado.di = di;
  if (p.get('aba') === 'documentos') mostraAba('docs');
}

let timer;
q.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(buscar, 160); });
for (const el of [opInteiras, opAcentos]) el.addEventListener('change', buscar);
$('escArtigo').onclick = () => defineEscopo('artigo');
$('escCompleto').onclick = () => defineEscopo('completo');
$('abaBusca').onclick = () => mostraAba('busca');
$('abaDocs').onclick = () => mostraAba('docs');
document.querySelectorAll('.atalhos button').forEach(b =>
  b.addEventListener('click', () => { q.value = b.dataset.t; mostraAba('busca'); buscar(); }));
saida.addEventListener('click', e => {
  const oc = e.target.closest('.oc'), h = e.target.closest('h2[data-d]');
  if (oc) abre(+oc.dataset.d, +oc.dataset.k);
  else if (h) abre(+h.dataset.d, 0);
});
$('painelDocs').addEventListener('click', e => {
  const it = e.target.closest('.item');
  if (it) abre(+it.dataset.d, 0);
});
document.addEventListener('keydown', e => {
  if (e.target === q || estado.di === null) return;
  const n = (resultados[estado.di] || []).length;
  if (!n) return;
  if (e.key === 'ArrowRight' || e.key === 'j') abre(estado.di, (estado.k + 1) % n);
  if (e.key === 'ArrowLeft' || e.key === 'k') abre(estado.di, (estado.k - 1 + n) % n);
});
restaura();
buscar();
if (estado.di !== null && !resultados[estado.di]) abre(estado.di, 0, false);
"""


def prepara(raw: str) -> tuple[str, str, list[list[int]]]:
    """raw -> (texto de exibicao, texto normalizado, cortes de pagina).

    Os dois textos tem o mesmo comprimento, caractere a caractere, de modo que
    uma posicao encontrada no normalizado recorta o trecho certo no de exibicao.
    Ligaduras tipograficas sao expandidas no texto de exibicao ("gra\ufb01cas" ->
    "graficas").
    """
    import unicodedata

    marcas = {m.start(): (m.end(), int(m.group(1)))
              for m in re.finditer(r"===== \[pag (\d+)\] =====", raw)}
    # hifenizacao de fim de linha: "inte-\nroperabilidade" e costurada, como na varredura
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




def le(nome: str) -> list[dict]:
    with (DADOS / nome).open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main() -> None:
    num = json.loads((DADOS / "numeros_verificados.json").read_text(encoding="utf-8"))
    inv = {r["arquivo"]: r for r in le("inventario_documentos.csv")}
    res = {r["arquivo"]: r for r in le("inventario_resolucoes.csv")}
    reu = {r["arquivos_registro"]: r for r in le("inventario_reunioes.csv")}

    def chave(arq: str):
        r = inv[arq]
        if r["categoria"] == "resolucao":
            return (0, int(r["numero"]), "")
        if r["categoria"] == "registro_reuniao":
            d = reu[arq]
            return (1, int(d["data"][6:] + d["data"][3:5] + d["data"][:2]), d["ordem_declarada"])
        return (2, 0, r["categoria"] + r["documento"])

    docs = []
    for arq in sorted(inv, key=chave):
        raw = (TEXTOS / f"{arq}.txt").read_text(encoding="utf-8", errors="replace")
        exib, norm, cortes = prepara(raw)
        assert len(exib) == len(norm), f"desalinhamento em {arq}"
        r = inv[arq]
        if r["categoria"] == "resolucao":
            e = res[arq]
            titulo, sub, grupo = f"Resolução nº {e['numero']}, de {e['data']}", e["ementa"], "res"
        elif r["categoria"] == "registro_reuniao":
            d = reu[arq]
            decl = " ".join(x for x in (d["ordem_declarada"], d["tipo_declarado"]) if x) or "ordem e tipo não declarados"
            titulo, sub, grupo = f"Reunião de {d['data']}", f"{decl} · {d['modalidade']}", "reu"
        else:
            titulo, sub, grupo = r["documento"], r["data_documento"] or "", "out"
        # "n" nao e embutido: o navegador o deriva de "t" com o mesmo algoritmo,
        # caractere a caractere, o que mantem o alinhamento e reduz o arquivo
        docs.append({"a": arq, "t": exib, "c": cortes, "ti": titulo, "su": sub, "ca": grupo,
                     "ar": 1 if grupo in ("res", "reu") else 0, "g": r["orgao"],
                     "o": r["observacao"]})

    ausentes = ["transferência de tecnologia", "conteúdo local", "encomenda tecnológica",
                "margem de preferência", "desenvolvimento nacional", "código-fonte",
                "software livre", "padrão aberto", "substituição de fornecedor",
                "aprisionamento"]
    presentes = ["interoperabilidade", "território nacional", "preferencialmente",
                 "mais de um fornecedor", "concorrência", "soberania"]
    atalhos = '<span class="rot">sem ocorr&ecirc;ncia no artigo:</span>'
    atalhos += "".join(f'<button class="aus" data-t="{t}">{t}</button>' for t in ausentes)
    atalhos += '<span class="sep"></span><span class="rot">presentes:</span>'
    atalhos += "".join(f'<button data-t="{t}">{t}</button>' for t in presentes)

    resumo = (f"{num['documentos_artigo']} documentos do artigo (33 resolu&ccedil;&otilde;es e 40 "
              f"registros de reuni&atilde;o) em um corpus de {num['documentos']}, "
              f"{num['paginas']} p&aacute;ginas, coleta em {num['corte']}")
    nota = ("Busca no texto integral. <em>Ignorar acentos e caixa</em>: <code>resolucao</code> "
            "encontra &ldquo;Resolu&ccedil;&atilde;o&rdquo;. <em>Palavras inteiras</em>: "
            "<code>NIB</code> n&atilde;o casa em &ldquo;disponibilidade&rdquo;. Ligaduras "
            "tipogr&aacute;ficas expandidas. Setas &larr; &rarr; percorrem as ocorr&ecirc;ncias do "
            "documento aberto. O endere&ccedil;o da p&aacute;gina guarda a busca e pode ser "
            "compartilhado. Um documento sem camada de texto: "
            "<code>dados/lacunas_cobertura.csv</code>.")

    html = (CABECALHO
            .replace("__RESUMO__", resumo)
            .replace("__NA__", str(num["documentos_artigo"]))
            .replace("__NC__", str(num["documentos"]))
            .replace("__ATALHOS__", atalhos)
            .replace("__NOTA__", nota)
            .replace("__SCRIPT__", SCRIPT)
            .replace("__DADOS__", json.dumps({"d": docs, "u": REPOSITORIO},
                                             ensure_ascii=False, separators=(",", ":"))
                     .replace("</", "<\\/")))
    SAIDA.write_text(html, encoding="utf-8", newline="\n")
    print(f"busca_corpus_cefic.html gerado: {len(html)//1024} KB, {len(docs)} documentos")


if __name__ == "__main__":
    main()
