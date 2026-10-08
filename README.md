# Corpus CEFIC — dados, código e verificação da análise documental

Material de verificação do artigo **"Identidade digital e desenvolvimento tecnológico: o
papel da Cefic"** (Boletim Radar, Ipea). Reúne o corpus documental em texto, os inventários
dos documentos e das reuniões, a lista completa dos termos buscados, o código que produz os
resultados e o registro das limitações do procedimento.

O artigo conclui que a regulamentação da identificação biométrica federal incorpora
requisitos de concorrência, mas não instrumentos de desenvolvimento tecnológico nacional.
Essa segunda conclusão apoia-se em ausências. Das famílias de termos associadas às duas
dimensões do artigo, **14 não registram ocorrência no recorte declarado, e 11 delas
continuam sem ocorrência quando o léxico é ampliado com sinônimos e variantes**: nenhuma das
100 expressões que compõem essas 14 famílias ocorre no corpus, à exceção de três termos
vizinhos em ocorrências marginais. Este repositório publica o corpus e o procedimento para
que essas ausências — e as presenças — possam ser verificadas de forma independente.

A Câmara Executiva Federal de Identificação do Cidadão (CEFIC) foi criada pelo Decreto nº
10.900/2021 e mantida pelo Decreto nº 11.797/2023. A coleta dos documentos foi realizada em
14/09/2026.

## Busca no corpus

O arquivo **[`busca_corpus_cefic.html`](busca_corpus_cefic.html)** é uma ferramenta de busca
autocontida: um único arquivo HTML, com o corpus embutido, que funciona offline em qualquer
navegador, sem servidor, sem instalação e sem conexão. O download é feito pelo botão
*Download raw file* na página do arquivo; a abertura, por duplo clique. Cada ocorrência é
exibida com o documento, o arquivo, a página e o trecho em que consta.

A ferramenta traz atalhos para os termos cuja ausência sustenta conclusões do artigo —
*transferência de tecnologia*, *conteúdo local*, *encomenda tecnológica*, entre outros — e
para termos presentes, como *interoperabilidade* e *território nacional*, o que permite
comparar os dois casos. Um filtro restringe a busca aos atos e registros da própria CEFIC.

## Orientação

| objetivo | documento |
|---|---|
| buscar um termo no corpus | [`busca_corpus_cefic.html`](busca_corpus_cefic.html) |
| conferir em que se apoia cada item do quadro do artigo | [FUNDAMENTACAO_DO_QUADRO.md](FUNDAMENTACAO_DO_QUADRO.md) |
| examinar o procedimento de busca e seus limites | [METODOLOGIA.md](METODOLOGIA.md) |
| consultar os termos buscados, um a um | [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md) |
| localizar cada ocorrência com arquivo e página | [`dados/kwic_estrito.csv`](dados/kwic_estrito.csv) |
| saber a que documento corresponde cada arquivo | [`dados/inventario_documentos.csv`](dados/inventario_documentos.csv) |
| conferir as reuniões com registro | [`dados/inventario_reunioes.csv`](dados/inventario_reunioes.csv) |
| conferir as resoluções | [`dados/inventario_resolucoes.csv`](dados/inventario_resolucoes.csv) |
| interpretar as colunas das tabelas | [DICIONARIO_DE_DADOS.md](DICIONARIO_DE_DADOS.md) |
| ler os documentos em texto | [`corpus_txt/`](corpus_txt/) |
| consultar termos com ocorrência fora do recorte do artigo | [PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md) |
| rastrear a origem de cada arquivo | [`dados/proveniencia.csv`](dados/proveniencia.csv) |
| repetir a análise | a seção *Reprodução*, adiante |

## Por que este repositório existe

Um resultado de busca igual a zero admite duas leituras: o assunto não aparece nos
documentos, ou o procedimento de busca não era capaz de encontrá-lo. Uma lista de termos
curta, um tratamento inadequado da acentuação ou uma janela de busca estreita bastam para
produzir ausência artificial. O procedimento é publicado integralmente para que a distinção
entre as duas leituras seja verificável.

## O corpus

| | |
|---|---|
| PDFs coletados | 154 |
| Cópias byte-idênticas descartadas | 24 |
| Captura preterida por extração corrompida | 1 |
| **Arquivos de texto analisados** | **129** |
| **Documentos a que correspondem** | **105** |
| Páginas | 663 |
| Linhas de texto | 28.508 |
| Documentos da própria CEFIC | 82 |
| Documentos de outros órgãos ou de autoria não determinada | 23 |
| Resoluções da CEFIC, números distintos | 33 — série 1 a 33, sem lacuna |
| Reuniões da CEFIC com registro | 40 — de 14/03/2022 a 11/08/2026 |
| Coleta | 14/09/2026 |

**Arquivos e documentos.** A coleta reuniu 154 PDFs. Vinte e quatro eram cópias
byte-idênticas de outros e foram descartados, com registro em
[`dados/copias_identicas.csv`](dados/copias_identicas.csv). Um vigésimo quinto, versão do
registro da reunião de 10/06/2025 cuja extração de texto saiu corrompida, foi preterido em
favor de outra captura do mesmo documento, com registro em
[`dados/capturas_preteridas.csv`](dados/capturas_preteridas.csv). Restam 129 arquivos de
texto, todos de conteúdo distinto. Vários documentos, porém, constam em mais de uma captura —
a mesma resolução publicada no Diário Oficial e em arquivo próprio, ou a mesma memória de
reunião em duas versões —, de modo que os 129 arquivos correspondem a 105 documentos. Os 24
grupos de capturas do mesmo documento estão em
[`dados/versoes_mesmo_documento.csv`](dados/versoes_mesmo_documento.csv), e a
correspondência completa entre arquivo e documento, em
[`dados/inventario_documentos.csv`](dados/inventario_documentos.csv). As tabelas de
resultado trazem as contagens por arquivo e por documento.

**Documentos da CEFIC e de outros órgãos.** Dos 105 documentos, 82 são atos ou registros da
própria CEFIC: 33 resoluções, 2 retificações, os registros de 40 reuniões, os slides de 3
reuniões de 2022, 3 relatórios de visita técnica e 1 anexo do Modelo Informacional da CIN. Os
23 demais são leis e decretos (8), portarias de designação da SGD/MGI (12), a norma ABNT NBR
17225, um relatório de impacto à proteção de dados do Ministério da Economia e um arquivo sem
camada de texto de autoria não determinada. A distinção importa na leitura, pois afirmações
sobre o que a CEFIC enuncia referem-se ao primeiro conjunto. Três capturas são páginas
inteiras do Diário Oficial que contêm uma resolução da CEFIC ao lado de atos de outros
órgãos; ficam fora das contagens da CEFIC, pois as três resoluções constam de capturas
próprias.

**Reuniões.** O corpus contém registros — atas ou memórias — de 40 reuniões, ordinárias e
extraordinárias, realizadas entre 14/03/2022 e 11/08/2026, em 45 arquivos: cinco reuniões
têm duas versões do registro. Os cabeçalhos dos próprios registros nem sempre concordam
entre si quanto à ordem e ao tipo da reunião; [`dados/inventario_reunioes.csv`](dados/inventario_reunioes.csv)
traz uma linha por reunião, com a ordem e o tipo tais como declarados e as divergências
assinaladas.

Os PDFs originais não são redistribuídos. [`dados/sha256_pdfs.csv`](dados/sha256_pdfs.csv) traz
o hash SHA-256 do PDF de que cada texto foi extraído, o que permite confrontar o texto
publicado com o documento oficial de origem. Os textos são atos normativos e documentos
administrativos públicos.

## Resultados

Contagens no nível estrito de busca. Arquivos e documentos diferem quando o mesmo documento
consta em mais de uma captura. A tabela completa, com o nível ampliado, está em
[`dados/resultados_por_familia.csv`](dados/resultados_por_familia.csv).

### Famílias das duas dimensões analíticas do artigo

| família | ocorrências | arquivos | documentos | documentos da CEFIC | situação |
|---|---|---|---|---|---|
| Território nacional | 38 | 16 | 13 | 7 | presente |
| Interoperabilidade | 34 | 19 | 15 | 9 | presente |
| Preferência normativa | 12 | 10 | 7 | 5 | presente; família acrescentada ao léxico no teste de robustez |
| Multifornecedor / segundo motor | 3 | 3 | 2 | 2 | presente |
| Soberania | 3 | 2 | 2 | 1 | presente |
| Concorrência | 3 | 2 | 2 | 1 | presente |
| Capacitação tecnológica | 0 | 0 | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Propriedade intelectual | 0 | 0 | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Empresa/indústria nacional | 0 | 0 | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Aprisionamento / lock-in | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Conteúdo local | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Código-fonte | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Desenvolvimento nacional | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Encomenda tecnológica | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Margem de preferência | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Nova Indústria Brasil | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Padrão aberto | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Software livre / código aberto | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Substituição de fornecedor | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |
| Transferência de tecnologia | 0 | 0 | 0 | 0 | ausência robusta a sinônimos e variantes |

### Termos que sustentam afirmações do texto fora do quadro

| família | ocorrências | arquivos | documentos | documentos da CEFIC |
|---|---|---|---|---|
| NIST / NFIQ | 16 | 8 | 5 | 5 |
| Tier III | 2 | 2 | 1 | 1 |
| Sítios operacionais | 2 | 2 | 1 | 1 |

### Demais famílias do levantamento

Não respondem às dimensões analíticas do artigo e ficam registradas por transparência.

| família | ocorrências | arquivos | documentos | documentos da CEFIC |
|---|---|---|---|---|
| Gráficas | 39 | 21 | 17 | 16 |
| Fala.BR | 7 | 1 | 1 | 0 |
| Blockchain | 6 | 3 | 2 | 2 |
| Bancos / sistema financeiro | 6 | 2 | 2 | 1 |
| Acurácia | 5 | 5 | 3 | 3 |
| Fomento | 4 | 3 | 3 | 2 |
| Polícia Federal / aditivo | 3 | 3 | 2 | 2 |

### Ausências

Das 14 famílias sem ocorrência no recorte declarado, **11 permanecem sem ocorrência** sob
normalização que expande ligaduras tipográficas e costura hifenização, e sob léxico ampliado
com sinônimos e variantes: padrão aberto, substituição de fornecedor, desenvolvimento
nacional, Nova Indústria Brasil, margem de preferência, conteúdo local, encomenda tecnológica,
software livre e código aberto, código-fonte, transferência de tecnologia e
aprisionamento/*lock-in*. A ausência é propriedade do corpus, não do procedimento.

As três famílias restantes registram apenas termos vizinhos, em ocorrências que não exprimem
o conceito:

- **capacitação tecnológica** — "capacitação" em três registros de reunião, referida à
  capacitação de órgãos emissores, de estados e de equipes, e em ato de outro órgão publicado
  na mesma página do Diário Oficial que a Resolução nº 15; "treinamento" na Lei de Acesso à
  Informação;
- **propriedade intelectual** — "patente" em relatório de visita técnica às gráficas e em
  cláusula padrão da norma ABNT NBR 17225;
- **empresa/indústria nacional** — a razão social "Empresa Brasileira de Participações em
  Energia Nuclear", em ato de outro órgão publicado na mesma página do Diário Oficial que a
  Resolução nº 1.

As 14 famílias reúnem 100 expressões, entre formas estritas e variantes, listadas uma a uma
em [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md). Em termos literais, 97 delas não ocorrem em
nenhum arquivo do corpus; as três que ocorrem são os termos vizinhos acima. A lista refere-se
apenas às famílias sem ocorrência: os termos das famílias presentes constam das tabelas
anteriores.

## Reprodução

```bash
python reproduzir.py          # refaz as buscas e reescreve as tabelas de dados/
python teste_reproducao.py    # confere os números-âncora; falha se algum divergir
python verificar_checksums.py # confere a integridade das tabelas publicadas
python gerar_busca.py         # regenera a ferramenta de busca
```

Não há dependências além da biblioteca padrão do Python, versão 3.10 ou superior. A
verificação é executada automaticamente a cada alteração enviada ao repositório e confere,
além das buscas, a composição do corpus — arquivos, documentos, resoluções e reuniões — a
partir dos inventários.

## Estrutura

```
busca_corpus_cefic.html          ferramenta de busca autocontida
README.md                         este documento
METODOLOGIA.md                    procedimento de busca, cuidados técnicos e limitações
FUNDAMENTACAO_DO_QUADRO.md        liga cada item do quadro do artigo à evidência
PRESENCAS_FORA_DO_RECORTE.md      termos com ocorrência fora do recorte declarado
TERMOS_BUSCADOS.md                as 100 expressões das famílias sem ocorrência, uma a uma
DICIONARIO_DE_DADOS.md            significado de cada coluna de cada tabela
corpus_txt/                       os 129 arquivos de texto
dados/                            inventários, resultados, proveniência e verificação
robustez_varredura.py             normalização, léxico e varredura
reproduzir.py                     regenera as tabelas de resultado e o dicionário de dados
gerar_busca.py                    gera a ferramenta de busca
teste_reproducao.py               confere os números-âncora
verificar_checksums.py            confere a integridade das tabelas
CITATION.cff                      forma de citação
datapackage.json / codemeta.json  metadados legíveis por máquina
CHECKSUMS.sha256                  hash de cada tabela publicada
```

Seis arquivos de nome excessivamente longo foram encurtados, para que o repositório funcione
em Windows sem configuração adicional; [`dados/mapa_arquivos.csv`](dados/mapa_arquivos.csv) dá
a correspondência com os nomes originais.

## Citação

Ver [CITATION.cff](CITATION.cff). O GitHub gera a citação formatada a partir desse arquivo,
pelo botão *Cite this repository*.

## Licença

Código sob licença MIT. Dados e textos derivados de documentos oficiais, sob CC BY 4.0. Ver
[LICENSE](LICENSE).
