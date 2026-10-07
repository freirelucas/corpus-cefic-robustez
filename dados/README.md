# Dados

Tabelas de resultado, proveniência e verificação do corpus de 130 documentos.

O significado de cada coluna está em [DICIONARIO_DE_DADOS.md](../DICIONARIO_DE_DADOS.md).

| arquivo | o que contém | linhas |
|---|---|---|
| [`robustez_termos_cefic.csv`](robustez_termos_cefic.csv) | Comparação, por família de termos, entre a varredura anterior e a varredura sobre o corpus deduplicado, nos níveis estrito e ampliado. | 30 |
| [`freq_termos_robusto.csv`](freq_termos_robusto.csv) | Contagens por família nos dois níveis de busca, sobre o corpus canônico. | 30 |
| [`freq_termos_varredura_anterior.csv`](freq_termos_varredura_anterior.csv) | Contagens da varredura anterior, preservadas para comparação. | 29 |
| [`kwic_cefic_corrigido.csv`](kwic_cefic_corrigido.csv) | Uma linha por ocorrência encontrada no nível estrito, com arquivo, página e contexto. | 201 |
| [`kwic_cefic_ampliado.csv`](kwic_cefic_ampliado.csv) | Uma linha por ocorrência encontrada no nível ampliado. | 881 |
| [`termos_buscados_conferencia.csv`](termos_buscados_conferencia.csv) | Os termos de busca em forma literal, com o resultado de cada um, para conferência manual. | 100 |
| [`sonda_vocabulario_nativo.csv`](sonda_vocabulario_nativo.csv) | Termos usados pelos próprios documentos que o recorte original não cobria. | 21 |
| [`proveniencia.csv`](proveniencia.csv) | Origem, hash, tipo documental e data de coleta de cada documento do corpus. | 130 |
| [`integridade_texto.csv`](integridade_texto.csv) | Verificação da correspondência entre cada texto e seu PDF de origem. | 130 |
| [`lacunas_cobertura.csv`](lacunas_cobertura.csv) | Documentos sem camada de texto, inalcançáveis por qualquer busca. | 2 |
| [`duplicatas_removidas.csv`](duplicatas_removidas.csv) | Cópias byte-idênticas descartadas do corpus, com o arquivo canônico correspondente. | 24 |
| [`sha256_pdfs.csv`](sha256_pdfs.csv) | Hash SHA-256 de cada PDF de origem. | 130 |
| [`mapa_arquivos.csv`](mapa_arquivos.csv) | Correspondência entre nomes encurtados e nomes originais. | 6 |
| [`inventario_resolucoes.csv`](inventario_resolucoes.csv) | Inventário das resoluções identificadas no corpus. | 52 |
| [`inventario_atas.csv`](inventario_atas.csv) | Inventário dos registros de reunião identificados no corpus. | 39 |

`numeros_verificados.json` guarda os números-âncora conferidos pelo teste automatizado.
