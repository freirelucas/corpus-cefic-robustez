# Termos buscados

As 100 expressões que compõem as 14 famílias sem ocorrência no recorte declarado, em forma
literal, com o resultado de cada uma nos 129 arquivos do corpus. **97 das 100 expressões não
ocorrem em nenhum arquivo**; as três que ocorrem são termos vizinhos em ocorrências marginais,
descritas no [README](README.md#ausências). Os termos das famílias presentes —
interoperabilidade, território nacional e as demais — não integram esta lista; seus
resultados constam das tabelas ao final.

A conferência manual em um PDF requer a opção **"Palavras inteiras"** ativada. Sem ela,
siglas curtas produzem falso positivo: `NIB` casa no interior de *disponibilidade*, `ETEC` no
de *detecção* e `cativo` no de *aplicativo*.

O travessão (—) indica que o termo não ocorre em nenhum arquivo. "Arq." indica arquivos.

A mesma informação em formato tabular está em
[`dados/termos_buscados_conferencia.csv`](dados/termos_buscados_conferencia.csv). A
localização de cada ocorrência dos termos presentes, com arquivo e página, está em
[`dados/kwic_estrito.csv`](dados/kwic_estrito.csv). A ferramenta
[`busca_corpus_cefic.html`](busca_corpus_cefic.html) permite verificar qualquer termo diretamente no corpus.

**Padrão aberto**

| termo | ocorrências |
|---|---|
| padrão aberto | — |
| padrões abertos | — |
| padronização aberta | — |
| especificação aberta | — |
| especificações abertas | — |
| open standard | — |
| API pública | — |
| API aberta | — |

**Substituição de fornecedor**

| termo | ocorrências |
|---|---|
| substituição de fornecedor | — |
| substituição do fornecedor | — |
| troca de fornecedor | — |
| trocar de fornecedor | — |
| mudança de fornecedor | — |
| portabilidade de fornecedor | — |
| migração de fornecedor | — |
| substituição da solução | — |
| substituição de tecnologia | — |

**Desenvolvimento nacional**

| termo | ocorrências |
|---|---|
| desenvolvimento nacional | — |
| desenvolvimento tecnológico nacional | — |
| desenvolvimento local | — |
| nacionalização | — |
| produção nacional | — |
| solução nacional | — |
| tecnologia nacional | — |
| autonomia tecnológica | — |

**Empresa/indústria nacional**

| termo | ocorrências |
|---|---|
| empresa nacional | — |
| empresas nacionais | — |
| indústria nacional | — |
| fabricante nacional | — |
| fornecedor nacional | — |
| fornecedores nacionais | — |
| capital nacional | — |
| sediada no país | — |

**Nova Indústria Brasil**

| termo | ocorrências |
|---|---|
| Nova Indústria Brasil | — |
| NIB | — |
| política industrial | — |
| BNDES | — |
| FINEP | — |

**Margem de preferência**

| termo | ocorrências |
|---|---|
| margem de preferência | — |
| margens de preferência | — |
| critério de desempate | — |
| Lei 14.133 | — |

**Conteúdo local**

| termo | ocorrências |
|---|---|
| conteúdo local | — |
| conteúdo nacional | — |
| índice de nacionalização | — |
| processo produtivo básico | — |
| PPB | — |

**Encomenda tecnológica**

| termo | ocorrências |
|---|---|
| encomenda tecnológica | — |
| encomenda pública | — |
| ETEC | — |
| Lei de Inovação | — |
| contratação de solução inovadora | — |
| CPSI | — |

**Software livre / código aberto**

| termo | ocorrências |
|---|---|
| software livre | — |
| software público | — |
| código aberto | — |
| open source | — |
| licença livre | — |
| licença pública | — |
| GitHub | — |
| repositório público | — |

**Código-fonte**

| termo | ocorrências |
|---|---|
| código-fonte | — |
| código fonte | — |
| códigos-fonte | — |
| acesso ao código | — |
| entrega do código | — |
| source code | — |
| escrow | — |

**Propriedade intelectual**

| termo | ocorrências |
|---|---|
| propriedade intelectual | — |
| propriedade industrial | — |
| direitos patrimoniais | — |
| patente | 1 em 1 arq. |
| titularidade dos direitos | — |
| titularidade dos resultados | — |
| INPI | — |
| licenciamento | — |

**Transferência de tecnologia**

| termo | ocorrências |
|---|---|
| transferência de tecnologia | — |
| transferência tecnológica | — |
| transferência de conhecimento | — |
| absorção tecnológica | — |
| repasse de tecnologia | — |
| internalização da tecnologia | — |

**Capacitação tecnológica**

| termo | ocorrências |
|---|---|
| capacitação tecnológica | — |
| capacitação técnica | — |
| capacitação | 4 em 4 arq. |
| treinamento | 1 em 1 arq. |
| formação de equipes | — |
| formação de pessoal | — |
| qualificação técnica | — |

**Aprisionamento / lock-in**

| termo | ocorrências |
|---|---|
| aprisionamento | — |
| lock-in | — |
| lock in | — |
| vendor lock | — |
| dependência tecnológica | — |
| dependência de fornecedor | — |
| dependência do fornecedor | — |
| cativo | — |
| monopólio | — |
| fornecedor único | — |
| exclusividade | — |

---

## Contagens por família

As famílias agrupam termos que designam o mesmo conceito. Contagens no nível estrito; a
tabela completa, com o nível ampliado, está em
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

Fonte: corpus documental da CEFIC.
Elaboração dos autores.
