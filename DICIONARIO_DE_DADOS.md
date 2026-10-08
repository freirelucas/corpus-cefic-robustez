# Dicionário de dados

Significado de cada tabela publicada em `dados/` e de cada uma de suas colunas.
Gerado por `reproduzir.py` a partir de `datapackage.json`.

## `resultados_por_familia.csv`

Resultado por família de termos nos dois níveis de busca, contado por ocorrência, por arquivo e por documento, com a situação de cada família. Gerado por reproduzir.py.

30 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) |
| `estrito_ocorrencias` | inteiro | Ocorrências no nível estrito |
| `estrito_arquivos` | inteiro | Arquivos distintos com ocorrência no nível estrito |
| `estrito_documentos` | inteiro | Documentos distintos com ocorrência no nível estrito, agregando capturas do mesmo documento |
| `estrito_documentos_cefic` | inteiro | Documentos da CEFIC com ocorrência no nível estrito |
| `ampliado_ocorrencias` | inteiro | Ocorrências no nível ampliado, com sinônimos e variantes |
| `ampliado_arquivos` | inteiro | Arquivos distintos com ocorrência no nível ampliado |
| `ampliado_documentos` | inteiro | Documentos distintos com ocorrência no nível ampliado |
| `sem_ocorrencia_no_recorte_declarado` | booleano | Família sem ocorrência no recorte de termos declarado na pesquisa |
| `situacao` | texto | Leitura do resultado: presente; ausência robusta a sinônimos e variantes; ou sintagma ausente com termos vizinhos em ocorrências marginais |

## `kwic_estrito.csv`

Uma linha por ocorrência encontrada no nível estrito, com arquivo, página e contexto.

183 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `pagina` | inteiro | Página do documento em que a ocorrência aparece |
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `trecho` | texto | Janela de contexto ao redor da ocorrência, no texto original acentuado |

## `kwic_ampliado.csv`

Uma linha por ocorrência encontrada no nível ampliado.

812 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `familia` | texto | Família de termos (conceito) a que a ocorrência pertence |
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `pagina` | inteiro | Página do documento em que a ocorrência aparece |
| `termo` | texto | Trecho exato do documento que casou com o padrão de busca |
| `trecho` | texto | Janela de contexto ao redor da ocorrência, no texto original acentuado |

## `termos_buscados_conferencia.csv`

Os termos de busca em forma literal, com o resultado de cada um.

100 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `conceito` | texto | Família de termos a que a expressão pertence |
| `termo` | texto | Expressão buscada, na forma literal |
| `situacao` | texto | presente ou ausente no corpus |
| `ocorrencias` | inteiro | Número de ocorrências no corpus |
| `documentos` | inteiro | Número de arquivos distintos em que o termo ocorre |
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
| `ocorrencias` | inteiro | Ocorrências no nível estrito |
| `ocorrencias_lexico_ampliado` | inteiro | Ocorrências sob o léxico ampliado, com sinônimos |
| `documentos` | inteiro | Número de arquivos distintos com ocorrência no nível estrito |
| `resultado` | texto | Se o item ocorre no corpus e, quando necessário, em que forma |
| `onde_conferir` | texto | Arquivo em que a evidência pode ser inspecionada |

## `sonda_vocabulario_nativo.csv`

Termos empregados pelos próprios documentos que o recorte declarado não cobre, com contagens no corpus e nos atos da CEFIC.

22 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `termo` | texto | Termo do vocabulário dos documentos, fora do recorte declarado |
| `padrao` | texto | Expressão regular aplicada ao texto normalizado, ancorada no início da palavra |
| `ocorrencias` | inteiro | Ocorrências no corpus inteiro |
| `arquivos` | inteiro | Arquivos distintos com ocorrência |
| `documentos` | inteiro | Documentos distintos com ocorrência, agregando capturas do mesmo documento |
| `ocorrencias_cefic` | inteiro | Ocorrências em arquivos cujo órgão emissor é a CEFIC |
| `documentos_cefic` | inteiro | Documentos da CEFIC com ocorrência |

## `proveniencia.csv`

Origem, hash e data de coleta do PDF de que cada texto do corpus foi extraído.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `arquivo_origem` | texto | Nome do arquivo PDF de origem |
| `sha256` | texto | Hash SHA-256 do PDF de que o texto foi extraído |
| `bytes` | inteiro | Tamanho do PDF em bytes |
| `data_coleta` | texto | Data da coleta, em ISO 8601 |
| `fonte` | texto | Origem declarada do documento |

## `integridade_texto.csv`

Correspondência entre cada texto e o PDF de origem.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha256_pdf` | texto | Hash SHA-256 do PDF de origem correspondente ao texto |
| `texto_presente` | booleano | Indica se há arquivo de texto correspondente |
| `chars_uteis` | inteiro | Número de caracteres não brancos no texto extraído |
| `paginas` | inteiro | Número de páginas detectadas no texto extraído |
| `situacao` | texto | ok, ou a natureza do problema encontrado na extração do texto |

## `lacunas_cobertura.csv`

Arquivos sem camada de texto, inalcançáveis por qualquer busca.

2 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `chars_uteis` | inteiro | Número de caracteres não brancos no texto extraído |
| `problema` | texto | Natureza da lacuna identificada no documento |
| `observacao` | texto | Consequência da lacuna para a busca |

## `copias_identicas.csv`

PDFs byte-idênticos a outro PDF da coleta, descartados na constituição do corpus.

24 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `pdf_descartado` | texto | PDF descartado por ser cópia byte-idêntica de outro |
| `identico_a` | texto | PDF de conteúdo idêntico, mantido ou registrado em capturas_preteridas.csv |
| `sha256_pdf` | texto | Hash SHA-256 comum aos dois PDFs |

## `versoes_mesmo_documento.csv`

Arquivos que correspondem ao mesmo documento em capturas distintas; os conteúdos diferem e nenhum foi descartado. Gerado a partir de inventario_documentos.csv.

48 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `documento` | texto | Documento a que os arquivos do grupo correspondem, conforme inventario_documentos.csv |
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `chars` | inteiro | Número de caracteres do texto extraído |
| `caracteres_corrompidos` | inteiro | Número de caracteres que não puderam ser decodificados do PDF (U+FFFD) |

## `sha256_pdfs.csv`

Hash SHA-256 de cada PDF de origem.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha256` | texto | Hash SHA-256 do PDF de que o texto foi extraído |

## `mapa_arquivos.csv`

Correspondência entre nomes encurtados e nomes originais.

6 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo_repo` | texto | Nome do documento no repositório, sem extensão |
| `arquivo_original` | texto | Nome do arquivo tal como coletado, antes do encurtamento |

## `inventario_resolucoes.csv`

Uma linha por arquivo de resolução ou retificação da CEFIC, com número, datas e dados de publicação no Diário Oficial.

54 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `sha12` | texto | Primeiros 12 caracteres do hash SHA-256 do PDF |
| `paginas` | inteiro | Número de páginas do texto extraído |
| `bytes` | inteiro | Tamanho do PDF em bytes |
| `num` | texto | Número da resolução |
| `data_doc` | texto | Data do documento no formato DD/MM/AAAA |
| `sem_texto` | texto | "sim" quando o PDF não possui camada de texto |
| `minuta` | texto | "sim" quando a captura é versão de minuta |
| `dou` | texto | Data de publicação no Diário Oficial da União |
| `dou_edicao` | número | Número da edição do Diário Oficial da União |
| `dou_secao` | número | Seção do Diário Oficial da União |
| `dou_pagina` | número | Página do Diário Oficial da União |
| `ementa_raw` | texto | Ementa da norma, transcrita do documento |
| `signatario` | texto | Autoridade signatária da norma |

## `inventario_documentos.csv`

Classificação de cada arquivo do corpus: documento a que corresponde, categoria e órgão emissor. Base das contagens por documento e do recorte dos atos da CEFIC.

129 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `arquivo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `documento` | texto | Documento a que o arquivo corresponde; arquivos com o mesmo valor são capturas distintas do mesmo documento |
| `categoria` | texto | resolucao, retificacao, registro_reuniao, apresentacao_reuniao, relatorio_tecnico, anexo, portaria, legislacao, norma_tecnica, relatorio_outro_orgao ou sem_camada_de_texto |
| `orgao` | texto | Órgão emissor; CEFIC para atos e registros da própria Câmara; "página mista do DOU" para página integral do Diário Oficial que contém ato da CEFIC e atos de outros órgãos |
| `numero` | texto | Número do ato, quando houver |
| `data_documento` | texto | Data do documento, DD/MM/AAAA ou MM/AAAA, quando identificada |
| `observacao` | texto | Particularidade do arquivo relevante para a leitura das contagens |

## `inventario_reunioes.csv`

Uma linha por reunião da CEFIC com registro no corpus, com a ordem e o tipo tais como declarados no cabeçalho do registro.

40 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `data` | texto | Data da reunião, DD/MM/AAAA, conforme o cabeçalho do registro |
| `ordem_declarada` | texto | Ordem da reunião declarada no cabeçalho; vazio quando ausente |
| `tipo_declarado` | texto | ordinária ou extraordinária, conforme o cabeçalho; vazio quando ausente |
| `modalidade` | texto | Forma de realização declarada: presencial, videoconferência, virtual para votação ou deliberação por e-mail |
| `arquivos_registro` | texto | Arquivo(s) de ata ou memória da reunião, separados por ponto e vírgula |
| `arquivo_apresentacao` | texto | Arquivo de slides exibidos na reunião, quando houver |
| `observacao` | texto | Divergência entre cabeçalho, nome do arquivo e sequência das reuniões, quando houver |

## `capturas_preteridas.csv`

PDFs distintos que não deram origem a texto do corpus por existir outra captura do mesmo documento com extração íntegra.

1 linhas.

| coluna | tipo | descrição |
|---|---|---|
| `pdf_preterido` | texto | Nome do PDF preterido |
| `sha256_pdf` | texto | Hash SHA-256 do PDF preterido |
| `documento` | texto | Documento a que o PDF corresponde |
| `substituido_por` | texto | PDF de que o texto publicado foi extraído |
| `sha256_substituto` | texto | Hash SHA-256 do PDF adotado |
| `arquivo_repo` | texto | Nome do arquivo no repositório, sem extensão; corresponde a corpus_txt/<arquivo>.txt |
| `motivo` | texto | Razão da substituição |
