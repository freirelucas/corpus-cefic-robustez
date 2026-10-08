# Corpus em texto

Os 129 arquivos de texto do corpus, extraídos dos PDFs de origem, um arquivo por PDF. Os
marcadores `===== [pag N] =====` assinalam o início de cada página do PDF de origem, o que
permite a citação por arquivo e página.

Os 129 arquivos correspondem a 105 documentos: 24 documentos constam em duas capturas de
conteúdo distinto. A correspondência entre arquivo e documento, a categoria e o órgão emissor
de cada arquivo estão em [`../dados/inventario_documentos.csv`](../dados/inventario_documentos.csv).

A coleta reuniu 154 PDFs; 24 eram cópias byte-idênticas de outros e foram descartadas
([`../dados/copias_identicas.csv`](../dados/copias_identicas.csv)), e um foi preterido em favor
de outra captura do mesmo documento com extração íntegra
([`../dados/capturas_preteridas.csv`](../dados/capturas_preteridas.csv)).

Dois arquivos não possuem camada de texto no PDF e constam aqui sem conteúdo pesquisável:
`Fluxo_CIN_V7` e `Resoluo23`. O conteúdo da Resolução nº 23 consta de `res23`, outra captura do
mesmo ato. Ver [`../dados/lacunas_cobertura.csv`](../dados/lacunas_cobertura.csv).

Os PDFs originais não são redistribuídos;
[`../dados/sha256_pdfs.csv`](../dados/sha256_pdfs.csv) traz o hash SHA-256 do PDF de que cada
texto foi extraído, para conferência contra a fonte oficial.
