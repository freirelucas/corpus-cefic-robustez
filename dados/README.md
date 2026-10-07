# Dados

Tabelas de resultado, proveniência e verificação do corpus de 129 documentos.

O significado de cada coluna consta de [DICIONARIO_DE_DADOS.md](../DICIONARIO_DE_DADOS.md).

| arquivo | conteúdo | linhas |
|---|---|---|
| [`resultados_por_familia.csv`](resultados_por_familia.csv) | Resultado por família de termos nos dois níveis de busca, com a situação de cada uma. | 30 |
| [`contagens_por_familia.csv`](contagens_por_familia.csv) | Contagens por família nos níveis estrito e ampliado. | 30 |
| [`kwic_estrito.csv`](kwic_estrito.csv) | Uma linha por ocorrência encontrada no nível estrito, com arquivo, página e contexto. | 183 |
| [`kwic_ampliado.csv`](kwic_ampliado.csv) | Uma linha por ocorrência encontrada no nível ampliado. | 812 |
| [`termos_buscados_conferencia.csv`](termos_buscados_conferencia.csv) | Os termos de busca em forma literal, com o resultado de cada um. | 100 |
| [`fundamentacao_do_quadro.csv`](fundamentacao_do_quadro.csv) | Liga cada item do quadro de dimensões analíticas do artigo aos termos buscados e ao resultado obtido. | 9 |
| [`sonda_vocabulario_nativo.csv`](sonda_vocabulario_nativo.csv) | Termos empregados pelos próprios documentos que o recorte declarado não cobria. | 21 |
| [`proveniencia.csv`](proveniencia.csv) | Origem, hash, tipo documental e data de coleta de cada documento do corpus. | 129 |
| [`integridade_texto.csv`](integridade_texto.csv) | Correspondência entre cada texto e o PDF de origem. | 129 |
| [`lacunas_cobertura.csv`](lacunas_cobertura.csv) | Documentos sem camada de texto, inalcançáveis por qualquer busca. | 2 |
| [`copias_identicas.csv`](copias_identicas.csv) | Cópias byte-idênticas descartadas na constituição do corpus, com o arquivo canônico correspondente. | 24 |
| [`versoes_mesmo_documento.csv`](versoes_mesmo_documento.csv) | Grupos de arquivos correspondentes ao mesmo documento em capturas distintas; os conteúdos diferem e nenhum foi descartado. | 18 |
| [`sha256_pdfs.csv`](sha256_pdfs.csv) | Hash SHA-256 de cada PDF de origem. | 129 |
| [`mapa_arquivos.csv`](mapa_arquivos.csv) | Correspondência entre nomes encurtados e nomes originais. | 6 |
| [`inventario_resolucoes.csv`](inventario_resolucoes.csv) | Inventário das resoluções identificadas no corpus. | 52 |
| [`inventario_atas.csv`](inventario_atas.csv) | Inventário dos registros de reunião identificados no corpus. | 38 |

`numeros_verificados.json` guarda os números-âncora conferidos pelo teste automatizado.
