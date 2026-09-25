# Contexto do App — Grupo 1 · AgroPrevisãoMT

**Professor:** Prof. Heitor
**Integrantes:** Bruna · Keila · Yanni · Célia
**Código de coleta:** `G1-<nnn>` · **Formulário:** 20 perguntas · **Meta:** 15–20 respostas

> Este documento é o mapa de produto do AgroPrevisãoMT: problema, personas, valor, funcionalidades, dados públicos, impacto, riscos e como o formulário de campo valida (ou derruba) a hipótese do grupo. Números citados como ilustração são hipóteses, não dados coletados.

---

## 1. Pitch em uma frase

Um app que prevê, a partir de sinais públicos do agro, **quando e onde** o crescimento rural vai pressionar emprego, transporte, moradia e serviços públicos, para que moradores, gestores e a própria empresa rural se preparem antes do aperto.

---

## 2. O problema e a oportunidade (por que agora)

Quando uma empresa rural cresce, a lavoura cresce primeiro e a cidade cresce depois. Chegam máquinas, caminhões, trabalhadores safristas, demanda por moradia, por vaga em escola, por consulta no posto e por estrada asfaltada — mas o planejamento urbano raramente é acionado com antecedência. O resultado é uma cidade que reage em vez de se preparar: aluguel que dispara, trânsito de carga no centro, fila nos serviços, ocupação irregular em periferia.

**Por que agora:**

- **Rastreabilidade pública aumentou.** Bases como IBGE (Censo, PNAD Contínua, PIB municipal), CAGED/Novo CAGED (emprego formal), INEP (matrículas), SNIS (saneamento), DATASUS e portais de transparência municipal já permitem cruzar sinais de crescimento econômico com pressão sobre serviços.
- **Safra e logística geram sazonalidade previsível.** O calendário agrícola, o volume de escoamento e a abertura de novas áreas criam ondas que se repetem — e podem ser antecipadas.
- **Cidades do interior ganharam voz digital.** Smartphone e WhatsApp chegaram ao campo e à cidade média; o custo de entregar um alerta caiu a quase zero.
- **Gestão pública pressionada por resultado.** Prefeituras pequenas precisam justificar investimento e planejar orçamento; previsão é argumento para priorizar obra e vaga.

A oportunidade é ocupar o intervalo entre "o agro já cresceu" e "a cidade percebeu" — usando dado público gratuito e linguagem simples.

---

## 3. Público e personas (2–3 personas com nome, contexto e dor)

**Dona Marlene, 54 — moradora e comerciante, cidade média do interior de MT**
Vende marmita e aluga dois quartos nos fundos de casa. Contexto: viu a lavoura se expandir e chegou gente nova na cidade. Dor: não sabe se o movimento que está vendo vai continuar, se é safra ou mudança permanente; erra o preço do aluguel e o estoque da marmita, e perde dinheiro nas duas pontas.

**Rafael, 32 — agente municipal de planejamento**
Servidor de uma prefeitura pequena, cuida de obras e mobilidade. Contexto: recebe pressão por asfalto, creche e posto de saúde, mas decide com o orçamento do ano passado. Dor: não consegue prever onde a demanda vai estourar primeiro e improvisa remendo; o dado que precisa está espalhado em sistemas que não conversam.

**Seu Anísio, 47 — gestor de empresa rural**
Administra fazenda que está ampliando área e contratando. Contexto: precisa de mão de obra, moradia para equipe e escoamento de safra. Dor: sofre com a falta de infraestrutura e de trabalhadores porque ninguém avisou a cidade que a operação ia dobrar; vira problema social o que era só logística.

---

## 4. Proposta de valor (mini canvas)

| Dores (do cliente) | Alívios | Ganhos |
|---|---|---|
| "Sinto o agro crescer, mas não sei o que isso muda na cidade." | Liga crescimento do agro a efeitos concretos em linguagem simples | Entende o que vem antes de acontecer |
| Aluguel, trânsito e serviços estouram de surpresa | Previsão por região e por horizonte (curto/médio prazo) | Planeja preço, rota, vaga e orçamento |
| Gestor decide no escuro e corre atrás do prejuízo | Painel com sinais de emprego, moradia, transporte e serviços | Prioriza investimento com base em evidência |
| Empresa rural é vista como problema, não como parceira | Visão compartilhada de impacto entre campo e cidade | Menos conflito, mais coordenação |

Proposta central: **transformar crescimento do agro em previsão útil para cidade** — não em denúncia, não em estatística, mas em decisão.

---

## 5. Jornada do usuário (passo a passo, do problema à decisão)

1. **Percepção.** Morador nota movimento novo: caminhões, gente de fora, aluguel subindo, fila maior.
2. **Curiosidade.** Ele busca entender se é passageiro ou tendência; pergunta no comércio, no grupo da cidade.
3. **Descoberta do app.** Chega por WhatsApp, indicação da associação ou da prefeitura.
4. **Leitura do cenário.** Vê mapa e alertas da região: emprego formal, pressão sobre moradia, trânsito de carga, demanda por serviços.
5. **Interpretação.** App explica o porquê em linguagem clara, com fonte do dado e nível de confiança.
6. **Decisão.**
   - Morador: ajusta aluguel, planeja mudança, busca curso/vaga.
   - Gestor: prioriza obra, creche, linha de ônibus, mutirão.
   - Empresa: antecipa moradia, transporte e contratação.
7. **Retorno.** Usuário confirma ou corrige o que viu; a previsão melhora no ciclo seguinte.

---

## 6. Funcionalidades — MVP | v1 | v2

| Funcionalidade | MVP | v1 | v2 |
|---|---|---|---|
| Mapa de calor de pressão (emprego, moradia, transporte, serviços) | Básico, 1 região | Multi-região, camadas | Mapas colaborativos |
| Alertas de curto prazo | Manual | Automático por gatilho | Preditivo com alerta personalizado |
| Explicação em linguagem simples | Texto fixo | Texto contextual | Assistente que responde perguntas |
| Fonte e nível de confiança do dado | Selo de fonte | Painel de confiança | Auditoria aberta do dado |
| Painel do gestor público | Não | Versão enxuta | Orçamento e simulação de cenário |
| Canal de coleta/validação pelo usuário | Formulário 1–5 | Formulário + áudio | Feedback contínuo geolocalizado |
| Personalização por perfil | Não | Por cidade | Por persona e interesse |
| Modo offline / baixo sinal | Leitura offline | Cache de alertas | Sincronização inteligente |

---

## 7. Diferenciais e alternativas (o que existe hoje e por que isso é melhor)

Alternativas atuais: relatórios econômicos e boletins setoriais (bons, mas genéricos e técnicos); notícia de jornal local (atrasada e pontual); sistemas oficiais de emprego e saneamento (dados ricos, mas frios e dispersos); grupos de WhatsApp da cidade (rápidos, mas sem método).

Diferenciais do AgroPrevisãoMT:

- **Foco na ponte agro × cidade**, que quase ninguém cobre de forma integrada.
- **Previsão, não retrospecto**: olha para frente usando sazonalidade e sinais antecipados.
- **Linguagem do morador**, não do pesquisador.
- **Dado público + escuta de campo**, combinando quanti (formulário 1–5) e quali (áudio WhatsApp).
- **Transparência de fonte**, essencial para confiança em previsão.

---

## 8. Dados, governo e LGPD (dados abertos, fontes, privacidade)

**Fontes públicas possíveis (a validar):** IBGE (Censo, PNAD Contínua, PIB municipal, estimativas populacionais); CAGED / Novo CAGED (admissões e desligamentos formais); INEP (matrículas e escolas); SNIS (água e esgoto); DATASUS (atendimentos e saúde); DENATRAN/RENAVAM e DER (frota e fluxo); portais de transparência municipal; dados abertos de licenciamento e obras.

**Uso no produto:** cruzar crescimento econômico (agro, emprego) com indicadores de pressão (moradia, trânsito, serviços) para gerar previsão por região e horizonte.

**Governança e LGPD:**

- Coleta somente do necessário; **perfil marcado por observação** é sensível e deve ser tratado como dado agregado, nunca individualizado.
- Anonimização e agregação por região antes de publicar qualquer camada.
- Consentimento explícito no início da coleta e do áudio; informar uso e finalidade.
- **Áudio do WhatsApp** armazenado com código `G1-<nnn>` como chave, sem nome, e apagado depois da transcrição/codificação.
- Transparência ativa: o app mostra de onde vem cada dado e o que é estimativa.
- Direito de correção e exclusão para quem participou.

---

## 9. Impacto público e sustentabilidade

**Impacto público:** planejamento antecipado de moradia, transporte, emprego e serviços; menos improviso orçamentário; mais capacidade da cidade de absorver o crescimento sem crise social; voz para o morador no desenho do futuro da região.

**Sustentabilidade (hipóteses de modelo):**

- **Parceria público-prefeitura** (licenciamento ou cooperação técnica) para painel do gestor.
- **Sindicatos rurais, cooperativas e associações** financiando a visão de impacto compartilhado.
- **Dados abertos e código aberto** para reduzir custo e ganhar credibilidade.
- **Versão social gratuita** para moradores; recursos avançados para instituições.

Tudo isso é hipótese de desenho — o teste de campo definirá o que tem valor real.

---

## 10. Métricas de sucesso (KPIs)

| Dimensão | KPI | Leitura |
|---|---|---|
| Produto | % de usuários que entendem o alerta (teste simples) | Linguagem funciona? |
| Produto | Frequência de uso por persona | Utilidade recorrente? |
| Previsão | Acurácia das previsões de pressão vs. ocorrido | O modelo acerta? |
| Campo | Respostas válidas `G1-<nnn>` com áudio correlacionado | Coleta robusta? |
| Hipótese | % que liga agro a mudanças da cidade após usar o app | Hipótese confirmada? |
| Impacto | Nº de decisões públicas/privadas influenciadas | Gera ação? |
| GovTech | Nº de fontes públicas integradas e auditáveis | Base sólida? |

---

## 11. Riscos e mitigação (tabela Risco | Mitigação)

| Risco | Mitigação |
|---|---|
| Dados públicos incompletos ou desatualizados | Combinar múltiplas fontes, sinalizar confiança e revisar periodicamente |
| Previsão errada gera descrédito | Publicar faixa de incerteza e explicar limites |
| Baixa adesão do morador | Entrada por WhatsApp, linguagem simples e retorno visível |
| Prefeitura não usar o painel | Versão enxuta, integração com rotina e capacitação curta |
| Uso indevido de dados pessoais (LGPD) | Anonimizar, agregar, consentir e excluir após uso |
| Amostra de campo pequena (15–20 respostas) | Tratar como sinal exploratório, não como prova estatística |
| Confundir correlação com causa | Explicitar que é correlação; validar em sprints seguintes |
| Dependência de parceiro único | Diversificar fontes de dado e de apoio institucional |

---

## 12. Roadmap de sprints

| Sprint | Objetivo | Entrega |
|---|---|---|
| 0 | Fundação | Estrutura do app + Bloco 0 (perfil por observação) |
| 1 | Perguntas | 20 perguntas em escala 1–5, sem resposta aberta |
| 2 | Código + planilha | Geração do código `G1-<nnn>` por resposta + registro em planilha |
| 3 | Campo + correlação | Coleta (meta 15–20) + áudio no WhatsApp iniciado pelo código |
| 4 | Análise | Tabulação quanti (1–5) + leitura quali dos áudios |
| 5 | Refino final | App pronto + relatório de achados (hipótese confirmada / parcial / derrubada) |

---

## 13. Como o formulário valida a hipótese

Hipótese: **as pessoas sentem o agro crescer, mas não conectam esse crescimento às mudanças da cidade (moradia, transporte), e veriam valor em previsões.**

Cada bloco ataca uma parte da hipótese:

| Bloco | Perguntas | O que testa na hipótese |
|---|---|---|
| 0 — Perfil (exceção, por observação) | Faixa etária, sexo, classe social, raça | Recorte de quem percebe e quem não percebe |
| 1 | Q1–Q5 — chegada do agro e informação | "Sentem o agro crescer?" e de onde vem a informação |
| 2 | Q6–Q12 — mapeamento e funcionalidades (habitação, empregos, serviços, trânsito) | "Conectam crescimento a mudanças da cidade?" e o que priorizariam |
| 3 | Q13–Q16 — formato, notificações, uso de longo prazo | "Veriam valor em previsões?" e em que formato |
| 4 | Q17–Q20 — governança, confiança e privacidade | Disposição a confiar e a compartilhar dado |

**Regra de leitura:** cada item é marcado de **1 a 5** (1 = uma dimensão, 5 = a oposta). Como **não há resposta aberta**, o "porquê" de cada nota vive no **áudio de WhatsApp**, que **começa com o código `G1-<nnn>`**. Isso permite casar a nota da planilha com a fala exata da pessoa.

**Critério de decisão (proposto):**

- Médias altas no Bloco 1 e baixas no Bloco 2 → hipótese **confirmada** (sentem, mas não conectam).
- Altas no Bloco 1 e altas no Bloco 2 → hipótese **derrubada** (já conectam).
- Padrão misto → hipótese **parcial**, exige refino de pergunta e recorte (Sprint 4–5).

Amostra de 15–20 respostas é sinal exploratório, não prova estatística — resultado contrário também é resultado.

---

## 14. Pitch de 30 segundos

O agro cresce antes da cidade se preparar. Quando a lavoura se expande, chegam caminhão, morador novo, aluguel caro, fila no posto e falta de vaga na creche — e ninguém avisou o município. O AgroPrevisãoMT cruza dados públicos do agro e do emprego com sinais de pressão urbana e entrega uma previsão simples: o que vai apertar, onde e quando. Morador se antecipa, prefeitura prioriza obra, empresa planeja gente e logística. Não é denúncia nem relatório frio — é aviso na hora certa para decidir antes do problema. Estamos testando com moradores do interior de MT se essa previsão tem valor real. Se tiver, a cidade deixa de correr atrás e começa a se preparar.

---

## Entregáveis do grupo

- [ ] Questionário validado (20 perguntas) e `formulario-app.md` final
- [ ] App testado no celular com o código `G1-<nnn>`
- [ ] Coleta com áudios correlacionados
- [ ] Relatório de achados (hipótese confirmada / parcial / derrubada)
