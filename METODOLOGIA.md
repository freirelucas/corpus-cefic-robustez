# Metodologia

Documento complementar ao [README](README.md). Descreve o percurso do corpus, os cuidados
técnicos que o procedimento exige e o que ele não alcança.

## Procedimento de busca

O artigo analisa duas dimensões: concorrência e contestabilidade, e capacidades tecnológicas
nacionais. Para cada uma, o procedimento parte de uma lista de termos agrupados em famílias —
conjuntos de expressões que designam um mesmo conceito. "Transferência de tecnologia",
"transferência tecnológica" e "absorção tecnológica" pertencem à mesma família.

Cada documento é convertido em texto e percorrido integralmente em busca dessas expressões.
Toda ocorrência encontrada é registrada com **arquivo e página**, acompanhada do trecho de
texto ao redor — o formato que a linguística de corpus denomina KWIC, *key word in context*.
Daí decorre que cada afirmação do artigo baseada no corpus possa ser rastreada até uma linha
de [`dados/kwic_estrito.csv`](dados/kwic_estrito.csv) e, dali, até a página do documento.

As buscas são feitas em dois níveis. O nível **estrito** procura o conceito tal como definido
no desenho da pesquisa. O nível **ampliado** acrescenta variantes, sinônimos e termos
vizinhos: para a família de aprisionamento tecnológico, admite "lock-in", "vendor lock",
"dependência de fornecedor", "fornecedor único", "exclusividade" e "monopólio". O nível
ampliado não serve para elevar contagens, e sim para testar se uma ausência resiste a critério
deliberadamente mais generoso.

## Cuidados que condicionam o resultado

Documentos em PDF impõem três dificuldades à busca textual, tratadas em
`robustez_varredura.py`.

**Ligaduras tipográficas.** Programas de diagramação representam os pares "fi" e "fl" por um
único caractere, ﬁ e ﬂ. Um procedimento que descarte caracteres fora do alfabeto básico parte
a palavra ao meio: "grá**ﬁ**cas" torna-se "grá cas" e deixa de ser encontrada. O corpus contém
1.260 ligaduras, distribuídas por 72 documentos. A normalização adotada expande essas
ligaduras, de modo que a grafia com caractere único e a grafia com dois caracteres sejam
tratadas como a mesma palavra.

**Acentuação.** A redução do texto a caracteres sem acento é necessária para que "território"
e "territorio" constituam a mesma busca, mas precisa preservar a integridade da palavra.
Executada de modo tosco, torna invisível boa parte do vocabulário: uma busca literal por
"identificação" ou "resolução" não retornaria resultado algum.

**Hifenização e quebra de página.** Palavras partidas no fim da linha são costuradas antes da
busca, e a varredura percorre o documento inteiro em lugar de página a página, para que
expressões que atravessem a quebra sejam encontradas. A página é recuperada em seguida, pela
posição da ocorrência.

A normalização preserva um mapa de posições de volta ao texto original, de maneira que o
trecho KWIC exibido seja o texto real, acentuado, e não a forma achatada usada na comparação.

## Limitações declaradas

**Dois documentos não possuem camada de texto** e nenhuma busca os alcança: `Fluxo_CIN_V7` e,
com maior relevância, a **Resolução nº 23**, que integra o corpus sem conteúdo pesquisável.
Qualquer afirmação de ausência vale para os demais 127 documentos. Ver
[`dados/lacunas_cobertura.csv`](dados/lacunas_cobertura.csv).

**A busca é lexical.** Encontra o termo, não a ideia expressa por outras palavras. O nível
ampliado mitiga o problema sem eliminá-lo.

**O vocabulário provém da literatura, não do corpus.** Termos que os próprios documentos
empregam ficaram fora do recorte declarado — entre eles credenciamento, contrato, auditoria,
dispensa, certificação, homologação e capacidade técnica.
[`dados/sonda_vocabulario_nativo.csv`](dados/sonda_vocabulario_nativo.csv) lista os termos
nativos não cobertos, e [PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md) registra
os de maior frequência. Um recorte construído a partir do vocabulário dos documentos
produziria um conjunto distinto de resultados.

**As famílias não têm forma comparável entre as dimensões.** Os termos da dimensão de
capacidades tecnológicas são expressões de três palavras — "margem de preferência", "encomenda
tecnológica"; os da outra dimensão são palavras isoladas — "interoperabilidade", "soberania".
Expressões longas têm probabilidade de ocorrência literal menor que palavras únicas, qualquer
que seja o corpus. Parte do contraste entre as duas dimensões decorre dessa assimetria, e não
apenas do conteúdo dos documentos.

**O número de atas não é unívoco.** Conforme o critério de deduplicação, obtêm-se números
distintos. A série de resoluções, ao contrário, está confirmada em 33 unidades, numeradas de 1
a 33 sem lacuna. [`dados/inventario_atas.csv`](dados/inventario_atas.csv) traz o inventário
para a aplicação de critério próprio.

## Verificação

`teste_reproducao.py` refaz a varredura sobre o corpus e confere os números declarados —
documentos, páginas, linhas, famílias sem ocorrência no nível ampliado, documentos sem camada
de texto e total de termos ausentes —, falhando se algum divergir. Confere também a
inexistência de cópias idênticas no corpus, a declaração de todo documento com caractere não
decodificado e a descrição, no dicionário de dados, de toda coluna publicada. A verificação é
executada a cada alteração enviada ao repositório.
