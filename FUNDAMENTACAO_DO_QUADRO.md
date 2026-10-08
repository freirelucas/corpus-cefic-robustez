# Fundamentação do quadro de dimensões

Este documento liga cada item do quadro de dimensões analíticas do artigo aos termos
efetivamente buscados no corpus e ao resultado obtido. Permite verificar, item a item, em que
a afirmação do texto se apoia.

Corpus: 129 arquivos de texto, correspondentes a 105 documentos, 663 páginas, coleta em
14/09/2026. A busca percorre o texto integral e registra arquivo e página de cada ocorrência.
Nas tabelas, "arquivos" e "documentos" diferem quando o mesmo documento consta em mais de uma
captura.

## Dimensão 1 — Concorrência e contestabilidade

| item do quadro | termos buscados | ocorrências | arquivos | documentos | resultado |
|---|---|---|---|---|---|
| padrões abertos | API aberta; API pública; especificação aberta; especificações abertas; open standard; padronização aberta; padrão aberto; padrões abertos | 0 | 0 | 0 | **ausente** |
| interoperabilidade | interoperab | 34 | 19 | 15 | **presente** |
| condições para substituição de fornecedores | migração de fornecedor; mudança de fornecedor; portabilidade de fornecedor; substituição da solução; substituição de fornecedor; substituição de tecnologia; substituição do fornecedor; troca de fornecedor; trocar de fornecedor; mais de um fornecedor; multifornecedor; segundo motor | 3 | 3 | 2 | **presente apenas como pluralidade de fornecedores** |
| código aberto | GitHub; código aberto; licença livre; licença pública; open source; repositório público; software livre; software público | 0 | 0 | 0 | **ausente** |
| software livre | GitHub; código aberto; licença livre; licença pública; open source; repositório público; software livre; software público | 0 | 0 | 0 | **ausente** |
| aprisionamento tecnológico | aprisionamento; cativo; dependência de fornecedor; dependência do fornecedor; dependência tecnológica; exclusividade; fornecedor único; lock in; lock-in; monopólio; vendor lock | 0 | 0 | 0 | **ausente** |

Composição do terceiro item. Nenhuma das expressões de substituição de fornecedor ocorre, nem
no nível ampliado. As três ocorrências vêm de dois documentos: a Resolução nº 21/2025, cujo
item 3.2 do Anexo I estabelece que o Serviço Biométrico Federal deve "ter, preferencialmente,
mais de um fornecedor dos algoritmos do motor biométrico" — em duas capturas —, e o registro
da reunião de 13/05/2026, que informa que "o segundo motor está sendo adquirido". O item
está presente como pluralidade de fornecedores, não como regra de substituição.

## Dimensão 2 — Desenvolvimento tecnológico nacional

| item do quadro | termos buscados | ocorrências | arquivos | documentos | resultado |
|---|---|---|---|---|---|
| mecanismos de contratação ou outros instrumentos de estímulo ao nacional | CPSI; ETEC; Lei 14.133; Lei de Inovação; PPB; conteúdo local; conteúdo nacional; contratação de solução inovadora; critério de desempate; encomenda pública; encomenda tecnológica; margem de preferência; margens de preferência; processo produtivo básico; índice de nacionalização | 0 | 0 | 0 | **ausente** |
| desenvolvimento tecnológico nacional | autonomia tecnológica; desenvolvimento local; desenvolvimento nacional; desenvolvimento tecnológico nacional; nacionalização; produção nacional; solução nacional; tecnologia nacional | 0 | 0 | 0 | **ausente** |
| incentivo a empresa nacional | BNDES; FINEP; NIB; Nova Indústria Brasil; capital nacional; empresa nacional; empresas nacionais; fabricante nacional; fornecedor nacional; fornecedores nacionais; indústria nacional; política industrial; sediada no país | 0 | 0 | 0 | **ausente** |

A única ocorrência no léxico ampliado da dimensão é a razão social "Empresa Brasileira de
Participações em Energia Nuclear", em ato de outro órgão publicado na mesma página do Diário
Oficial que a Resolução nº 1.

## Síntese

Dos nove itens do quadro, **sete não ocorrem no corpus**, um ocorre (interoperabilidade) e
um ocorre apenas em forma parcial (pluralidade de fornecedores, sem regra de substituição).
As expressões dos itens ausentes estão listadas uma a uma em
[TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md); cada ocorrência dos itens presentes está em
[`dados/kwic_estrito.csv`](dados/kwic_estrito.csv), com arquivo e página. A ferramenta
[`busca_corpus_cefic.html`](busca_corpus_cefic.html) permite verificar qualquer termo
diretamente no corpus.

## Termos buscados além do quadro

O levantamento cobriu também termos que o quadro não declara e que correspondem a
afirmações do corpo do texto. Ficam registrados para que a correspondência entre o que se
buscou e o que se afirma seja completa. As presenças não incorporadas ao artigo constam de
[PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md).

| termo | ocorrências | arquivos | documentos | sustenta no texto |
|---|---|---|---|---|
| Território nacional | 38 | 16 | 13 | hospedagem em território nacional (Res. 21/2025, Anexo I, item 3.1) |
| NIST / NFIQ | 16 | 8 | 5 | padrões internacionais de qualidade biométrica (Res. 21/2025, Anexo I, item 1.1.1) |
| Sítios operacionais | 2 | 2 | 1 | redundância de sítios operacionais (Res. 21/2025, Anexo I, item 3.3) |
| Tier III | 2 | 2 | 1 | certificação Tier III (Res. 21/2025, Anexo I, item 3.3) |
| Preferência normativa | 12 | 10 | 7 | preferência normativa ("preferencialmente") |

Fonte: corpus documental da CEFIC.
Elaboração dos autores.
