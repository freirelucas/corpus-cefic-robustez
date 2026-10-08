# Dados

Tabelas de resultado, inventário, proveniência e verificação do corpus.

O significado de cada coluna consta de [DICIONARIO_DE_DADOS.md](../DICIONARIO_DE_DADOS.md).

| arquivo | conteúdo | linhas |
|---|---|---|
| [`resultados_por_familia.csv`](resultados_por_familia.csv) | Resultado por família de termos nos dois níveis de busca, no corpus do artigo (73 documentos) e no corpus completo (105). Gerado por reproduzir.py. | 30 |
| [`kwic_estrito.csv`](kwic_estrito.csv) | Uma linha por ocorrência encontrada no nível estrito, com arquivo, página e contexto. | 145 |
| [`kwic_ampliado.csv`](kwic_ampliado.csv) | Uma linha por ocorrência encontrada no nível ampliado. | 716 |
| [`termos_buscados_conferencia.csv`](termos_buscados_conferencia.csv) | As 100 expressões das 14 famílias sem ocorrência no recorte declarado, em forma literal, com o resultado de cada uma. As contagens são geradas por reproduzir.py. | 100 |
| [`fundamentacao_do_quadro.csv`](fundamentacao_do_quadro.csv) | Liga cada item do quadro de dimensões analíticas do artigo aos termos buscados e ao resultado obtido. | 9 |
| [`sonda_vocabulario_nativo.csv`](sonda_vocabulario_nativo.csv) | Termos empregados pelos próprios documentos que o recorte declarado não cobre, com contagens no corpus do artigo e no corpus completo. | 22 |
| [`proveniencia.csv`](proveniencia.csv) | Origem, hash e data de coleta do PDF de que cada texto do corpus foi extraído. | 105 |
| [`integridade_texto.csv`](integridade_texto.csv) | Correspondência entre cada texto e o PDF de origem. | 105 |
| [`lacunas_cobertura.csv`](lacunas_cobertura.csv) | Documentos sem camada de texto, inalcançáveis por qualquer busca. | 1 |
| [`copias_identicas.csv`](copias_identicas.csv) | PDFs byte-idênticos a outro PDF da coleta, descartados na constituição do corpus. | 24 |
| [`sha256_pdfs.csv`](sha256_pdfs.csv) | Hash SHA-256 de cada PDF de origem. | 105 |
| [`mapa_arquivos.csv`](mapa_arquivos.csv) | Correspondência entre nomes encurtados e nomes originais. | 5 |
| [`inventario_resolucoes.csv`](inventario_resolucoes.csv) | Uma linha por resolução ou retificação da CEFIC, com data, ementa, dados de publicação no Diário Oficial da União e signatário. | 35 |
| [`inventario_documentos.csv`](inventario_documentos.csv) | Classificação de cada documento do corpus: categoria e órgão emissor. Base do recorte dos atos da CEFIC. | 105 |
| [`inventario_reunioes.csv`](inventario_reunioes.csv) | Uma linha por reunião da CEFIC com registro no corpus, com a ordem e o tipo tais como declarados no cabeçalho do registro. | 40 |
| [`capturas_preteridas.csv`](capturas_preteridas.csv) | PDFs distintos de documentos que constavam em mais de uma captura; de cada documento mantém-se uma única captura, e as demais são registradas aqui com o motivo. | 25 |

`numeros_verificados.json` guarda os números-âncora conferidos por `teste_reproducao.py`.
