# Corpus CEFIC — dados, código e verificação da análise documental

Corpus documental, inventários, código e resultados que fundamentam a análise documental do
artigo **"Identidade digital e desenvolvimento tecnológico: o papel da Cefic"** (Boletim
Radar, Ipea). O artigo examina os atos e registros da Câmara Executiva Federal de
Identificação do Cidadão (CEFIC), criada pelo Decreto nº 10.900/2021 e mantida pelo Decreto
nº 11.797/2023, em duas dimensões: concorrência e contestabilidade, e desenvolvimento
tecnológico nacional. Versão 1.2.1; coleta dos documentos em 14/09/2026.

## Busca no corpus

**[Abrir a ferramenta de busca](https://rawcdn.githack.com/freirelucas/corpus-cefic-robustez/v1.2.1/busca_corpus_cefic.html)**

A ferramenta pesquisa o texto integral dos 105 documentos e exibe cada ocorrência com o
documento, a página e o trecho em que consta. Selecionada uma ocorrência, o documento
inteiro abre ao lado, com todas as ocorrências assinaladas e navegação entre elas. Traz atalhos para os termos cuja ausência
fundamenta o artigo — *transferência de tecnologia*, *conteúdo local*, *encomenda
tecnológica*, entre outros — e para termos presentes, como *interoperabilidade* e *território
nacional*. Um filtro restringe a busca aos documentos da CEFIC. O arquivo
[`busca_corpus_cefic.html`](busca_corpus_cefic.html) contém o corpus embutido e funciona
também offline, depois de baixado.

## Corpus

| categoria | documentos |
|---|---|
| Resoluções | 33 |
| Retificações de resolução | 2 |
| Registros de reunião (atas e memórias) | 40 |
| Apresentações exibidas em reunião | 3 |
| Relatórios de visita técnica | 3 |
| Anexo de resolução | 1 |
| **Documentos da CEFIC** | **82** |
| Portarias de designação da SGD/MGI | 12 |
| Leis e decretos | 8 |
| Norma técnica ABNT NBR 17225 | 1 |
| Relatório de impacto à proteção de dados (Ministério da Economia) | 1 |
| Documento sem camada de texto, autoria não determinada | 1 |
| **Documentos de outros órgãos** | **23** |
| **Total** | **105** |

Os 105 documentos somam 580 páginas. A coleta reuniu 154 PDFs; 24 eram cópias byte-idênticas
de outros e 25 eram capturas adicionais de documentos já presentes, de que se manteve uma por
documento pelo critério descrito em [METODOLOGIA.md](METODOLOGIA.md). Ambos os conjuntos estão
registrados em [`dados/copias_identicas.csv`](dados/copias_identicas.csv) e
[`dados/capturas_preteridas.csv`](dados/capturas_preteridas.csv). Todas as contagens são por
documento. A classificação de cada documento está em
[`dados/inventario_documentos.csv`](dados/inventario_documentos.csv); afirmações sobre o que a
CEFIC enuncia referem-se aos 82 documentos da própria CEFIC.

## Resultados

Contagens no nível estrito de busca. O nível ampliado, com sinônimos e variantes, está em
[`dados/resultados_por_familia.csv`](dados/resultados_por_familia.csv).

### Famílias das duas dimensões analíticas do artigo

| família | ocorrências | documentos | documentos da CEFIC | situação |
|---|---|---|---|---|
| Território nacional | 31 | 12 | 7 | presente |
| Interoperabilidade | 27 | 15 | 9 | presente |
| Preferência normativa | 9 | 7 | 5 | presente |
| Multifornecedor / segundo motor | 2 | 2 | 2 | presente |
| Soberania | 3 | 2 | 1 | presente |
| Concorrência | 3 | 2 | 1 | presente |
| Capacitação tecnológica | 0 | 0 | 0 | ausente no nível estrito; termos vizinhos no ampliado |
| Propriedade intelectual | 0 | 0 | 0 | ausente no nível estrito; termos vizinhos no ampliado |
| Aprisionamento / lock-in | 0 | 0 | 0 | ausente nos dois níveis |
| Conteúdo local | 0 | 0 | 0 | ausente nos dois níveis |
| Código-fonte | 0 | 0 | 0 | ausente nos dois níveis |
| Desenvolvimento nacional | 0 | 0 | 0 | ausente nos dois níveis |
| Empresa/indústria nacional | 0 | 0 | 0 | ausente nos dois níveis |
| Encomenda tecnológica | 0 | 0 | 0 | ausente nos dois níveis |
| Margem de preferência | 0 | 0 | 0 | ausente nos dois níveis |
| Nova Indústria Brasil | 0 | 0 | 0 | ausente nos dois níveis |
| Padrão aberto | 0 | 0 | 0 | ausente nos dois níveis |
| Software livre / código aberto | 0 | 0 | 0 | ausente nos dois níveis |
| Substituição de fornecedor | 0 | 0 | 0 | ausente nos dois níveis |
| Transferência de tecnologia | 0 | 0 | 0 | ausente nos dois níveis |

### Termos que sustentam afirmações do texto fora do quadro

| família | ocorrências | documentos | documentos da CEFIC |
|---|---|---|---|
| NIST / NFIQ | 9 | 5 | 5 |
| Tier III | 1 | 1 | 1 |
| Sítios operacionais | 1 | 1 | 1 |

### Demais famílias do levantamento

Famílias auxiliares do levantamento, fora das dimensões analíticas do artigo.

| família | ocorrências | documentos | documentos da CEFIC |
|---|---|---|---|
| Gráficas | 32 | 17 | 16 |
| Fala.BR | 7 | 1 | 0 |
| Bancos / sistema financeiro | 6 | 2 | 1 |
| Blockchain | 5 | 2 | 2 |
| Fomento | 4 | 3 | 2 |
| Acurácia | 3 | 3 | 3 |
| Polícia Federal / aditivo | 2 | 2 | 2 |

### Ausências

Das 14 famílias sem ocorrência no nível estrito, 12 também não ocorrem no nível ampliado:
padrão aberto, substituição de fornecedor, desenvolvimento nacional, empresa/indústria
nacional, Nova Indústria Brasil, margem de preferência, conteúdo local, encomenda
tecnológica, software livre e código aberto, código-fonte, transferência de tecnologia e
aprisionamento/*lock-in*.

Nas duas restantes, o nível ampliado encontra apenas termos vizinhos:

- **capacitação tecnológica** — "capacitação" em três registros de reunião, referida à
  capacitação de órgãos emissores, de estados e de equipes; "treinamento" na Lei de Acesso à
  Informação;
- **propriedade intelectual** — "patente" em relatório de visita técnica às gráficas e em
  cláusula padrão da norma ABNT NBR 17225.

As 14 famílias reúnem 100 expressões, listadas em [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md).
Noventa e sete não ocorrem em nenhum documento; as três que ocorrem são "patente",
"capacitação" e "treinamento", nos contextos acima.

## Resoluções e reuniões

Listas geradas a partir de [`dados/inventario_resolucoes.csv`](dados/inventario_resolucoes.csv)
e [`dados/inventario_reunioes.csv`](dados/inventario_reunioes.csv); a verificação automatizada
confere que coincidem com eles.

<!-- listas: gerado por reproduzir.py a partir de dados/ -->

### As 33 resoluções

| nº | data | ementa | publicação no DOU | texto |
|---|---|---|---|---|
| 1 | 24/03/2022 | Regimento Interno da Câmara-Executiva Federal de Identificação do Cidadão. | 01/04/2022, ed. 63, seç. 1, p. 25 | [`res1`](corpus_txt/res1.txt) |
| 2 | 02/06/2022 | Credenciamento Provisório da Câmara-Executiva Federal de Identificação do Cidadão. | 03/06/2022, ed. 105, seç. 1, p. 6 | [`res2`](corpus_txt/res2.txt) |
| 3 | 13/06/2022 | Fluxograma da expedição da Carteira de Identidade Nacional, aplicado às Unidades da Federação, pertencentes ao Projeto Piloto. | 15/06/2022, ed. 113, seç. 1, p. 7 | [`resolucao_n__3__de_13_de_junho_de_2022`](corpus_txt/resolucao_n__3__de_13_de_junho_de_2022.txt) |
| 4 | 07/06/2022 | Parametrização técnica do Serviço de Identificação do Cidadão. | 15/06/2022, ed. 113, seç. 1, p. 8 | [`res4`](corpus_txt/res4.txt) |
| 5 | 11/08/2022 | Regulamenta a opção da pessoa natural pelo modelo físico em cartão de policarbonato. | 15/08/2022, ed. 154, seç. 1, p. 3 | [`res5`](corpus_txt/res5.txt) |
| 6 | 13/10/2022 | Altera o art. 7º, da Resolução nº 4, de 7 de junho de 2022 e dá outras providências. | 14/10/2022, ed. 196, seç. 1, p. 5 | [`res6`](corpus_txt/res6.txt) |
| 7 | 13/10/2022 | Institui grupo de trabalho técnico destinado à elaboração de Protocolo de Divergências no âmbito do Sistema de Identificação do Cidadão como proposição de ações destinadas ao processo de emissão da Carteira de Identidade Nacional (CIN) e de atualização das bases. | 14/10/2022, ed. 196, seç. 1, p. 5 | [`res7`](corpus_txt/res7.txt) |
| 8 | 13/10/2022 | Institui grupo de trabalho técnico para realização de diagnóstico e proposição de ações destinadas ao fortalecimento do processo de emissão da Carteira de Identidade Nacional (CIN). | 14/10/2022, ed. 196, seç. 1, p. 5 | [`res8`](corpus_txt/res8.txt) |
| 9 | 07/11/2022 | Altera o art. 7º, da Resolução nº 4, de 7 de junho de 2022 e dá outras providências. | 17/11/2022, ed. 216, seç. 1, p. 13 | [`res9`](corpus_txt/res9.txt) |
| 10 | 06/04/2023 | Revoga a Resolução nº 1, de 24 de março de 2023 e aprova o Regimento Interno da Câmara-Executiva Federal de Identificação do Cidadão-CEFIC. | 14/04/2023, ed. 72, seç. 1, p. 1 | [`res10`](corpus_txt/res10.txt) |
| 11 | 06/04/2023 | Institui Grupo de Trabalho Técnico para apresentar Minuta de alteração do Decreto nº 10.977, de 23 de fevereiro de 2022, quanto à disposição dos campos "sexo" e "nome social" na Carteira de Identidade Nacional. | 10/04/2023, ed. 68, seç. 1, p. 4 | [`res11`](corpus_txt/res11.txt) |
| 12 | 28/07/2023 | Institui Grupo de Trabalho Técnico para debater questões técnicas, analisar e propor soluções no âmbito do Serviço de Identificação do Cidadão. | 02/08/2023, ed. 146, seç. 1, p. 55 | [`res12`](corpus_txt/res12.txt) |
| 13 | 28/07/2023 | Dispõe sobre o procedimento e a forma de acesso à base do Cadastro de Pessoas Físicas da Secretaria Especial da Receita Federal do Brasil do Ministério da Fazenda, no âmbito de expedição da Carteira de Identidade de que trata a Lei nº 7.116, de 29 de agosto de 1983. | 02/08/2023, ed. 146, seç. 1, p. 56 | [`res13`](corpus_txt/res13.txt) |
| 14 | 21/08/2023 | Altera o art. 2º, da Resolução nº 13, de 28 de julho de 2023 e dá outras providências. | 23/08/2023, ed. 161, seç. 1, p. 43 | [`res14`](corpus_txt/res14.txt) |
| 15 | 01/11/2023 | Altera o art. 2º, da Resolução nº 9, de 7 de novembro de 2022 e dá outras providências. | 06/11/2023, ed. 210, seç. 1, p. 34 | [`res15`](corpus_txt/res15.txt) |
| 16 | 22/01/2024 | Institui Grupo de Trabalho Técnico para apresentar proposta de ações para aumentar e fortalecer a segurança da emissão da Carteira de Identidade Nacional. | 26/01/2024, ed. 19, seç. 1, p. 36 | [`res16`](corpus_txt/res16.txt) |
| 17 | 04/06/2024 | Institui Grupo de Trabalho Técnico 01 para elaborar planejamento estruturado, monitorar atividades e subsidiar decisões da CEFIC. | 07/06/2024, ed. 108, seç. 1, p. 50 | [`res17`](corpus_txt/res17.txt) |
| 18 | 04/06/2024 | Institui Grupo de Trabalho Técnico 02 para acompanhamento e monitoramento do processo emissão da Carteira de Identidade Nacional junto às unidades federativas. | 07/06/2024, ed. 108, seç. 1, p. 50 | [`res18`](corpus_txt/res18.txt) |
| 19 | 04/06/2024 | Institui Grupo de Trabalho Técnico 03 para acompanhamento, alinhamento e compartilhamento dos desenvolvimentos técnicos dos diferentes órgãos integradores e envolvidos na emissão da CIN e integrantes do Serviço de Identificação Civil. | 06/06/2024, ed. 107, seç. 1, p. 52 | [`res19`](corpus_txt/res19.txt) |
| 20 | 09/09/2024 | Institui o Modelo Informacional da Carteira de Identidade Nacional, no âmbito dos órgãos de identificação civil dos Estados e do Distrito Federal e dos órgãos federais executores do Serviço de Identificação do Cidadão. | 20/09/2024, ed. 183, seç. 1, p. 5 | [`res20`](corpus_txt/res20.txt) |
| 21 | 06/02/2025 | Institui o Serviço Biométrico Federal para identificar e verificar biometricamente os requerentes da Carteira de Identidade Nacional-CIN e dispõe sobre o Fluxograma da expedição da CIN, aplicado às Unidades da Federação e ao Governo Federal, em conformidade com o Serviço Biométrico Federal. | 13/02/2025, ed. 31, seç. 1, p. 5 | [`res21`](corpus_txt/res21.txt) |
| 22 | 05/05/2025 | Altera o Anexo I da Resolução nº 21, de 6 de fevereiro de 2025, da Câmara Executiva Federal de Identificação do Cidadão - CEFIC, que institui o Serviço Biométrico Federal para identificar e verificar biometricamente os requerentes da Carteira de Identidade Nacional - CIN e dispõe sobre o fluxograma da expedição da CIN, aplicado às Unidades da Federação e ao Governo Federal, em conformidade com o Serviço Biométrico Federal. | 08/05/2025, ed. 85, seç. 1, p. 1 | [`res22`](corpus_txt/res22.txt) |
| 23 | 05/05/2025 | Altera a Resolução nº 20, de 9 de setembro de 2024, da Câmara Executiva Federal de Identificação do Cidadão - CEFIC, que institui o Modelo Informacional da Carteira de Identidade Nacional, no âmbito dos órgãos de identificação civil dos Estados e do Distrito Federal e dos órgãos federais executores do Serviço de Identificação do Cidadão, e dá outras providências. | 09/05/2025, ed. 86, seç. 1, p. 3 | [`res23`](corpus_txt/res23.txt) |
| 24 | 08/09/2025 | Institui o Modelo Informacional da Carteira de Identidade Nacional - MI-CIN, no âmbito dos Órgãos de Identificação Civil - OICs das unidades federativas e dos órgãos federais executores do Serviço de Identificação do Cidadão - SIC; Revoga o art. 2º da Resolução nº 9, de 7 de novembro de 2022, Câmara Executiva Federal de Identificação do Cidadão - Cefic, a Resolução nº 20, de 9 de setembro de 2024, da Cefic, a Resolução nº 23, de 5 de maio de 2025, da Cefic. | 15/09/2025, ed. 175, seç. 1, p. 5 | [`res24`](corpus_txt/res24.txt) |
| 25 | 08/09/2025 | Institui e define a composição e as atribuições do Grupo de Trabalho Técnico 1 (GTT 1), para elaborar o planejamento das ações da Câmara-Executiva Federal de Identificação do Cidadão - Cefic. | 15/09/2025, ed. 175, seç. 1, p. 15 | [`res25`](corpus_txt/res25.txt) |
| 26 | 08/09/2025 | Institui o Grupo de Trabalho Técnico 2 (GTT 2), para acompanhar e aprimorar o processo de emissão da Carteira de Identidade Nacional, no âmbito dos Órgãos de Identificação Civil das unidades federativas. | 15/09/2025, ed. 175, seç. 1, p. 15 | [`res26`](corpus_txt/res26.txt) |
| 27 | 08/09/2025 | Institui Grupo de Trabalho Técnico 3 (GTT 3), para acompanhar e propor ações de aprimoramento técnico dos procedimentos e operações do processo de emissão da Carteira de Identidade Nacional - CIN, no âmbito do Serviço de Identificação do Cidadão - SIC e de demais órgãos federais envolvidos. | 15/09/2025, ed. 175, seç. 1, p. 15 | [`res27`](corpus_txt/res27.txt) |
| 28 | 08/09/2025 | Dispõe sobre o procedimento para reimpressão da Carteira de Identidade Nacional - CIN. | 15/09/2025, ed. 175, seç. 1, p. 16 | [`res28`](corpus_txt/res28.txt) |
| 29 | 02/02/2026 | Dispõe sobre a aprovação do Protocolo de Divergências, que orientará os procedimentos para tratamento das divergências verificadas no âmbito da emissão da Carteira de Identidade Nacional - CIN, no domínio do Serviço Biométrico Federal - SBF. | 10/02/2026, ed. 28, seç. 1, p. 1 | [`res29`](corpus_txt/res29.txt) |
| 30 | 02/02/2026 | Institui o Serviço de Controle do Fluxo de Emissão da Carteira de Identidade Nacional - SCF-CIN. | 10/02/2026, ed. 28, seç. 1, p. 2 | [`res30`](corpus_txt/res30.txt) |
| 31 | 16/03/2026 | Institui e define a composição e as atribuições do Grupo de Trabalho Técnico 1 (GTT 1), para elaborar planejamento estruturado, monitorar atividades e subsidiar decisões da Câmara-Executiva Federal de Identificação do Cidadão - Cefic. | 19/03/2026, ed. 53, seç. 1, p. 2 | [`res31`](corpus_txt/res31.txt) |
| 32 | 03/06/2026 | Dispõe sobre o cancelamento da Carteira de Identidade Nacional, emitida ou em processo de emissão, no âmbito dos Órgãos de Identificação Civil das unidades federativas e dos órgãos federais executores do Serviço de Identificação do Cidadão. | 15/06/2026, ed. 109, seç. 1, p. 2 | [`resolucao-no-32_03_06_2026`](corpus_txt/resolucao-no-32_03_06_2026.txt) |
| 33 | 03/06/2026 | Institui o Plano de Implantação do Serviço Biométrico Federal e define data de adoção do Fluxograma de expedição da Carteira de Identidade Nacional. | 15/06/2026, ed. 109, seç. 1, p. 3 | [`resolucao-no-33_03_06_2026`](corpus_txt/resolucao-no-33_03_06_2026.txt) |

Retificações publicadas:

- Resolução nº 21: DOU de 14/02/2025, ed. 32, seç. 1, p. 1 — [`retificacao___retificacao___dou___imprensa_nacional`](corpus_txt/retificacao___retificacao___dou___imprensa_nacional.txt)
- Resolução nº 24: DOU de 01/10/2025, ed. 187, seç. 1, p. 7 — [`ret_res24`](corpus_txt/ret_res24.txt)

### As 40 reuniões com registro

Ordem e tipo tais como declarados no cabeçalho de cada registro.

| | data | ordem e tipo declarados | modalidade | registro | observação |
|---|---|---|---|---|---|
| 1 | 14/03/2022 | 1ª ordinária | presencial | [`ata_1_14mar22`](corpus_txt/ata_1_14mar22.txt) | cabeçalho grafa a data como "014/03/2022" |
| 2 | 24/03/2022 | 2ª ordinária | videoconferência | [`ata2areuniaodacefic`](corpus_txt/ata2areuniaodacefic.txt) |  |
| 3 | 05/05/2022 | 3ª ordinária | videoconferência | [`Ata3aReuCEFIC1`](corpus_txt/Ata3aReuCEFIC1.txt) |  |
| 4 | 11/05/2022 | 4ª ordinária | deliberação por e-mail | [`Ata4aReu_CEFIC1`](corpus_txt/Ata4aReu_CEFIC1.txt) |  |
| 5 | 18/05/2022 | 5ª extraordinária | deliberação por e-mail | [`Ata5aReu_CEFICv4`](corpus_txt/Ata5aReu_CEFICv4.txt) |  |
| 6 | 31/05/2022 | 6ª ordinária | videoconferência | [`Atada6reuniaoCEFIC.v2`](corpus_txt/Atada6reuniaoCEFIC.v2.txt) | duas reuniões distintas na mesma data |
| 7 | 31/05/2022 | 7ª ordinária | deliberação por e-mail | [`Atada7reuniaoCEFIC.v2`](corpus_txt/Atada7reuniaoCEFIC.v2.txt) | duas reuniões distintas na mesma data |
| 8 | 11/08/2022 | 8ª ordinária | videoconferência | [`ATA8reudacefic11`](corpus_txt/ATA8reudacefic11.txt) |  |
| 9 | 05/04/2023 | 1ª ordinária | presencial | [`1reuniao_Cefic_06_04_2023-`](corpus_txt/1reuniao_Cefic_06_04_2023-.txt) | nome do arquivo indica 06/04/2023; o cabeçalho, 05/04/2023 |
| 10 | 21/07/2023 | extraordinária | virtual, para votação | [`1_reunicextra_cefic_21_07_2023`](corpus_txt/1_reunicextra_cefic_21_07_2023.txt) | cabeçalho sem ordem; nome do arquivo indica 1ª extraordinária |
| 11 | 10/08/2023 | 1ª ordinária | presencial | [`3_reuniao_cefic_10_08_2023`](corpus_txt/3_reuniao_cefic_10_08_2023.txt) | cabeçalho declara 1ª ordinária de 2023, ordem já atribuída à reunião de 05/04/2023; nome do arquivo indica 3ª |
| 12 | 21/08/2023 | 2ª extraordinária | virtual, para votação | [`2_reunicextra_cefic_21_08_2023`](corpus_txt/2_reunicextra_cefic_21_08_2023.txt) |  |
| 13 | 11/10/2023 | 4ª ordinária | presencial | [`4___reuniao_CEFIC_11_10_2023`](corpus_txt/4___reuniao_CEFIC_11_10_2023.txt) |  |
| 14 | 21/12/2023 | 5ª ordinária | presencial | [`5_reuniao_cefic_2023_12_21`](corpus_txt/5_reuniao_cefic_2023_12_21.txt) |  |
| 15 | 15/05/2024 | 1ª extraordinária | presencial | [`1-reunic-ordinaria-15_05_2024`](corpus_txt/1-reunic-ordinaria-15_05_2024.txt) | cabeçalho declara 1ª extraordinária; nome do arquivo indica 1ª ordinária; a reunião de 27/05/2024 também se declara 1ª extraordinária |
| 16 | 27/05/2024 | 1ª extraordinária | virtual, para votação | [`2024-05-27_memoria-de-reuniao-1a-reuniao-extradordinaria-cefic`](corpus_txt/2024-05-27_memoria-de-reuniao-1a-reuniao-extradordinaria-cefic.txt) |  |
| 17 | 02/07/2024 | não declarados | presencial | [`2024-07-02_memoria-de-reuniao-2a-reuniao-ordinaria-cefic`](corpus_txt/2024-07-02_memoria-de-reuniao-2a-reuniao-ordinaria-cefic.txt) | cabeçalho sem ordem nem tipo; nome do arquivo indica 2ª ordinária |
| 18 | 06/08/2024 | 2ª ordinária | presencial | [`2024-08-06_memoria-de-reuniao-3a-reuniao-ordinaria-cefic`](corpus_txt/2024-08-06_memoria-de-reuniao-3a-reuniao-ordinaria-cefic.txt) | cabeçalho declara 2ª ordinária; nome do arquivo indica 3ª |
| 19 | 20/08/2024 | 2ª extraordinária | virtual, para votação | [`2024-08-20_memoria-de-reuniao-2a-reuniao-extraordinaria-cefic`](corpus_txt/2024-08-20_memoria-de-reuniao-2a-reuniao-extraordinaria-cefic.txt) |  |
| 20 | 01/10/2024 | 5ª extraordinária | presencial | [`2024-10-01_memoria-de-reuniao-4a-reuniao-cefic`](corpus_txt/2024-10-01_memoria-de-reuniao-4a-reuniao-cefic.txt) | cabeçalho declara 5ª extraordinária; nome do arquivo indica 4ª reunião |
| 21 | 03/12/2024 | 5ª ordinária | presencial | [`2024-12-03_memoria-de-reuniao-5a-reuniao-cefic`](corpus_txt/2024-12-03_memoria-de-reuniao-5a-reuniao-cefic.txt) |  |
| 22 | 19/12/2024 | 3ª extraordinária | presencial | [`2024-12-19_memoria-de-reuniao-3a-reuniao-extraordinaria-cefic`](corpus_txt/2024-12-19_memoria-de-reuniao-3a-reuniao-extraordinaria-cefic.txt) |  |
| 23 | 11/03/2025 | 1ª ordinária | presencial e videoconferência | [`Memoria1aReuniaoCEFIC20250311v2`](corpus_txt/Memoria1aReuniaoCEFIC20250311v2.txt) |  |
| 24 | 22/04/2025 | 2ª ordinária | presencial | [`Memoria2aReuniaoCEFIC20250422`](corpus_txt/Memoria2aReuniaoCEFIC20250422.txt) |  |
| 25 | 13/05/2025 | 3ª ordinária | presencial | [`Memoria3aReuniaoCEFIC202505131`](corpus_txt/Memoria3aReuniaoCEFIC202505131.txt) |  |
| 26 | 10/06/2025 | 4ª ordinária | presencial | [`2025.06.10MemriadaReunioCEFICFINAL`](corpus_txt/2025.06.10MemriadaReunioCEFICFINAL.txt) |  |
| 27 | 10/07/2025 | 5ª ordinária | presencial | [`2025.07.10MemriadaReunioCEFIC_FINAL`](corpus_txt/2025.07.10MemriadaReunioCEFIC_FINAL.txt) |  |
| 28 | 15/08/2025 | 6ª ordinária | presencial | [`2025.08.15MemriadaReunioCEFIC`](corpus_txt/2025.08.15MemriadaReunioCEFIC.txt) |  |
| 29 | 09/09/2025 | 7ª ordinária | presencial | [`2025.09.09MemriadaReunioCEFIC`](corpus_txt/2025.09.09MemriadaReunioCEFIC.txt) |  |
| 30 | 09/12/2025 | 8ª ordinária | presencial | [`2025.12.09MemriaCefic`](corpus_txt/2025.12.09MemriaCefic.txt) |  |
| 31 | 16/12/2025 | 1ª extraordinária | virtual, para votação | [`2025.12.16CEFICMemriadareunio`](corpus_txt/2025.12.16CEFICMemriadareunio.txt) |  |
| 32 | 11/02/2026 | 1ª ordinária | presencial | [`2026.02.11CEFICMemriadareuniov2`](corpus_txt/2026.02.11CEFICMemriadareuniov2.txt) |  |
| 33 | 26/02/2026 | 1ª extraordinária | virtual, para votação | [`2026.02.26CEFICMemriadeReunioVirtual`](corpus_txt/2026.02.26CEFICMemriadeReunioVirtual.txt) |  |
| 34 | 12/03/2026 | 2ª ordinária | presencial | [`2026.03.12MemriadaReunioCEFIC1`](corpus_txt/2026.03.12MemriadaReunioCEFIC1.txt) |  |
| 35 | 16/04/2026 | 3ª ordinária | presencial | [`2026.04.16MemriadaReunioCEFIC1`](corpus_txt/2026.04.16MemriadaReunioCEFIC1.txt) |  |
| 36 | 17/04/2026 | 2ª extraordinária | virtual, para votação | [`2026.04.17MemriadaReunioVirtualCEFIC`](corpus_txt/2026.04.17MemriadaReunioVirtualCEFIC.txt) |  |
| 37 | 13/05/2026 | 4ª ordinária | presencial | [`2026-05-13-memoria-da-reuniao-cefic`](corpus_txt/2026-05-13-memoria-da-reuniao-cefic.txt) |  |
| 38 | 16/06/2026 | 5ª ordinária | presencial | [`2026-06-16-memoria-da-reuniao-cefic`](corpus_txt/2026-06-16-memoria-da-reuniao-cefic.txt) |  |
| 39 | 14/07/2026 | 6ª ordinária | presencial | [`2026.07.14MemriadaReunioCEFIC`](corpus_txt/2026.07.14MemriadaReunioCEFIC.txt) |  |
| 40 | 11/08/2026 | 7ª ordinária | presencial | [`2026.08.11MemriadaReunioCEFIC`](corpus_txt/2026.08.11MemriadaReunioCEFIC.txt) |  |

<!-- fim das listas -->

## Arquivos

| arquivo | conteúdo |
|---|---|
| [METODOLOGIA.md](METODOLOGIA.md) | constituição do corpus, procedimento de busca e limitações |
| [FUNDAMENTACAO_DO_QUADRO.md](FUNDAMENTACAO_DO_QUADRO.md) | correspondência entre cada item do quadro do artigo e o resultado da busca |
| [TERMOS_BUSCADOS.md](TERMOS_BUSCADOS.md) | as 100 expressões das famílias sem ocorrência, uma a uma |
| [PRESENCAS_FORA_DO_RECORTE.md](PRESENCAS_FORA_DO_RECORTE.md) | termos com ocorrência fora do recorte do artigo |
| [DICIONARIO_DE_DADOS.md](DICIONARIO_DE_DADOS.md) | significado de cada coluna de cada tabela |
| [`corpus_txt/`](corpus_txt/) | os 105 documentos em texto, com marcação de página |
| [`dados/`](dados/) | inventários, resultados, ocorrências com documento e página, proveniência |
| `robustez_varredura.py` | normalização, léxico e varredura |
| `reproduzir.py` | regenera as tabelas de resultado, o dicionário de dados e as listas acima |
| `gerar_busca.py` | gera a ferramenta de busca |
| `teste_reproducao.py`, `verificar_checksums.py` | conferem os números declarados e a integridade das tabelas |
| `CITATION.cff`, `datapackage.json`, `codemeta.json` | metadados de citação e de dados |

Os PDFs originais não são redistribuídos;
[`dados/sha256_pdfs.csv`](dados/sha256_pdfs.csv) traz o hash SHA-256 de cada um, para
conferência contra a fonte oficial. Cinco arquivos de nome longo foram encurtados;
[`dados/mapa_arquivos.csv`](dados/mapa_arquivos.csv) dá a correspondência com os nomes
originais.

## Reprodução

```bash
python reproduzir.py          # refaz as buscas e reescreve as tabelas de dados/
python teste_reproducao.py    # confere os números declarados; falha se algum divergir
python verificar_checksums.py # confere a integridade das tabelas publicadas
python gerar_busca.py         # regenera a ferramenta de busca
```

Requer apenas Python 3.10 ou superior, sem bibliotecas externas. A verificação é executada
automaticamente a cada alteração do repositório.

## Citação e licença

Citação conforme [CITATION.cff](CITATION.cff) (botão *Cite this repository*). Código sob
licença MIT; dados e textos derivados de documentos oficiais, sob CC BY 4.0. Ver
[LICENSE](LICENSE).
