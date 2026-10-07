# Metodologia

Documento complementar ao [README](README.md). Descreve como o corpus foi percorrido, que
cuidados técnicos o procedimento exige e o que ele não alcança.

---

## O que foi buscado, e como

O artigo analisa duas dimensões: **concorrência** e **capacidades tecnológicas nacionais**.
Para cada uma, o procedimento parte de uma lista de termos agrupados em famílias — conjuntos
de expressões que designam um mesmo conceito. "Transferência de tecnologia", "transferência
tecnológica" e "absorção tecnológica", por exemplo, pertencem à mesma família.

Cada documento foi convertido em texto e percorrido integralmente em busca dessas
expressões. Toda ocorrência encontrada foi registrada com **arquivo e página**, acompanhada
do trecho de texto ao redor — o formato que a linguística de corpus chama de KWIC
(*key word in context*, palavra-chave em contexto). É por isso que cada afirmação do artigo
baseada no corpus pode ser rastreada até uma linha de `dados/kwic_cefic_corrigido.csv` e,
dali, até a página do documento original.

As buscas foram feitas em dois níveis. O nível **estrito** procura o conceito tal como
definido no desenho da pesquisa. O nível **ampliado** acrescenta variantes, sinônimos e
termos vizinhos — para a família de aprisionamento tecnológico, por exemplo, admite
"lock-in", "vendor lock", "dependência de fornecedor", "fornecedor único", "exclusividade"
e "monopólio". O nível ampliado não serve para inflar contagens: serve para testar se uma
ausência resiste a um critério deliberadamente mais generoso.

---

---

## Três cuidados que mudam o resultado

Documentos em PDF guardam armadilhas para busca textual. Três foram tratadas, e vale
explicá-las porque cada uma já produziu erro de contagem neste corpus.

**Ligaduras tipográficas.** Programas de diagramação representam os pares "fi" e "fl" como
um único caractere (ﬁ, ﬂ). Um procedimento que descarte caracteres fora do alfabeto básico
parte a palavra ao meio: "grá**ﬁ**cas" vira "grá cas" e deixa de ser encontrada. Há 1.260
ligaduras neste corpus, distribuídas por 72 documentos. A varredura anterior deixava de
encontrar, por esse motivo, três ocorrências do termo "gráficas" em dois documentos.

**Acentuação.** Reduzir o texto a caracteres sem acento é necessário para que "território"
e "territorio" sejam a mesma busca, mas precisa ser feito preservando a palavra. Feito de
modo tosco, torna invisível boa parte do vocabulário: uma busca literal por "identificação"
ou "resolução" simplesmente não retornaria nada.

**Hifenização e quebra de página.** Palavras partidas no fim da linha são costuradas antes
da busca, e a varredura percorre o documento inteiro em vez de página a página, para que
expressões que atravessam a quebra sejam encontradas. A página é recuperada depois, pela
posição da ocorrência.

---

---

## Limitações declaradas

**Dois documentos não têm camada de texto** e nenhuma busca os alcança: `Fluxo_CIN_V7` e,
mais relevante, a **Resolução nº 23**, que entra no corpus sem conteúdo pesquisável.
Qualquer afirmação de ausência vale para os demais 127 documentos. Ver
`dados/lacunas_cobertura.csv`.

**A busca é lexical.** Encontra o termo, não a ideia expressa por outras palavras. O nível
ampliado mitiga o problema, não o elimina.

**O vocabulário foi construído a partir da literatura, não do corpus.** Termos que os
próprios documentos usam ficaram de fora do recorte original — o caso mais importante é
credenciamento, discutido na seção 6, mas também contrato (49), auditoria (40), dispensa (28), certificacao (14), homologacao (13), capacidade tecnica (3).
`dados/sonda_vocabulario_nativo.csv` lista os termos nativos não cobertos. Um recorte
construído a partir do vocabulário dos documentos produziria um mapa diferente, e
possivelmente mais rico, da dimensão concorrência.

**As famílias não têm forma comparável entre as duas dimensões.** Os termos da dimensão de
capacidades tecnológicas são expressões de três palavras ("margem de preferência",
"encomenda tecnológica"); os da outra dimensão são palavras isoladas ("interoperabilidade",
"soberania"). Expressões longas têm probabilidade de ocorrência literal menor que palavras
únicas, qualquer que seja o corpus. Parte do contraste entre as duas dimensões decorre
dessa assimetria e não apenas do conteúdo dos documentos.

**O número de atas não é unívoco.** Conforme o critério de deduplicação adotado, chega-se a
números diferentes. A série de resoluções, ao contrário, está confirmada em 33 unidades
numeradas de 1 a 33 sem lacuna. `dados/inventario_atas.csv` traz o inventário para quem
quiser aplicar o próprio critério.

---

---

## Verificação

O repositório traz verificação automatizada. `teste_reproducao.py` refaz a varredura sobre
o corpus e confere os números declarados — documentos, páginas, linhas, famílias ainda
zeradas no nível ampliado, documentos sem camada de texto e total de termos ausentes —,
falhando se algum divergir. Também confere que não restam duplicatas no corpus e que toda
coluna publicada tem descrição no dicionário de dados. A verificação roda a cada alteração
enviada ao repositório.
