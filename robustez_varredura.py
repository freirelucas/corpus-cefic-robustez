"""Varredura robusta do corpus CEFIC.

Objetivo: separar ausencia real de artefato metodologico. Reduzir o texto a um
"esqueleto ASCII" destroi palavras acentuadas, buscar pagina a pagina perde
expressoes que atravessam a quebra, e ignorar a hifenizacao de fim de linha
perde palavras partidas.

Aqui a normalizacao preserva alinhamento 1:1 com o texto original (cada
caractere de entrada gera exatamente um caractere normalizado), de modo que o
KWIC pode ser recortado do original acentuado e a pagina recuperada por offset.
"""
from __future__ import annotations

import re
import unicodedata
from bisect import bisect_right
from pathlib import Path

MARCA = re.compile(r"===== \[pag (\d+)\] =====")

_cache: dict[str, str] = {}


def _dobra(ch: str) -> str:
    """Normaliza um caractere; pode devolver 0, 1 ou N caracteres.

    NFKD expande ligaduras tipograficas de PDF (U+FB01 'fi' -> 'fi'), que de
    outro modo partiriam palavras ao meio ("justificativa" -> "justi cativa").
    """
    if ch in _cache:
        return _cache[ch]
    d = unicodedata.normalize("NFKD", ch)
    base = "".join(c for c in d if not unicodedata.combining(c)).lower()
    out = "".join(c if (c.isalnum() and c.isascii()) else " " for c in base) or " "
    _cache[ch] = out
    return out


class Doc:
    """Texto normalizado + mapa de offsets de volta ao original."""

    __slots__ = ("raw", "norm", "mapa", "_ini", "_pag")

    def __init__(self, raw: str):
        self.raw = raw
        # 1) posicoes a suprimir: hifenizacao de fim de linha e marcadores de pagina
        suprime = set()
        for m in re.finditer(r"-[ \t]*\r?\n[ \t]*", raw):
            suprime.update(range(m.start(), m.end()))
        corta: list[tuple[int, int]] = []  # (offset_norm, pagina)
        marcas = []
        for m in MARCA.finditer(raw):
            marcas.append((m.start(), m.end(), int(m.group(1))))
            suprime.update(range(m.start(), m.end()))

        pedacos: list[str] = []
        mapa: list[int] = []
        pos = 0
        prox = 0
        for i, ch in enumerate(raw):
            while prox < len(marcas) and marcas[prox][0] == i:
                corta.append((pos, marcas[prox][2]))
                prox += 1
            if i in suprime:
                continue
            s = _dobra(ch)
            pedacos.append(s)
            mapa.extend([i] * len(s))
            pos += len(s)
        self.norm = "".join(pedacos)
        self.mapa = mapa
        if corta:
            self._ini = [c[0] for c in corta]
            self._pag = [c[1] for c in corta]
        else:
            self._ini, self._pag = [0], [1]

    def pagina(self, off_norm: int) -> int:
        i = bisect_right(self._ini, off_norm) - 1
        return self._pag[max(i, 0)]

    def orig(self, off_norm: int) -> int:
        return self.mapa[min(off_norm, len(self.mapa) - 1)] if self.mapa else 0

    def kwic(self, a: int, b: int, n: int = 90) -> str:
        oa, ob = self.orig(a), self.orig(max(b - 1, a)) + 1
        ini, fim = max(oa - n, 0), min(ob + n, len(self.raw))
        return re.sub(r"\s+", " ", self.raw[ini:fim]).strip()

    def termo(self, a: int, b: int) -> str:
        oa, ob = self.orig(a), self.orig(max(b - 1, a)) + 1
        return re.sub(r"\s+", " ", self.raw[oa:ob]).strip()


def _esp(frase: str) -> str:
    """Une palavras com \\s+ para tolerar quebras de linha e espacos de OCR."""
    return r"\s+".join(frase.split())


# ---------------------------------------------------------------------------
# Lexico. "estrito" = o conceito tal como definido no desenho da pesquisa.
# "ampliado" = variantes morfologicas, sinonimos e termos vizinhos.
# ---------------------------------------------------------------------------
LEXICO: dict[str, dict[str, list[str]]] = {
    "padrao_aberto": {
        "estrito": [r"padr(ao|oes)\s+abert"],
        # "formato aberto" descartado: no D10977 designa a dimensao fisica da carteira
        "ampliado": [r"padr(ao|oes|onizacao)\s+(tecnic[oa]s?\s+)?abert", r"especificac(ao|oes)\s+abert",
                     r"open\s+standard", r"api\s+(publica|aberta)"],
    },
    "substituicao_fornecedor": {
        "estrito": [r"substituicao\s+(de|do)\s+fornecedor"],
        "ampliado": [r"(substituicao|troca|portabilidade|migracao)\s+(de|do|entre)\s+fornecedor",
                     r"trocar?\s+de\s+fornecedor", r"mudanca\s+de\s+fornecedor",
                     r"substituicao\s+(da|de)\s+(solucao|tecnologia|contratad)"],
    },
    "desenvolvimento_nacional": {
        "estrito": [r"desenvolvimento\s+(tecnologico\s+)?nacional"],
        "ampliado": [r"desenvolvimento\s+(tecnologico\s+)?nacional", r"desenvolvimento\s+local",
                     r"nacionalizacao", r"produc(ao|oes)\s+nacional", r"solucao\s+nacional",
                     r"tecnologia\s+nacional", r"autonomia\s+tecnologica"],
    },
    "empresa_industria_nacional": {
        "estrito": [r"empresa\s+nacional", r"industria\s+nacional"],
        "ampliado": [r"empresas?\s+(nacionais?|brasileiras?)", r"industria\s+nacional",
                     r"fabricante\s+nacional", r"fornecedor(es)?\s+(nacionais?|brasileiros?)",
                     r"capital\s+nacional", r"sediada\s+no\s+(pais|brasil)"],
    },
    "nova_industria_brasil": {
        "estrito": [r"nova\s+industria\s+(do\s+)?brasil", r"\bnib\b"],
        "ampliado": [r"nova\s+industria\s+(do\s+)?brasil", r"\bnib\b",
                     r"politica\s+industrial", r"\bbndes\b", r"\bfinep\b",
                     r"plano\s+(brasil\s+)?mais\s+produtivo"],
    },
    "margem_preferencia": {
        "estrito": [r"margem\s+de\s+preferencia"],
        # "artigo 26" e "preferencialmente" foram testados e descartados: o primeiro casa
        # art. 26 de decretos diversos; o segundo e conceito distinto (preferencia_normativa)
        "ampliado": [r"margens?\s+de\s+preferencia", r"criterio\s+de\s+desempate",
                     r"lei\s+14\.?\s?133", r"preferencia\s+(a|para|por|pelo)\s"],
    },
    "conteudo_local": {
        "estrito": [r"conteudo\s+local"],
        "ampliado": [r"conteudo\s+local", r"indice\s+de\s+nacionalizacao",
                     r"conteudo\s+nacional", r"processo\s+produtivo\s+basico", r"\bppb\b"],
    },
    "encomenda_tecnologica": {
        "estrito": [r"encomenda\s+(tecnologica|publica)"],
        "ampliado": [r"encomenda\s+(tecnologica|publica)", r"\betec\b",
                     r"lei\s+de\s+inovacao", r"contratacao\s+de\s+(solucao\s+)?inovador",
                     r"\bcpsi\b", r"compra\s+publica\s+(de\s+)?inovacao"],
    },
    "software_livre_codigo_aberto": {
        "estrito": [r"software\s+livre", r"codigo\s+aberto"],
        "ampliado": [r"software\s+(livre|publico)", r"codigo\s+aberto", r"open\s+source",
                     r"licenca\s+(livre|publica|gpl|mit|apache)", r"\bgithub\b", r"repositorio\s+publico"],
    },
    "codigo_fonte": {
        "estrito": [r"codigo\s*-?\s*fonte"],
        "ampliado": [r"codigos?\s*-?\s*fontes?", r"acesso\s+ao\s+codigo",
                     r"entrega\s+do\s+codigo", r"source\s+code", r"\bescrow\b"],
    },
    "propriedade_intelectual": {
        "estrito": [r"propriedade\s+intelectual"],
        "ampliado": [r"propriedade\s+(intelectual|industrial)", r"direitos?\s+patrimoniais?",
                     r"\bpatente", r"titularidade\s+(dos?\s+)?(direitos|resultados)",
                     r"\binpi\b", r"licenciamento"],
    },
    "transferencia_tecnologia": {
        "estrito": [r"transferencia\s+de\s+tecnologia"],
        "ampliado": [r"transferencia\s+(de\s+)?(tecnologia|tecnologica|de\s+conhecimento)",
                     r"absorcao\s+tecnologica", r"repasse\s+de\s+tecnologia",
                     r"internalizacao\s+(da\s+)?tecnologia"],
    },
    "capacitacao_tecnologica": {
        "estrito": [r"capacitacao\s+tecnologica"],
        "ampliado": [r"capacitacao\s+(tecnologica|tecnica)?", r"treinamento",
                     r"formacao\s+de\s+(equipes?|pessoal|servidores)", r"qualificacao\s+tecnica"],
    },
    "aprisionamento_lockin": {
        "estrito": [r"aprisionamento", r"lock\s*-?\s*in\b",
                    r"dependencia\s+de\s+(um\s+|qualquer\s+)?fornecedor"],
        "ampliado": [r"aprisionamento", r"lock\s*-?\s*in\b", r"vendor\s+lock",
                     r"dependencia\s+(tecnologica|de\s+fornecedor|do\s+fornecedor|de\s+um\s+fornecedor)",
                     r"\bcativ[oa]s?\b", r"monopoli", r"fornecedor\s+unico", r"exclusividade"],
    },
    # familias nao-zeradas, mantidas para conferir se o esqueleto perdeu ocorrencias
    "interoperabilidade": {"estrito": [r"interoperab"], "ampliado": [r"interoperab", r"integracao\s+de\s+(sistemas|bases)"]},
    "multifornecedor_segundo_motor": {
        "estrito": [r"multifornecedor", r"mais\s+de\s+um\s+fornecedor", r"segundo\s+motor"],
        "ampliado": [r"multi\s*-?\s*fornecedor", r"mais\s+de\s+um\s+fornecedor", r"segundo\s+motor",
                     r"multiplos\s+fornecedores", r"dois\s+fornecedores", r"segunda\s+fonte",
                     r"motor\s+(biometrico|de\s+busca)", r"\babis\b"],
    },
    "concorrencia": {"estrito": [r"concorrencia"], "ampliado": [r"concorrenc", r"competitividade", r"disputa\s+de\s+precos", r"certame", r"pregao"]},
    "soberania": {"estrito": [r"soberan"], "ampliado": [r"soberan", r"autonomia\s+(nacional|tecnologica|digital)"]},
    "territorio_nacional": {"estrito": [r"territorio\s+nacional"], "ampliado": [r"territorio\s+nacional", r"em\s+solo\s+brasileiro", r"datacenter\s+no\s+(pais|brasil)", r"localizacao\s+dos?\s+dados"]},
    "blockchain": {"estrito": [r"blockchain"], "ampliado": [r"block\s*chain", r"\bdlt\b", r"registro\s+distribuido"]},
    "bancos": {"estrito": [r"febraban", r"bancari", r"serasa"], "ampliado": [r"febraban", r"bancari", r"serasa", r"instituic(ao|oes)\s+financeir"]},
    "fomento": {"estrito": [r"fomento"], "ampliado": [r"fomento", r"financiamento\s+publico", r"subvencao"]},
    "acuracia": {"estrito": [r"acuracia"], "ampliado": [r"acuracia", r"acuracidade", r"taxa\s+de\s+(erro|falso)", r"\bfmr\b", r"\bfnmr\b"]},
    "nist_nfiq": {"estrito": [r"nfiq", r"\bnist\b"], "ampliado": [r"nfiq", r"\bnist\b", r"\bminex\b", r"\bfrvt\b"]},
    "policiafederal_aditivo": {"estrito": [r"aditiv"], "ampliado": [r"aditiv", r"prorrogacao\s+contratual", r"policia\s+federal"]},
    # fronteira a esquerda: sem ela, "graficas" casa dentro de "biograficas"
    "graficas": {"estrito": [r"(?<![a-z])graficas"], "ampliado": [r"(?<![a-z])grafica", r"casa\s+da\s+moeda", r"\bcmb\b", r"impressao\s+(do\s+)?documento"]},
    "fala_brasil": {"estrito": [r"fala\s*\.?\s*br"], "ampliado": [r"fala\s*\.?\s*br", r"gov\s*\.?\s*br"]},
    "tier_iii": {"estrito": [r"tier\s*iii"], "ampliado": [r"tier\s*(iii|3)\b", r"\btia\s*942"]},
    "sitios_operacionais": {"estrito": [r"sitios\s+operacionais"], "ampliado": [r"sitios?\s+operacion", r"site\s+de\s+contingencia", r"data\s*center"]},
    # termo do item 3.2 do Anexo I da Res. 21/2025
    "preferencia_normativa": {
        "estrito": [r"preferencialmente"],
        "ampliado": [r"preferencialmente", r"sempre\s+que\s+possivel", r"dar-?se-?a\s+preferencia"],
    },
}

# Familias sem ocorrencia no nivel estrito.
ZERADAS = ["padrao_aberto", "substituicao_fornecedor", "desenvolvimento_nacional",
           "empresa_industria_nacional", "nova_industria_brasil", "margem_preferencia",
           "conteudo_local", "encomenda_tecnologica", "software_livre_codigo_aberto",
           "codigo_fonte", "propriedade_intelectual", "transferencia_tecnologia",
           "capacitacao_tecnologica", "aprisionamento_lockin"]
