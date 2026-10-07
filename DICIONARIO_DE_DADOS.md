# Dicionário de dados

Significado de cada tabela publicada em `dados/` e de cada uma de suas colunas.

## `resultados_por_familia.csv`

Resultado por família de termos nos dois níveis de busca, com a situação de cada uma.

30 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `estrito_total` | inteiro | Ocorrências no nível estrito de busca |
| `estrito_docs` | inteiro | Documentos distintos no nível estrito |
| `ampliado_total` | inteiro | Ocorrências no nível ampliado, com sinônimos e variantes |
| `ampliado_docs` | inteiro | Documentos distintos no nível ampliado |
| `no_recorte_declarado_sem_ocorrencia` | booleano | Indica que a família não registrou ocorrência no recorte de termos declarado na pesquisa |
| `situacao` | texto | Interpretação do resultado da família após o teste de robustez |

## `contagens_por_familia.csv`

Contagens por família nos níveis estrito e ampliado.

30 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `estrito_total` | inteiro | Ocorrências no nível estrito de busca |
| `estrito_docs` | inteiro | Documentos distintos no nível estrito |
| `ampliado_total` | inteiro | Ocorrências no nível ampliado, com sinônimos e variantes |
| `ampliado_docs` | inteiro | Documentos distintos no nível ampliado |
| `sem_ocorrencia_no_recorte_declarado` | booleano | Indica que a família não registrou ocorrência no recorte de termos declarado na pesquisa |

## `kwic_estrito.csv`

Uma linha por ocorrência encontrada no nível estrito, com arquivo, página e contexto.

183 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `pagina` | inteiro | Página do documento em que a ocorrência aparece |
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `trecho` | texto | Janela de contexto ao redor da ocorrência, no texto original acentuado |

## `kwic_ampliado.csv`

Uma linha por ocorrência encontrada no nível ampliado.

812 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `pagina` | inteiro | Página do documento em que a ocorrência aparece |
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `trecho` | texto | Janela de contexto ao redor da ocorrência, no texto original acentuado |

## `termos_buscados_conferencia.csv`

Os termos de busca em forma literal, com o resultado de cada um.

100 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `conceito` | texto | Nome legível da família de termos |
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `situacao` | texto | Interpretação do resultado da família após o teste de robustez |
| `ocorrencias` | inteiro | Número de ocorrências no corpus |
| `documentos` | inteiro | Número de documentos distintos em que o termo ocorre |
| `aviso` | texto | Observação sobre como conferir o termo manualmente |

## `fundamentacao_do_quadro.csv`

Liga cada item do quadro de dimensões analíticas do artigo aos termos buscados e ao resultado obtido.

9 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `dimensao` | texto | Dimensão analítica do artigo |
| `item_do_quadro` | texto | Item tal como declarado no quadro de dimensões |
| `termos_buscados` | texto | Termos literais efetivamente buscados |
| `n_termos` | inteiro | Quantidade de termos buscados para o item |
| `ocorrencias` | inteiro | Número de ocorrências no corpus |
| `ocorrencias_lexico_ampliado` | inteiro | Ocorrências sob o léxico ampliado, com sinônimos |
| `documentos` | inteiro | Número de documentos distintos em que o termo ocorre |
| `resultado` | texto | Se o item ocorre ou não no corpus |
| `onde_conferir` | texto | Arquivo em que a evidência pode ser inspecionada |

## `sonda_vocabulario_nativo.csv`

Termos empregados pelos próprios documentos que o recorte declarado não cobria.

21 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `ocorrencias` | inteiro | Número de ocorrências no corpus |
| `docs_cefic` | inteiro | Número de documentos da própria CEFIC em que o termo ocorre |

## `proveniencia.csv`

Origem, hash, tipo documental e data de coleta de cada documento do corpus.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do documento no repositório, sem extensão |
| `arquivo_origem` | texto | Nome do arquivo PDF de origem |
| `sha256` | texto | Hash SHA-256 do arquivo PDF de origem, em hexadecimal |
| `bytes` | inteiro | Tamanho do arquivo em bytes |
| `tipo_documental` | texto | Classificação do documento: resolucao, registro_reuniao, portaria, norma_externa ou contexto |
| `numero` | texto | Número da norma, quando aplicável |
| `data_documento` | texto | Data do documento no formato DD/MM/AAAA, quando identificada |
| `data_coleta` | texto | Data em que o arquivo foi coletado, em ISO 8601 |
| `fonte` | texto | Origem declarada do documento |

## `integridade_texto.csv`

Correspondência entre cada texto e o PDF de origem.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do documento no repositório, sem extensão |
| `sha256_pdf` | texto | Hash SHA-256 do PDF de origem correspondente ao texto |
| `texto_presente` | booleano | Indica se há arquivo de texto correspondente |
| `chars_uteis` | inteiro | Número de caracteres não brancos no texto extraído |
| `paginas` | inteiro | Número de páginas detectadas no texto extraído |
| `situacao` | texto | Interpretação do resultado da família após o teste de robustez |

## `lacunas_cobertura.csv`

Documentos sem camada de texto, inalcançáveis por qualquer busca.

2 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `chars_uteis` | inteiro | Número de caracteres não brancos no texto extraído |
| `problema` | texto | Natureza da lacuna identificada no documento |

## `copias_identicas.csv`

Cópias byte-idênticas descartadas na constituição do corpus, com o arquivo canônico correspondente.

24 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_removido` | texto | Nome do arquivo descartado por ser cópia byte-idêntica de outro |
| `identico_a` | texto | Arquivo canônico cujo conteúdo é idêntico ao removido |
| `sha256` | texto | Hash SHA-256 do arquivo PDF de origem, em hexadecimal |

## `versoes_mesmo_documento.csv`

Grupos de arquivos correspondentes ao mesmo documento em capturas distintas; os conteúdos diferem e nenhum foi descartado.

18 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `documento` | texto | Documento ao qual os arquivos do grupo correspondem |
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `chars` | inteiro | Número de caracteres do texto extraído |
| `caracteres_corrompidos` | inteiro | Número de caracteres que não puderam ser decodificados do PDF (U+FFFD) |

## `sha256_pdfs.csv`

Hash SHA-256 de cada PDF de origem.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha256` | texto | Hash SHA-256 do arquivo PDF de origem, em hexadecimal |

## `mapa_arquivos.csv`

Correspondência entre nomes encurtados e nomes originais.

6 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do documento no repositório, sem extensão |
| `arquivo_original` | texto | Nome do arquivo tal como coletado, antes do encurtamento |

## `inventario_resolucoes.csv`

Inventário das resoluções identificadas no corpus.

52 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha12` | texto | Primeiros 12 caracteres do hash SHA-256 do arquivo, usado como identificador curto |
| `paginas` | inteiro | Número de páginas detectadas no texto extraído |
| `bytes` | inteiro | Tamanho do arquivo em bytes |
| `num` | texto | Número da resolução |
| `data_doc` | texto | Data do documento no formato DD/MM/AAAA |
| `sem_texto` | texto | Marca os documentos cujo PDF não possui camada de texto |
| `minuta` | texto | Marca os documentos em versão de minuta, não publicada |
| `dou` | texto | Data de publicação no Diário Oficial da União |
| `dou_edicao` | número | Número da edição do Diário Oficial da União |
| `dou_secao` | número | Seção do Diário Oficial da União |
| `dou_pagina` | número | Página do Diário Oficial da União |
| `ementa_raw` | texto | Ementa da norma, transcrita do documento |
| `signatario` | texto | Autoridade signatária da norma |

## `inventario_atas.csv`

Inventário dos registros de reunião identificados no corpus.

38 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do documento no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha12` | texto | Primeiros 12 caracteres do hash SHA-256 do arquivo, usado como identificador curto |
| `paginas` | inteiro | Número de páginas detectadas no texto extraído |
| `bytes` | inteiro | Tamanho do arquivo em bytes |
| `ordinal` | número | Número ordinal da reunião no ano, quando identificado |
| `tipo` | texto | Natureza da reunião: ordinária ou extraordinária |
| `data_doc` | texto | Data do documento no formato DD/MM/AAAA |
| `ano` | número | Ano de referência da reunião |
