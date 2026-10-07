# Corpus CEFIC — dados, código e teste de robustez da análise documental

Material de verificação do artigo **"Identidade digital e desenvolvimento tecnológico:
o papel da Cefic"** (Radar / Ipea). Contém o corpus em texto, o código da varredura de
termos e os resultados do teste de robustez que sustenta as afirmações de **ausência**
feitas no artigo.

A Câmara Executiva Federal de Identificação do Cidadão (CEFIC) foi criada pelo Decreto
nº 10.900/2021 e mantida pelo Decreto nº 11.797/2023.

## Por que este repositório existe

Parte das conclusões do artigo repousa sobre a *não ocorrência* de certos termos no
corpus — dizer que a CEFIC não tratou de transferência de tecnologia, conteúdo local ou
encomenda tecnológica é uma afirmação forte. Um zero de busca, porém, pode medir o
corpus ou pode medir o método: basta uma normalização de texto malfeita, uma janela de
busca estreita ou uma lista de termos curta para produzir ausência artificial. Este
repositório publica o procedimento inteiro para que o leitor possa distinguir os dois
casos por conta própria.

## Corpus

| Item | Valor |
|---|---|
| Documentos (PDF → texto) | 154 |
| Hashes SHA-256 distintos | 130 |
| Páginas | 805 |
| Linhas de texto | 32.170 |
| Resoluções (números distintos) | 33 — série 1 a 33, sem lacuna |
| Corte do levantamento | 15/09/2026 |

Os PDFs originais não são redistribuídos aqui; `dados/sha256_pdfs.csv` traz o hash
SHA-256 de cada um, o que permite conferir que o texto publicado em `corpus_txt/`
corresponde ao documento oficial de origem. Os textos são atos normativos e documentos
administrativos públicos.

## Método

A varredura percorre cada documento procurando famílias de termos — conjuntos de padrões
que representam um mesmo conceito — e registra cada ocorrência em formato **KWIC**
(*key word in context*): família, arquivo, página e o trecho de texto ao redor. Toda
afirmação do artigo baseada no corpus pode ser rastreada até uma linha desses arquivos e,
daí, até a página do PDF.

### Normalização

O texto extraído do PDF passa por uma normalização que remove diacríticos, uniformiza a
caixa e converte pontuação em espaço. Três cuidados são decisivos e estão implementados
em `robustez_varredura.py`:

1. **Ligaduras tipográficas.** PDFs representam "fi" e "fl" como caractere único
   (U+FB01, U+FB02). Uma normalização que descarte caracteres não-ASCII parte a palavra
   ao meio: "grá**ﬁ**cas" vira "grá cas" e deixa de ser encontrada. Há 1.260 ligaduras em
   72 dos 154 documentos. A normalização aqui expande essas ligaduras (NFKD).
2. **Hifenização de quebra de linha.** "inte-\ninteroperabilidade" é costurado antes da
   busca.
3. **Janela de busca.** A varredura corre sobre o documento inteiro, não página a página,
   de modo que expressões que atravessam a quebra de página sejam encontradas. A página
   é recuperada depois, pelo deslocamento da ocorrência.

A normalização preserva um mapa de posições de volta ao texto original, de forma que o
trecho KWIC exibido é o texto real, acentuado, e não a versão achatada usada na busca.

### Léxico em dois níveis

Cada família é buscada duas vezes. O nível **estrito** contém o sintagma tal como
definido no desenho da pesquisa. O nível **ampliado** acrescenta variantes morfológicas,
sinônimos e termos vizinhos — por exemplo, a família `aprisionamento_lockin` admite
"lock-in", "vendor lock", "dependência de fornecedor", "fornecedor único",
"exclusividade" e "monopólio". O objetivo do nível ampliado não é inflar contagens: é
testar se um zero resiste a um recorte lexical deliberadamente mais generoso.

## Resultado do teste de robustez

`dados/robustez_termos_cefic.csv` traz, para cada família, a contagem original, a
contagem estrita corrigida, a contagem ampliada e um veredito.

- **11 das 14 famílias com contagem zero continuam em zero** mesmo com a normalização
  corrigida e o léxico ampliado: padrão aberto, substituição de fornecedor,
  desenvolvimento nacional, Nova Indústria Brasil, margem de preferência, conteúdo local,
  encomenda tecnológica, software livre e código aberto, código-fonte, transferência de
  tecnologia e aprisionamento/*lock-in*. A ausência é propriedade do corpus, não do
  método.
- **3 famílias saem do zero apenas por termos vizinhos marginais**, que não sustentam a
  presença do conceito: uma "patente" em relatório de visita técnica a gráfica, menção a
  direitos de patente em norma ABNT do corpus de contexto, e a razão social "Empresa
  Brasileira" em documento de outro órgão.
- **Duas famílias que não eram zero estavam subcontadas** pela varredura original, por
  efeito das ligaduras: `graficas` passa de 51 para 72 ocorrências (de 24 para 35
  documentos). Das 21 ocorrências recuperadas, **20 estão em resoluções** e 1 na memória
  de reunião de 09/12/2025.

### Limites conhecidos

- **4 documentos não têm camada de texto** e nenhuma busca os alcança: três cópias de
  `Fluxo_CIN_V7` e a **Resolução nº 23**, que entra no corpus sem conteúdo pesquisável.
  Estão listados em `dados/lacunas_cobertura.csv`. Reconhecê-los é condição para que a
  afirmação de ausência valha sobre os demais 150.
- A busca é lexical. Ela encontra o termo, não a ideia expressa por outras palavras —
  daí o nível ampliado, que mitiga mas não elimina o problema.
- O número de **atas** depende do critério de deduplicação adotado (arquivos, hashes
  distintos ou datas de reunião distintas) e não é unívoco nos inventários; o número de
  **resoluções** é firme em 33.

## Como reproduzir

```bash
python reproduzir.py
```

Sem dependências além da biblioteca padrão do Python (3.10+). O script relê
`corpus_txt/`, refaz a varredura nos dois níveis e reescreve os CSVs de `dados/`.
`varredura_original_referencia.py` é o script da primeira varredura, mantido para que a
diferença entre os dois procedimentos possa ser inspecionada.

## Estrutura

```
corpus_txt/                       154 documentos em texto, um por PDF
robustez_varredura.py             normalização, léxico e varredura
varredura_original_referencia.py  procedimento anterior, para comparação
reproduzir.py                     regenera os resultados
dados/
  robustez_termos_cefic.csv       tabela do teste: original × estrito × ampliado
  kwic_cefic_corrigido.csv        KWIC do nível estrito
  kwic_cefic_ampliado.csv         KWIC do nível ampliado
  lacunas_cobertura.csv           documentos sem camada de texto
  sha256_pdfs.csv                 hash de cada PDF de origem
  numeros_verificados.json        números-âncora do corpus
  inventario_*.csv                inventários por tipo documental
```

## Diagnóstico do vocabulário

`dados/diagnostico_vocabulario.md` examina se o léxico está alinhado ao objetivo da
análise e registra quatro ressalvas: a assimetria formal entre as dimensões (sintagmas de
três palavras de um lado, palavras isoladas do outro); a presença de 22 documentos que não
são atos da CEFIC no denominador; a ausência, no léxico, de termos nativos do corpus — em
especial **credenciamento**, que ocorre 108 vezes em 30 documentos da CEFIC e é o
instrumento pelo qual a Câmara regula a entrada de operadores; e a mistura de níveis de
abstração entre as famílias. `dados/sonda_vocabulario_nativo.csv` lista os termos nativos
não cobertos.

## Conferência manual

`dados/termos_buscados_conferencia.md` traz os 100 termos em forma literal, sem expressão
regular, para quem quiser conferir com Ctrl+F no PDF. Ative "Palavras inteiras": sem isso,
`NIB` casa dentro de *disponibilidade*, `ETEC` dentro de *detecção* e `cativo` dentro de
*aplicativo*. Dos 100 termos, 97 não ocorrem em nenhum documento.

## Nomes de arquivo

Seis arquivos de nome muito longo foram encurtados para que o repositório funcione em
Windows sem configuração adicional. `dados/mapa_arquivos.csv` dá a correspondência entre o
nome no repositório e o nome original.

## Licença

Código sob licença MIT. Dados e textos derivados de documentos oficiais, sob
CC BY 4.0. Ver `LICENSE`.
