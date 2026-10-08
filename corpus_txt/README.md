# Corpus em texto

Os 105 documentos do corpus, em texto extraído dos PDFs de origem, um arquivo por documento.
Os marcadores `===== [pag N] =====` assinalam o início de cada página do PDF de origem, o que
permite a citação por documento e página. A categoria e o órgão emissor de cada documento
estão em [`../dados/inventario_documentos.csv`](../dados/inventario_documentos.csv).

A coleta reuniu 154 PDFs. Vinte e quatro eram cópias byte-idênticas de outros
([`../dados/copias_identicas.csv`](../dados/copias_identicas.csv)), e 25 eram capturas
adicionais de documentos já presentes, preteridas pela regra descrita em
[`../METODOLOGIA.md`](../METODOLOGIA.md) e registradas em
[`../dados/capturas_preteridas.csv`](../dados/capturas_preteridas.csv).

Um documento não possui camada de texto no PDF e consta aqui sem conteúdo pesquisável:
`Fluxo_CIN_V7`. Ver [`../dados/lacunas_cobertura.csv`](../dados/lacunas_cobertura.csv).

Os PDFs originais não são redistribuídos;
[`../dados/sha256_pdfs.csv`](../dados/sha256_pdfs.csv) traz o hash SHA-256 do PDF de que cada
texto foi extraído, para conferência contra a fonte oficial.
