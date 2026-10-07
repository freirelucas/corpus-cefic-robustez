# Corpus CEFIC — dados, código e verificação da análise documental

Material de verificação do artigo **"Identidade digital e desenvolvimento tecnológico: o
papel da Cefic"** (Boletim Radar, Ipea). Reúne o corpus documental em texto, a lista completa
dos termos buscados, o código que produz os resultados e o registro das limitações do
procedimento.

O artigo conclui que a regulamentação da identificação biométrica federal incorpora
requisitos de concorrência, mas não instrumentos de desenvolvimento tecnológico nacional.
Essa segunda conclusão apoia-se em ausências: **97 dos 100 termos buscados não ocorrem em
nenhum dos 129 documentos do corpus**, e 11 das 14 famílias sem ocorrência permanecem sem
ocorrência quando o léxico é ampliado com sinônimos e variantes. Este repositório publica o
corpus e o procedimento para que essas ausências possam ser verificadas de forma
independente.

A Câmara Executiva Federal de Identificação do Cidadão (CEFIC) foi criada pelo Decreto nº
10.900/2021 e mantida pelo Decreto nº 11.797/2023. O material corresponde à versão do artigo
submetida ao Boletim Radar; o corte do levantamento é 15/09/2026.

## Busca no corpus

O arquivo **[`busca_corpus_cefic.html`](busca_corpus_cefic.html)** é uma ferramenta de busca autocontida: um único
arquivo HTML, com o corpus embutido, que funciona offline em qualquer navegador, sem
servidor, sem instalação e sem conexão. O download é feito pelo botão *Download raw file* na
página do arquivo; a abertura, por duplo clique. Cada ocorrência é exibida com o documento, a
página e o trecho em que consta.

A ferramenta traz atalhos para os termos cuja ausência sustenta conclusões do artigo —
*transferência de tecnologia*, *conteúdo local*, *encomenda tecnológica*, entre outros — e
para termos presentes, como *interoperabilidade* e *território nacional*, o que permite
comparar os dois casos. Um filtro restringe a busca aos atos da própria CEFIC.

## Orientação

| objetivo | documento |
|---|---|
| buscar um termo no corpus | [`busca_corpus_cefic.html`](busca_corpus_cefic.html) |
| conferir em que se apoia cada item do quadro do artigo | [FUNDAMENTACAO_DO_QUADRO.md](FUNDAMENTACAO_DO_QUADRO.md) |
| examinar o procedimento de busca e seus limites | [METODOLOGIA.md](METODOLOGIA.md) |
| consultar os termos buscados, um a um | [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md) |
| localizar cada ocorrência com arquivo e página | [`dados/kwic_estrito.csv`](dados/kwic_estrito.csv) |
| interpretar as colunas das tabelas | [DICIONARIO_DE_DADOS.md](DICIONARIO_DE_DADOS.md) |
| ler os documentos originais em texto | [`corpus_txt/`](corpus_txt/) |
| consultar termos com ocorrência fora do recorte do artigo | [PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md) |
| rastrear a origem de cada documento | [`dados/proveniencia.csv`](dados/proveniencia.csv) |
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
| Documentos coletados | 154 |
| Cópias byte-idênticas descartadas | 25 |
| **Documentos distintos analisados** | **129** |
| Páginas | 663 |
| Linhas de texto | 28,508 |
| Atos e registros da própria CEFIC | 109 |
| Documentos de contexto, de outros órgãos | 20 |
| Resoluções, números distintos | 33 — série 1 a 33, sem lacuna |
| Grupos de versões do mesmo documento | 9 |
| Corte do levantamento | 15/09/2026 |

A coleta reuniu 154 arquivos, dos quais 25 eram cópias exatas de outros.
Contá-las elevaria as frequências sem acrescentar evidência, de modo que foram descartadas na
constituição do corpus e registradas em [`dados/copias_identicas.csv`](dados/copias_identicas.csv).
Todos os números referem-se aos 129 documentos distintos.

Entre esses, 109 são atos ou registros da própria CEFIC — resoluções e memórias de
reunião — e 20 são documentos de contexto de outros órgãos: ABNT NBR 17225, Lei Geral de
Proteção de Dados, Lei de Acesso à Informação, Lei nº 14.534, decretos e portarias da SGD. A
distinção importa na leitura, pois afirmações sobre o que a Cefic enuncia referem-se ao
primeiro conjunto.

Nove documentos constam do corpus em mais de uma captura — a mesma resolução publicada no
Diário Oficial e em arquivo próprio, ou a mesma memória de reunião em duas extrações. Os
conteúdos diferem entre si, de modo que nenhum foi descartado; os grupos estão declarados em
[`dados/versoes_mesmo_documento.csv`](dados/versoes_mesmo_documento.csv), o que permite contar
por documento ou por arquivo. As contagens deste repositório são por arquivo.

Os PDFs originais não são redistribuídos. [`dados/sha256_pdfs.csv`](dados/sha256_pdfs.csv) traz
o hash SHA-256 de cada um, o que permite confrontar o texto publicado com o documento oficial
de origem. Os textos são atos normativos e documentos administrativos públicos.

## Resultados

### Famílias das duas dimensões analíticas do artigo

| família | ocorrências | documentos | situação |
|---|---|---|---|
| Território nacional | 38 | 16 | presente |
| Interoperabilidade | 34 | 19 | presente |
| Preferência normativa | 12 | 10 | presente; família acrescentada ao léxico no teste de robustez |
| Multifornecedor / segundo motor | 3 | 3 | presente |
| Soberania | 3 | 2 | presente |
| Concorrência | 3 | 2 | presente |
| Propriedade intelectual | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Capacitação tecnológica | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Aprisionamento / lock-in | 0 | 0 | ausência robusta a sinônimos e variantes |
| Empresa/indústria nacional | 0 | 0 | sintagma ausente; termos vizinhos presentes em ocorrências marginais |
| Código-fonte | 0 | 0 | ausência robusta a sinônimos e variantes |
| Conteúdo local | 0 | 0 | ausência robusta a sinônimos e variantes |
| Software livre / código aberto | 0 | 0 | ausência robusta a sinônimos e variantes |
| Padrão aberto | 0 | 0 | ausência robusta a sinônimos e variantes |
| Nova Indústria Brasil | 0 | 0 | ausência robusta a sinônimos e variantes |
| Margem de preferência | 0 | 0 | ausência robusta a sinônimos e variantes |
| Encomenda tecnológica | 0 | 0 | ausência robusta a sinônimos e variantes |
| Desenvolvimento nacional | 0 | 0 | ausência robusta a sinônimos e variantes |
| Substituição de fornecedor | 0 | 0 | ausência robusta a sinônimos e variantes |
| Transferência de tecnologia | 0 | 0 | ausência robusta a sinônimos e variantes |

### Demais famílias do levantamento

Pertencem ao estudo paralelo sobre os certames do Serviço Biométrico Federal e não respondem
às dimensões analíticas do artigo. Ficam registradas por transparência.

| família | ocorrências | documentos |
|---|---|---|
| Gráficas | 39 | 21 |
| NIST / NFIQ | 16 | 8 |
| Fala.BR | 7 | 1 |
| Bancos / sistema financeiro | 6 | 2 |
| Blockchain | 6 | 3 |
| Acurácia | 5 | 5 |
| Fomento | 4 | 3 |
| Polícia Federal / aditivo | 3 | 3 |
| Sítios operacionais | 2 | 2 |
| Tier III | 2 | 2 |

### Ausências

Das 14 famílias sem ocorrência no recorte declarado, **11 permanecem sem ocorrência** sob
normalização que expande ligaduras tipográficas e costura hifenização, e sob léxico ampliado
com sinônimos e variantes: padrão aberto, substituição de fornecedor, desenvolvimento
nacional, Nova Indústria Brasil, margem de preferência, conteúdo local, encomenda tecnológica,
software livre e código aberto, código-fonte, transferência de tecnologia e
aprisionamento/*lock-in*. A ausência é propriedade do corpus, não do procedimento.

Três famílias registram ocorrência apenas por termos vizinhos isolados, que não sustentam a
presença do conceito: uma menção a "patente" em relatório de visita técnica, quatro a
"capacitação" em contexto de divulgação da Carteira de Identidade Nacional e uma a
"treinamento".

Em termos literais, **97 dos 100 termos buscados não ocorrem em nenhum documento**.

## Reprodução

```bash
python reproduzir.py          # refaz as buscas e reescreve as tabelas de dados/
python teste_reproducao.py    # confere os números-âncora; falha se algum divergir
python verificar_checksums.py # confere a integridade das tabelas publicadas
python gerar_busca.py         # regenera a ferramenta de busca
```

Não há dependências além da biblioteca padrão do Python, versão 3.10 ou superior. A
verificação é executada automaticamente a cada alteração enviada ao repositório.

## Estrutura

```
busca_corpus_cefic.html          ferramenta de busca autocontida
README.md                         este documento
METODOLOGIA.md                    procedimento de busca, cuidados técnicos e limitações
FUNDAMENTACAO_DO_QUADRO.md        liga cada item do quadro do artigo à evidência
PRESENCAS_FORA_DO_RECORTE.md      termos com ocorrência fora do recorte declarado
TERMOS_BUSCADOS.md                os 100 termos, um a um, com o resultado de cada
DICIONARIO_DE_DADOS.md            significado de cada coluna de cada tabela
corpus_txt/                       os 129 documentos distintos em texto
dados/                            tabelas de resultado, proveniência e verificação
robustez_varredura.py             normalização, léxico e varredura
reproduzir.py                     regenera todas as tabelas
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
