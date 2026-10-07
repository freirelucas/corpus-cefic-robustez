# Corpus em texto

Os 129 documentos distintos do corpus, convertidos de PDF para texto. Um arquivo por
documento. Os marcadores `===== [pag N] =====` indicam onde começa cada página do PDF de
origem, o que permite citar arquivo e página.

A coleta reuniu 154 arquivos; 25 eram cópias exatas de outros e foram
removidas, com registro em [`../dados/duplicatas_removidas.csv`](../dados/duplicatas_removidas.csv).

Composição: 109 atos e registros da própria CEFIC e 20 documentos de contexto de
outros órgãos. A origem, o hash e o tipo documental de cada arquivo estão em
[`../dados/proveniencia.csv`](../dados/proveniencia.csv).

Dois documentos não possuem camada de texto no PDF e aparecem aqui sem conteúdo
pesquisável — `Fluxo_CIN_V7` e `Resoluo23` (Resolução nº 23). Ver
[`../dados/lacunas_cobertura.csv`](../dados/lacunas_cobertura.csv).

Os PDFs originais não são redistribuídos; [`../dados/sha256_pdfs.csv`](../dados/sha256_pdfs.csv)
traz o hash SHA-256 de cada um para conferência contra a fonte oficial.
