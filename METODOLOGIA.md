# Metodologia

Documento complementar ao [README](README.md). Descreve o percurso do corpus, os cuidados
técnicos que o procedimento exige e o que ele não alcança.

## Constituição do corpus

A coleta, realizada em 14/09/2026 em sítios oficiais do governo federal e no Diário Oficial
da União, reuniu 154 PDFs: resoluções e registros de reunião da CEFIC, atos que a criaram e
regulamentaram, portarias de designação de seus integrantes e documentos de contexto.

O corpus foi constituído em três passos, cada um com registro próprio:

1. **Cópias byte-idênticas.** Vinte e quatro PDFs eram cópias exatas de outros e foram
   descartados ([`dados/copias_identicas.csv`](dados/copias_identicas.csv)).
2. **Uma captura por documento.** Vinte e cinco PDFs eram capturas adicionais de documentos
   já presentes: a mesma resolução publicada no Diário Oficial e em arquivo próprio, a mesma
   memória de reunião em duas versões, páginas integrais do Diário Oficial que continham uma
   resolução ao lado de atos de outros órgãos e uma captura sem camada de texto. De cada
   documento manteve-se uma única captura, pela seguinte regra: excluem-se as capturas sem
   camada de texto, com caracteres não decodificados ou com atos de outros órgãos; entre as
   restantes, mantém-se a de texto mais extenso. As capturas preteridas estão em
   [`dados/capturas_preteridas.csv`](dados/capturas_preteridas.csv), com o motivo de cada
   exclusão.
3. **Classificação dos documentos.** Cada um dos 105 documentos restantes foi classificado
   por categoria e órgão emissor ([`dados/inventario_documentos.csv`](dados/inventario_documentos.csv)),
   a partir da leitura do cabeçalho de cada texto. A classificação é um dado curado, publicado
   para conferência, e dela deriva o recorte dos atos da CEFIC.

**Reuniões.** [`dados/inventario_reunioes.csv`](dados/inventario_reunioes.csv) registra uma
linha por reunião, identificada pela data e, quando há duas na mesma data, pela ordem. São 40
reuniões com registro, de 14/03/2022 a 11/08/2026, ordinárias e extraordinárias, um documento
por reunião. A ordem e o tipo constam tais como declarados no cabeçalho de cada registro; em
seis reuniões o cabeçalho omite a ordem ou o tipo, ou diverge do nome do arquivo ou da
sequência das demais reuniões do ano, e as divergências estão assinaladas. Três documentos de
2022 contêm os slides exibidos em reuniões que também têm ata e não são contados como
registros.

**Resoluções.** [`dados/inventario_resolucoes.csv`](dados/inventario_resolucoes.csv) registra
as resoluções nº 1 a 33, sem lacuna, e duas retificações, com os dados de publicação no
Diário Oficial.

**Corpus do artigo e corpus completo.** O artigo analisa as 33 resoluções e os registros das
40 reuniões — 73 documentos, o corpus do artigo. Os demais 32 documentos — retificações,
apresentações, relatórios técnicos, anexo, portarias, leis, decretos, norma técnica e
relatório de outro órgão — formam com eles o corpus completo, de 105 documentos. Os
resultados são apresentados para os dois conjuntos.

## Procedimento de busca

O artigo analisa duas dimensões: concorrência e contestabilidade, e capacidades tecnológicas
nacionais. Para cada uma, o procedimento parte de uma lista de termos agrupados em famílias —
conjuntos de expressões que designam um mesmo conceito. "Transferência de tecnologia",
"transferência tecnológica" e "absorção tecnológica" pertencem à mesma família.

Cada documento é percorrido integralmente em busca dessas expressões. Toda ocorrência
encontrada é registrada com **arquivo e página**, acompanhada do trecho de texto ao redor — o
formato que a linguística de corpus denomina KWIC, *key word in context*. Cada afirmação do
artigo baseada no corpus pode assim ser rastreada até uma linha de
[`dados/kwic_estrito.csv`](dados/kwic_estrito.csv) e, dali, até a página do documento.

As buscas são feitas em dois níveis. O nível **estrito** procura o conceito tal como definido
no desenho da pesquisa. O nível **ampliado** acrescenta variantes, sinônimos e termos
vizinhos: para a família de aprisionamento tecnológico, admite "lock-in", "vendor lock",
"dependência de fornecedor", "fornecedor único", "exclusividade" e "monopólio". O nível
ampliado testa se uma ausência se mantém sob critério mais amplo.

## Cuidados que condicionam o resultado

Documentos em PDF impõem dificuldades à busca textual, tratadas em `robustez_varredura.py`.

**Ligaduras tipográficas.** Programas de diagramação representam os pares "fi" e "fl" por um
único caractere, ﬁ e ﬂ. Um procedimento que descarte caracteres fora do alfabeto básico parte
a palavra ao meio: "grá**ﬁ**cas" tornar-se-ia "grá cas". O corpus contém
789 ligaduras, distribuídas por 49 documentos. A normalização adotada expande essas
ligaduras, de modo que a grafia com caractere único e a grafia com dois caracteres sejam
tratadas como a mesma palavra.

**Acentuação.** A busca compara o texto sem diacríticos, para que "território" e
"territorio" constituam a mesma busca. A normalização remove apenas o diacrítico e preserva a
letra; substituir a letra acentuada por um espaço partiria a palavra ("licita o").

**Início de palavra.** Expressões curtas casam no interior de outras palavras: "licitação"
dentro de "solicitação", "NIB" dentro de "disponibilidade", "cativo" dentro de "aplicativo".
Os padrões de busca ancoram no início da palavra sempre que essa confusão é possível.

**Hifenização e quebra de página.** Palavras partidas no fim da linha são costuradas antes da
busca, e a varredura percorre o documento inteiro em lugar de página a página, para que
expressões que atravessem a quebra sejam encontradas. A página é recuperada em seguida, pela
posição da ocorrência.

A normalização preserva um mapa de posições de volta ao texto original, de maneira que o
trecho KWIC exibido seja o texto real, acentuado, e não a forma achatada usada na comparação.

## Limitações declaradas

**Um documento não possui camada de texto** e nenhuma busca o alcança
([`dados/lacunas_cobertura.csv`](dados/lacunas_cobertura.csv)): `Fluxo_CIN_V7`, sem conteúdo
nem autoria verificáveis. Todas as 33 resoluções têm texto pesquisável.

**A busca é lexical.** Encontra o termo, não a ideia expressa por outras palavras. O nível
ampliado mitiga o problema sem eliminá-lo. Caso identificado: o registro da reunião de
22/04/2025 menciona a proposta de "um teste nacional de acurácia de motores biométricos para
reduzir a dependência de padrões internacionais no sistema biométrico brasileiro", que o
léxico da família de aprisionamento ("dependência tecnológica", "dependência de fornecedor")
não alcança. A passagem está registrada em
[FUNDAMENTACAO_DO_QUADRO.md](FUNDAMENTACAO_DO_QUADRO.md).

**O vocabulário provém da literatura, não do corpus.** Termos que os próprios documentos
empregam ficaram fora do recorte declarado — entre eles credenciamento, contrato, auditoria,
dispensa, certificação e homologação.
[`dados/sonda_vocabulario_nativo.csv`](dados/sonda_vocabulario_nativo.csv) lista esses termos
com as respectivas frequências no corpus e nos documentos da CEFIC, e
[PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md) registra os de maior
frequência. Um recorte construído a partir do vocabulário dos documentos produziria um
conjunto distinto de resultados.

**As famílias não têm forma comparável entre as dimensões.** Os termos da dimensão de
capacidades tecnológicas são expressões de duas ou três palavras — "margem de preferência",
"encomenda tecnológica"; os da outra dimensão são, em boa parte, palavras isoladas —
"interoperabilidade", "soberania". Expressões longas têm probabilidade de ocorrência literal
menor que palavras únicas, qualquer que seja o corpus. Parte do contraste entre as duas
dimensões decorre dessa assimetria, e não apenas do conteúdo dos documentos.

**Ordem e tipo das reuniões.** Os registros nem sempre concordam entre si quanto à ordem e ao
tipo da reunião. O número de reuniões não depende dessa divergência; a distribuição entre
ordinárias e extraordinárias, sim, e por isso não é declarada como resultado.

## Verificação

`teste_reproducao.py` refaz a varredura sobre o corpus e confere os números declarados —
documentos, páginas, linhas, ligaduras, documentos da CEFIC, resoluções, reuniões, cópias
descartadas, capturas preteridas, famílias sem ocorrência no nível ampliado, documentos sem
camada de texto e total de termos ausentes —, falhando se algum divergir. Confere também a
correspondência entre o inventário e o corpus, a existência de um único arquivo por
documento, a coerência entre o inventário de documentos e o de reuniões, a inexistência de
texto com caractere não decodificado e a descrição, no dicionário de dados, de toda tabela e
coluna publicada. A verificação é executada a cada alteração enviada ao repositório.
