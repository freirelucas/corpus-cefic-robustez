# Metodologia

Documento complementar ao [README](README.md). Descreve o percurso do corpus, os cuidados
técnicos que o procedimento exige e o que ele não alcança.

## Constituição do corpus

A coleta, realizada em 14/09/2026 em sítios oficiais do governo federal e no Diário Oficial
da União, reuniu 154 PDFs: resoluções e registros de reunião da CEFIC, atos que a criaram e
regulamentaram, portarias de designação de seus integrantes e documentos de contexto.

O corpus foi constituído em três passos, cada um com registro próprio:

1. **Cópias byte-idênticas.** Vinte e quatro PDFs eram cópias exatas de outros e foram
   descartados ([`dados/copias_identicas.csv`](dados/copias_identicas.csv)). Contá-los
   elevaria as frequências sem acrescentar evidência.
2. **Capturas preteridas.** O registro da reunião de 10/06/2025 constava em dois PDFs
   distintos; a extração de texto de um deles saiu com caracteres não decodificados, e o texto
   publicado provém do outro ([`dados/capturas_preteridas.csv`](dados/capturas_preteridas.csv)).
3. **Identificação dos documentos.** Cada um dos 129 arquivos de texto restantes foi
   atribuído ao documento a que corresponde, com categoria e órgão emissor
   ([`dados/inventario_documentos.csv`](dados/inventario_documentos.csv)). Os 129 arquivos
   correspondem a 105 documentos: 24 documentos constam em duas capturas de conteúdo distinto
   — a resolução publicada no Diário Oficial e em arquivo próprio, ou duas versões da mesma
   memória de reunião. Nenhuma delas foi descartada, pois os textos diferem; as tabelas de
   resultado contam por arquivo e por documento.

A atribuição de cada arquivo ao documento, à categoria e ao órgão emissor resulta de leitura
do cabeçalho de cada texto e é, portanto, um dado curado, publicado para conferência. Dela
derivam todas as contagens por documento e o recorte dos atos da CEFIC.

**Reuniões.** [`dados/inventario_reunioes.csv`](dados/inventario_reunioes.csv) registra uma
linha por reunião, identificada pela data e, quando há duas na mesma data, pela ordem. São 40
reuniões com registro, de 14/03/2022 a 11/08/2026, ordinárias e extraordinárias. A ordem e o
tipo constam tais como declarados no cabeçalho de cada registro; em seis reuniões o cabeçalho
omite a ordem ou o tipo, ou diverge do nome do arquivo ou da sequência das demais reuniões do
ano, e as divergências estão assinaladas. Três arquivos de 2022 contêm os slides exibidos em reuniões que também têm ata e
não são contados como registros.

**Resoluções.** [`dados/inventario_resolucoes.csv`](dados/inventario_resolucoes.csv) registra
os 54 arquivos de resolução e retificação, que correspondem às resoluções nº 1 a 33, sem
lacuna, e a duas retificações.

## Procedimento de busca

O artigo analisa duas dimensões: concorrência e contestabilidade, e capacidades tecnológicas
nacionais. Para cada uma, o procedimento parte de uma lista de termos agrupados em famílias —
conjuntos de expressões que designam um mesmo conceito. "Transferência de tecnologia",
"transferência tecnológica" e "absorção tecnológica" pertencem à mesma família.

Cada arquivo é percorrido integralmente em busca dessas expressões. Toda ocorrência
encontrada é registrada com **arquivo e página**, acompanhada do trecho de texto ao redor — o
formato que a linguística de corpus denomina KWIC, *key word in context*. Cada afirmação do
artigo baseada no corpus pode assim ser rastreada até uma linha de
[`dados/kwic_estrito.csv`](dados/kwic_estrito.csv) e, dali, até a página do documento.

As buscas são feitas em dois níveis. O nível **estrito** procura o conceito tal como definido
no desenho da pesquisa. O nível **ampliado** acrescenta variantes, sinônimos e termos
vizinhos: para a família de aprisionamento tecnológico, admite "lock-in", "vendor lock",
"dependência de fornecedor", "fornecedor único", "exclusividade" e "monopólio". O nível
ampliado não serve para elevar contagens, e sim para testar se uma ausência resiste a critério
deliberadamente mais generoso.

## Cuidados que condicionam o resultado

Documentos em PDF impõem dificuldades à busca textual, tratadas em `robustez_varredura.py`.

**Ligaduras tipográficas.** Programas de diagramação representam os pares "fi" e "fl" por um
único caractere, ﬁ e ﬂ. Um procedimento que descarte caracteres fora do alfabeto básico parte
a palavra ao meio: "grá**ﬁ**cas" torna-se "grá cas" e deixa de ser encontrada. O corpus contém
1.171 ligaduras, distribuídas por 65 arquivos. A normalização adotada expande essas
ligaduras, de modo que a grafia com caractere único e a grafia com dois caracteres sejam
tratadas como a mesma palavra.

**Acentuação.** A redução do texto a caracteres sem acento é necessária para que "território"
e "territorio" constituam a mesma busca, mas precisa preservar a integridade da palavra.
Executada de modo tosco — substituindo cada letra acentuada por um espaço —, torna invisível
boa parte do vocabulário: "licitação" passa a "licita o" e deixa de ser encontrada.

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

**Dois arquivos não possuem camada de texto** e nenhuma busca os alcança
([`dados/lacunas_cobertura.csv`](dados/lacunas_cobertura.csv)). Um deles, `Resoluo23`, é
captura da Resolução nº 23, cujo conteúdo consta de outra captura, `res23`; nenhuma
resolução fica, portanto, fora do alcance da busca. O outro, `Fluxo_CIN_V7`, não tem
conteúdo nem autoria verificáveis.

**Três capturas são páginas inteiras do Diário Oficial.** Contêm as resoluções nº 1, 15 e
16 ao lado de atos de outros órgãos publicados na mesma página. Ocorrências nesses arquivos
podem pertencer a esses outros atos; por isso eles ficam fora das contagens da CEFIC, sem
perda, pois as três resoluções constam de capturas próprias. Na contagem do corpus inteiro,
permanecem.

**A busca é lexical.** Encontra o termo, não a ideia expressa por outras palavras. O nível
ampliado mitiga o problema sem eliminá-lo.

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
arquivos, documentos, páginas, linhas, ligaduras, documentos da CEFIC, resoluções, reuniões,
cópias descartadas, famílias sem ocorrência no nível ampliado, arquivos sem camada de texto e
total de termos ausentes —, falhando se algum divergir. Confere também a correspondência
entre o inventário e os arquivos do corpus, a coerência entre o inventário de documentos e o
de reuniões, a inexistência de cópias idênticas no corpus, a declaração de todo arquivo com
caractere não decodificado e a descrição, no dicionário de dados, de toda tabela e coluna
publicada. A verificação é executada a cada alteração enviada ao repositório.
