# Fundamentação do quadro de dimensões

Este documento liga cada item do quadro de dimensões analíticas do artigo aos termos
efetivamente buscados no corpus e ao resultado obtido. Permite verificar, item a item, em que a afirmação do texto se apoia.

Corpus: 129 documentos distintos, 663 páginas, corte em 15/09/2026.
A busca percorre o texto integral e registra arquivo e página de cada ocorrência.

## Dimensão 1 — Concorrência e contestabilidade

| item do quadro | termos buscados | ocorrências | documentos | resultado |
|---|---|---|---|---|
| padrões abertos | API aberta; API pública; especificação aberta; especificações abertas; open standard; padronização aberta; padrão aberto; padrões abertos | 0 | 0 | **ausente** |
| interoperabilidade | interoperab | 34 | 19 | **presente** |
| condições para substituição de fornecedores | migração de fornecedor; mudança de fornecedor; portabilidade de fornecedor; substituição da solução; substituição de fornecedor; substituição de tecnologia; substituição do fornecedor; tr… | 3 | 3 | **presente** |
| código aberto | GitHub; código aberto; licença livre; licença pública; open source; repositório público; software livre; software público | 0 | 0 | **ausente** |
| software livre | GitHub; código aberto; licença livre; licença pública; open source; repositório público; software livre; software público | 0 | 0 | **ausente** |
| aprisionamento tecnológico | aprisionamento; cativo; dependência de fornecedor; dependência do fornecedor; dependência tecnológica; exclusividade; fornecedor único; lock in; lock-in; monopólio; vendor lock | 0 | 0 | **ausente** |

Observação sobre o terceiro item: as três ocorrências correspondem a *multifornecedor* e
*segundo motor* — a preferência por mais de um fornecedor de algoritmos. O sintagma
*substituição de fornecedor* e suas variantes não ocorrem no corpus. A presença, portanto, é
de uma preferência por pluralidade de fornecedores, não de um mecanismo de substituição.

## Dimensão 2 — Desenvolvimento tecnológico nacional

| item do quadro | termos buscados | ocorrências | documentos | resultado |
|---|---|---|---|---|
| mecanismos de contratação ou outros instrumentos de estímulo ao nacional | CPSI; ETEC; Lei 14.133; Lei de Inovação; PPB; conteúdo local; conteúdo nacional; contratação de solução inovadora; critério de desempate; encomenda pública; encomenda tecnológica; margem … | 0 | 0 | **ausente** |
| desenvolvimento tecnológico nacional | autonomia tecnológica; desenvolvimento local; desenvolvimento nacional; desenvolvimento tecnológico nacional; nacionalização; produção nacional; solução nacional; tecnologia nacional | 0 | 0 | **ausente** |
| incentivo a empresa nacional | BNDES; FINEP; NIB; Nova Indústria Brasil; capital nacional; empresa nacional; empresas nacionais; fabricante nacional; fornecedor nacional; fornecedores nacionais; indústria nacional; pol… | 0 | 0 | **ausente** |

A única ocorrência no léxico ampliado é a razão social "Empresa Brasileira de Participações
em Energia Nuclear" em documento de outro órgão, que não sustenta a presença do conceito.

## Síntese

Dos nove itens do quadro, **sete não ocorrem no corpus** e dois ocorrem. Os 97 termos
ausentes, de um total de 100 buscados, estão listados um a um em
[TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md); cada ocorrência dos itens presentes está em
[`dados/kwic_estrito.csv`](dados/kwic_estrito.csv), com arquivo e página.
A ferramenta [`busca_corpus_cefic.html`](busca_corpus_cefic.html) permite verificar qualquer termo diretamente no corpus.

## Termos buscados além do quadro

O levantamento cobriu também termos que o quadro não declara, mas que sustentam afirmações
do corpo do texto. Ficam registrados para que a correspondência entre o que se buscou e o
que se afirma seja completa. As presenças não incorporadas ao artigo estão examinadas em
[AGENDA_DE_PESQUISA.md](AGENDA_DE_PESQUISA.md).

| termo | ocorrências | documentos | sustenta no texto |
|---|---|---|---|
| Território nacional | 38 | 16 | hospedagem em território nacional (Res. 21/2025, item 3.1) |
| NIST / NFIQ | 16 | 8 | padrões internacionais de qualidade biométrica (NIST, NFIQ) |
| Sítios operacionais | 2 | 2 | redundância de sítios operacionais |
| Tier III | 2 | 2 | certificação Tier III |
| Preferência normativa | 12 | 10 | preferência normativa ("preferencialmente") |

Fonte: corpus documental da CEFIC.
Elaboração dos autores.
