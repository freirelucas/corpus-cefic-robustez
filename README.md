# Corpus CEFIC — dados, código e verificação da análise documental

Material de verificação do artigo **"Identidade digital e desenvolvimento tecnológico: o
papel da Cefic"** (Boletim Radar, Ipea). Reúne o corpus documental em texto, a lista
completa dos termos buscados, o código que produz os resultados e o registro das
limitações do procedimento.

Não é preciso programar para usar este repositório. Se você chegou aqui vindo do artigo,
comece pela pergunta que o trouxe:

| Se você quer... | vá para |
|---|---|
| entender por que a ausência de termos é confiável | [METODOLOGIA.md](METODOLOGIA.md) |
| conferir os termos buscados, um a um | [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md) |
| ver cada ocorrência com arquivo e página | [`dados/kwic_cefic_corrigido.csv`](dados/kwic_cefic_corrigido.csv) |
| saber o que significa cada coluna das tabelas | [DICIONARIO_DE_DADOS.md](DICIONARIO_DE_DADOS.md) |
| ler os documentos originais em texto | [`corpus_txt/`](corpus_txt/) |
| rastrear a origem de cada documento | [`dados/proveniencia.csv`](dados/proveniencia.csv) |
| repetir a análise do zero | a seção *Como reproduzir*, abaixo |

A Câmara Executiva Federal de Identificação do Cidadão (CEFIC) foi criada pelo Decreto nº
10.900/2021 e mantida pelo Decreto nº 11.797/2023.

---

## Por que este repositório existe

Uma parte das conclusões do artigo apoia-se na **ausência** de certos termos no corpus.
Afirmar que a Cefic não tratou de transferência de tecnologia, conteúdo local ou encomenda
tecnológica é uma afirmação forte, e um resultado de busca igual a zero pode significar
duas coisas muito diferentes: que o assunto realmente não aparece nos documentos, ou que o
procedimento de busca não era capaz de encontrá-lo. Basta uma lista de termos curta demais,
um tratamento inadequado de acentuação ou uma janela de busca estreita para fabricar
ausência.

O repositório publica o procedimento inteiro para que o leitor decida por conta própria
qual dos dois casos se aplica.

---

---

## O corpus

| | |
|---|---|
| Documentos coletados | 154 |
| Cópias byte-idênticas removidas | 25 |
| **Documentos distintos analisados** | **129** |
| Páginas | 663 |
| Linhas de texto | 28.508 |
| Atos da própria CEFIC | 109 |
| Documentos de contexto (outros órgãos) | 20 |
| Resoluções (números distintos) | 33 — série 1 a 33, sem lacuna |
| Grupos de versões do mesmo documento | 9 |
| Corte do levantamento | 15/09/2026 |

A coleta reuniu 154 arquivos, dos quais 25 eram cópias exatas de outros —
duplicações da própria coleta, sem conteúdo novo. Contá-las infla as frequências sem
acrescentar evidência, de modo que foram removidas e registradas em
`dados/duplicatas_removidas.csv`. Todos os números deste repositório referem-se aos
129 documentos distintos.

Dos 129, 109 são atos ou registros da própria CEFIC — resoluções e memórias
de reunião. Os outros 20 são documentos de contexto de outros órgãos (ABNT NBR 17225,
LGPD, Lei de Acesso à Informação, Lei 14.534, decretos e portarias da SGD). Essa distinção
importa na leitura: afirmações sobre o que a Cefic diz ou deixa de dizer dizem respeito ao
primeiro conjunto.

Nove documentos aparecem no corpus em mais de uma captura — a mesma resolução publicada no
Diário Oficial e em arquivo próprio, ou a mesma memória de reunião em duas extrações. Os
conteúdos não são idênticos, de modo que nenhum foi descartado; os grupos estão declarados
em `dados/versoes_mesmo_documento.csv`, para que quem reanalisar possa contar por documento
ou por arquivo. As contagens deste repositório são por arquivo.

Os PDFs originais não são redistribuídos. `dados/sha256_pdfs.csv` traz o hash SHA-256 de
cada um, o que permite verificar que o texto publicado aqui corresponde ao documento
oficial de origem. Os textos são atos normativos e documentos administrativos públicos.

---

---

## O que foi encontrado

### 5.1 Famílias das duas dimensões do artigo

| família | ocorrências | documentos | situação |
|---|---|---|---|
| Território nacional | 38 | 16 | presente; contagem anterior inflada por copias redundantes |
| Interoperabilidade | 34 | 19 | presente; contagem anterior inflada por copias redundantes |
| Preferência normativa | 12 | 10 | familia acrescentada no teste (fora do recorte original) |
| Multifornecedor / segundo motor | 3 | 3 | presente |
| Soberania | 3 | 2 | presente |
| Concorrência | 3 | 2 | presente |
| Propriedade intelectual | 0 | 0 | ausencia do sintagma; termos vizinhos presentes, marginais |
| Capacitação tecnológica | 0 | 0 | ausencia do sintagma; termos vizinhos presentes, marginais |
| Aprisionamento / lock-in | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Empresa/indústria nacional | 0 | 0 | ausencia do sintagma; termos vizinhos presentes, marginais |
| Código-fonte | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Conteúdo local | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Software livre / código aberto | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Padrão aberto | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Nova Indústria Brasil | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Margem de preferência | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Encomenda tecnológica | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Desenvolvimento nacional | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Substituição de fornecedor | 0 | 0 | ausencia confirmada (robusta a sinonimos) |
| Transferência de tecnologia | 0 | 0 | ausencia confirmada (robusta a sinonimos) |

### 5.2 Demais famílias do levantamento

Estas famílias pertencem ao estudo paralelo sobre os certames do Serviço Biométrico Federal
e não respondem às dimensões analíticas do artigo. Ficam registradas por transparência.

| família | ocorrências | documentos |
|---|---|---|
| Gráficas | 57 | 29 |
| NIST / NFIQ | 16 | 8 |
| Fala.BR | 7 | 1 |
| Bancos / sistema financeiro | 6 | 2 |
| Blockchain | 6 | 3 |
| Acurácia | 5 | 5 |
| Fomento | 4 | 3 |
| Polícia Federal / aditivo | 3 | 3 |
| Sítios operacionais | 2 | 2 |
| Tier III | 2 | 2 |

### 5.3 O teste de ausência

Das 14 famílias com contagem zero no recorte original, **11 continuam em zero** depois de
corrigida a normalização e de ampliado o léxico. A ausência, nesses casos, é propriedade do
corpus e não do método: padrão aberto, substituição de fornecedor, desenvolvimento nacional,
Nova Indústria Brasil, margem de preferência, conteúdo local, encomenda tecnológica,
software livre e código aberto, código-fonte, transferência de tecnologia e
aprisionamento/*lock-in*.

Três famílias saem do zero apenas por termos vizinhos isolados, que não sustentam a presença
do conceito: uma menção a "patente" em relatório de visita técnica, quatro a "capacitação"
em contexto de divulgação da CIN e uma a "treinamento". Estão nas tabelas da seção 8.

Em termos literais — a forma em que o leitor pode conferir manualmente —, **97 dos
100 termos buscados não ocorrem em nenhum documento do corpus**.

---

---

## O que a ausência autoriza concluir

Há uma leitura que a evidência sustenta e outra que ela não sustenta.

O corpus mostra que os instrumentos clássicos da política industrial de compras não
aparecem nas deliberações nem nas normas da Cefic. Mostra também **por que**: a Câmara não
opera por contratação. O termo "licitação" aparece 3 vezes no corpus e em nenhum documento
da própria Cefic. O instrumento pelo qual ela regula quem pode operar na infraestrutura é
outro — o **credenciamento**, que ocorre 81 vezes em 26 documentos da Câmara, em passagens
como "credenciamento de instituições públicas e empresas privadas para atuarem como
Gráficas da CIN".

A ausência, portanto, indica menos uma omissão da Cefic do que o alcance do instrumento de
que ela dispõe. Concluir que a Câmara "ignora o desenvolvimento tecnológico" iria além do
que os documentos permitem; concluir que ela não maneja os instrumentos de compra que
poderiam induzi-lo é o que a evidência sustenta.

Vale igualmente registrar o que o corpus **não** pode demonstrar: ele é composto de normas e
registros de deliberação, não de dados de mercado. Requisitos que favorecem a
contestabilidade — interoperabilidade, preferência por mais de um fornecedor — não
equivalem a efeitos observados sobre a concorrência.

---

O procedimento que sustenta essas afirmações, com os cuidados técnicos que ele exige, está
descrito em [METODOLOGIA.md](METODOLOGIA.md); as limitações conhecidas, na seção final
daquele documento.

---

## Como reproduzir

```bash
python reproduzir.py        # refaz as buscas e reescreve as tabelas de dados/
python teste_reproducao.py  # confere os números-âncora e falha se algum divergir
python verificar_checksums.py
```

Não há dependências além da biblioteca padrão do Python (3.10 ou superior). A verificação
roda automaticamente a cada alteração enviada ao repositório.

---

## Estrutura

```
README.md                         este documento — porta de entrada
METODOLOGIA.md                    procedimento de busca, cuidados técnicos e limitações
TERMOS_BUSCADOS.md                os 100 termos, um a um, com o resultado de cada
DICIONARIO_DE_DADOS.md            o que significa cada coluna de cada tabela
corpus_txt/                       os 129 documentos distintos em texto
dados/                            tabelas de resultado, proveniência e verificação
robustez_varredura.py             normalização, léxico e varredura
reproduzir.py                     regenera todas as tabelas
teste_reproducao.py               confere os números-âncora
verificar_checksums.py            confere a integridade das tabelas publicadas
varredura_original_referencia.py  procedimento anterior, mantido para comparação
CITATION.cff                      como citar
datapackage.json / codemeta.json  metadados legíveis por máquina
CHECKSUMS.sha256                  hash de cada tabela publicada
```

---

## Como citar

Ver [CITATION.cff](CITATION.cff). O GitHub gera a citação formatada a partir desse arquivo,
pelo botão *Cite this repository*.

## Licença

Código sob licença MIT. Dados e textos derivados de documentos oficiais, sob CC BY 4.0.
Ver [LICENSE](LICENSE).
