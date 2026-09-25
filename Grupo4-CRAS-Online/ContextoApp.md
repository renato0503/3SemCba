# Contexto do App — Grupo 4 · CRAS Online

**Professor:** Prof. Renato
**Integrantes:** Anna · Maria Eduarda · Marcelly · Kaique
**Código de coleta:** `G4-<nnn>` · **Formulário:** 20 perguntas · **Meta:** 15–20 respostas

---

## 1. Pitch em uma frase

Um CRAS no bolso do cidadão: enviar documentos, agendar atendimento e acompanhar o pedido pelo celular, com segurança e apoio humano, para resolver o serviço social sem sair de casa.

---

## 2. O problema e a oportunidade

O atendimento do CRAS ainda depende de presença física. Quem precisa de um benefício, de uma orientação ou do CadÚnico enfrenta deslocamento, fila de espera e, muitas vezes, perde um dia inteiro de trabalho para resolver algo que poderia começar por um formulário.

O problema é composto:

- **Distância e transporte:** o CRAS pode ficar longe, e o custo do deslocamento pesa no orçamento de quem mais precisa.
- **Fila e tempo perdido:** chegar cedo, esperar, ser atendido tarde; o dia produtivo se perde.
- **Informação escassa:** pouca gente sabe o que o CRAS faz, quais documentos levar e quais serviços existem.
- **Papel e repetição:** o cidadão leva documentos físicos, muitas vezes volta porque faltou algo, e refaz o caminho.

A oportunidade está em digitalizar a **porta de entrada** do atendimento — não o atendimento inteiro. Começar por documento, agendamento, status e dúvida significa reduzir a ida desnecessária ao CRAS, organizar a fila e liberar o servidor para o que exige cuidado humano. É uma vitória de eficiência e de dignidade ao mesmo tempo.

---

## 3. Público e personas

O público central são famílias de baixa renda que já dependem ou podem depender da assistência social. Três perfis ajudam a desenhar o produto.

| Persona | Perfil | Dor principal | O que ela espera |
|---|---|---|---|
| **Dona Neide, 54 anos** | Mãe de família, renda baixa, usa o celular para WhatsApp e pouco mais | Não sabe quais documentos levar; já voltou do CRAS sem resolver | Que alguém diga o que levar e que ela possa agendar |
| **Jovem Wesley, 22 anos** | Cuida da avó, faz trabalhos informais, usa o celular o dia todo | Perde dias de trabalho acompanhando a avó ao CRAS | Enviar documentos pelo celular e acompanhar o status |
| **Seu Antônio, 67 anos** | Baixa familiaridade digital, às vezes depende de terceiros para mexer no celular | Desconfia de mandar documentos por aplicativo e teme golpe | Atendimento humano, orientação clara e confirmação de que é oficial |

A persona de baixa familiaridade digital é um requisito de projeto, não um detalhe: se o app funciona para o Seu Antônio, funciona para todos.

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
|---|---|
| **Problema** | Deslocamento, fila, perda de dia de trabalho e falta de informação sobre o CRAS |
| **Público** | Famílias que usam ou precisam da assistência social, com níveis diferentes de familiaridade digital |
| **Proposta de valor** | Resolver a porta de entrada do CRAS pelo celular, com segurança, linguagem simples e apoio humano |
| **Canais** | Celular (app), WhatsApp oficial para áudio e suporte, unidade do CRAS como ponto de apoio |
| **Fontes de confiança** | gov.br, selo verificado, número oficial e atendente humano disponível |
| **Custo de não fazer** | Cidadão continua perdendo dias; CRAS continua com fila e retrabalho de papel |
| **Métricas** | Tempo até o primeiro retorno, taxa de pedido resolvido sem ir ao local, satisfação do cidadão |

---

## 5. Jornada: do cadastro ao benefício, sem sair de casa

1. **Descoberta:** o cidadão ouve falar do serviço no CRAS, no posto de saúde, na escola ou pela divulgação.
2. **Entrada segura:** acessa com a conta gov.br, o que confirma que ele é quem diz ser.
3. **Orientação:** uma primeira tela explica o que o CRAS faz e quais serviços estão disponíveis.
4. **Cadastro do pedido:** responde o essencial e escolhe o serviço (benefício, CadÚnico, orientação).
5. **Envio de documentos:** fotografa ou anexa os documentos pedidos, com indicação do que falta.
6. **Agendamento:** escolhe dia e horário quando a presença ainda for necessária.
7. **Acompanhamento:** vê o status do pedido (recebido, em análise, pendente, concluído) e recebe aviso de pendência.
8. **Conclusão:** resolve online quando possível; vai ao CRAS apenas na etapa que exige presença, já sabendo o que levar.

O ponto de desenho: cada passo reduz uma ida evitável. O presencial deixa de ser o começo e passa a ser a exceção.

---

## 6. Funcionalidades

| Funcionalidade | MVP | v1 | v2 |
|---|---|---|---|
| **Upload de documentos** | Foto/envio de documentos principais, com lista do que é exigido | Validação de legibilidade e alerta de pendência | Leitura assistida de dados e histórico de anexos por pedido |
| **Agendamento** | Escolha de serviço e pedido de agendamento com retorno por WhatsApp | Agenda com horários e confirmação | Reagendamento pelo app e lembretes automáticos |
| **Status do pedido** | Consulta por código do pedido | Estados claros e aviso de pendência | Linha do tempo do pedido com histórico |
| **Dúvidas** | Perguntas frequentes e canal de suporte | Atendente humano por chat/WhatsApp com continuidade | Base de dúvidas que aprende com as perguntas mais recorrentes |

Regra de ouro do MVP: fazer pouco, mas fazer o caminho crítico (documento, agendamento, status, dúvida) funcionar sem travar.

---

## 7. Diferenciais e alternativas

| Alternativa | Como funciona hoje | Limite | Onde o CRAS Online se diferencia |
|---|---|---|---|
| **Presencial** | Cidadão vai ao CRAS, pega fila e é atendido | Exige deslocamento e perda de dia; retrabalho por documento faltante | Começa o pedido antes da visita e elimina idas evitáveis |
| **Telefone** | Ligação para tirar dúvida ou agendar | Ocupa linha, não anexa documento, não registra histórico | Registra anexo, status e histórico por código de pedido |
| **Apps do governo** | Serviços digitais federais e estaduais oficiais | Foco em outras áreas; pouca orientação para quem tem baixa familiaridade digital | Linguagem simples, apoio humano e desenho para o público do CRAS |

O diferencial não é "mais um app do governo": é ser **ponte** entre o cidadão e o serviço, com segurança visível e humano acessível.

---

## 8. Dados, governo e LGPD

- **Identificação:** entrada via gov.br, aproveitando a autenticação oficial existente.
- **Documentos sensíveis:** documentos de assistência social são dados pessoais sensíveis; o app guarda o mínimo necessário e pelo tempo necessário.
- **Base legal e sigilo:** o tratamento segue a LGPD e o sigilo do atendimento socioassistencial; quem só precisa ver, vê.
- **Transparência:** o cidadão sabe o que está enviando, para quê e quem terá acesso.
- **Segurança:** transmissão protegida, acesso controlado por perfil e registro de quem consultou cada pedido.
- **Confiança como requisito:** selo verificado, número oficial e confirmação de que aquele canal é do CRAS, nunca de terceiros.

Digitalizar não pode significar expor. O desenho assume que o medo do cidadão é legítimo e responde a ele com regra, não com promessa.

---

## 9. Impacto público e sustentabilidade

**Impacto público**

- Reduz deslocamento, fila e perda de dia de trabalho para o cidadão.
- Organiza a demanda do CRAS, separando o que é online do que exige presença.
- Diminui retrabalho por documento faltante, liberando o servidor para o atendimento humano.
- Amplia o conhecimento sobre o CRAS, hoje desconhecido por parte do público.

**Sustentabilidade**

- Nasce como projeto do grupo, mas o desenho prevê continuidade: integração com gov.br, uso de canais existentes e operação no CRAS.
- O custo marginal cai conforme o online absorve a demanda repetitiva.
- O presencial permanece para os casos que exigem cuidado, e é justamente onde ele importa mais.

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede | Direção desejada |
|---|---|---|
| Pedidos resolvidos sem ir ao CRAS | Quanto do fluxo migrou para o online | Aumentar |
| Taxa de pendência por documento | Quantos pedidos travam por falta de anexo | Reduzir |
| Tempo até o primeiro retorno | Velocidade de resposta ao cidadão | Reduzir |
| Agendamentos cumpridos | Eficiência da agenda física | Aumentar |
| Uso do apoio humano | Quanto o cidadão quer falar com atendente | Monitorar (não zerar) |
| Confiança declarada | Disposição de enviar documento pelo app | Aumentar |
| Conhecimento sobre o CRAS | Quantos sabem o que o CRAS faz | Aumentar |

Os KPIs de confiança vêm direto do formulário de campo: eles testam a hipótese junto com o produto.

---

## 11. Riscos e mitigação

| Risco | Descrição | Mitigação |
|---|---|---|
| **Golpes e fraude** | Criminosos se passam pelo CRAS para obter documentos e dados | Canal oficial único, selo verificado, aviso claro de que o CRAS não pede senha nem pagamento |
| **Falsidade de documentos** | Envio de documento adulterado | Conferência na análise, cruzamento com bases oficiais e checagem humana nos casos suspeitos |
| **Baixa alfabetização digital** | Parte do público não consegue usar o app | Linguagem simples, apoio humano e WhatsApp como porta de entrada alternativa |
| **Documento ilegível ou incompleto** | Pedido trava por foto ruim ou anexo faltante | Lista do que levar, validação de legibilidade e alerta de pendência |
| **Vazamento de dados sensíveis** | Exposição de informação socioassistencial | Acesso por perfil, registro de consulta, guarda mínima e sigilo |
| **Exclusão de quem não tem celular** | Parte do público fica de fora do online | Presencial mantido e ponto de apoio no CRAS para quem precisa |
| **Baixa adesão** | Poucos conhecem ou confiam no serviço | Divulgação, tela explicativa e prova de confiabilidade no primeiro uso |

A hipótese de campo já aponta dois riscos centrais: desconhecimento e desconfiança. Mitigação de golpe e de exclusão entra no MVP, não depois.

---

## 12. Roadmap de sprints

| Sprint | Objetivo | Entrega |
|---|---|---|
| **0 — Fundação** | Estrutura do app e do projeto | Base do app + Bloco 0 (perfil) definido |
| **1 — Perguntas** | Montar as 20 perguntas | Questionário em escala 1–5 pronto para o campo |
| **2 — Código + planilha** | Gerar e registrar respostas | Código por resposta + respostas na planilha |
| **3 — Campo + correlação** | Coletar na rua | Coleta no shopping + áudios por código `G4-<nnn>` |
| **4 — Análise** | Ler os dados | Tabulação quanti + leitura quali das falas |
| **5 — Refino final** | Fechar o produto | App ajustado + relatório de achados |

Cada sprint entrega algo verificável. O campo alimenta o produto, e o produto devolve a próxima pergunta.

---

## 13. Como o formulário valida a hipótese (blocos + áudio)

O formulário de 20 perguntas é o instrumento que testa a hipótese: **poucos conhecem o CRAS e há desconfiança em enviar documentos por app, mesmo reconhecendo a dor do presencial.**

| Bloco | Perguntas | O que mede | O que valida na hipótese |
|---|---|---|---|
| **1** | Q1–Q5 | Conhecimento e uso do CRAS | Se o CRAS é conhecido ou invisível |
| **2** | Q6–Q10 | Impacto (fila, transporte, perda de dia, benefício) | Se a dor do presencial é real e forte |
| **3** | Q11–Q15 | Confiança no digital (documento, número oficial, selo, atendente humano) | Se há desconfiança e o que a reduz |
| **4** | Q16–Q20 | Preferência e solução (agendar, enviar documento, tirar dúvida, usar pelo celular) | Se o cidadão adotaria a solução |

**Regras de aplicação**

- **Bloco 0 — Perfil** é exceção: o entrevistador marca **por observação** (faixa etária, sexo, classe social, raça).
- As **20 perguntas** são marcadas **de 1 a 5**, com **1 em um polo e 5 no polo oposto**.
- **Não há respostas abertas.** Sugestões, desabafos e contexto vão para o **áudio no WhatsApp**.
- O áudio **começa com o código** `G4-<nnn>`, o mesmo gerado pela resposta salva.

**Por que o áudio importa**

O número mostra a direção; o áudio mostra o porquê. O código `G4-<nnn>` costura os dois: cada resposta quantitativa tem uma fala correspondente, permitindo correlação entre o que a pessoa marcou e o que ela explicou. É a diferença entre saber que a desconfiança existe e entender o que a provoca.

Meta de coleta: **15–20 respostas**, com áudios correlacionados por código.

---

## 14. Pitch de 30 segundos

"Hoje, resolver algo no CRAS custa um dia inteiro: transporte, fila e, muitas vezes, uma segunda ida porque faltou um documento. Nosso projeto permite enviar documentos, agendar atendimento e acompanhar o pedido pelo celular, com login gov.br, selo verificado e atendimento humano quando o cidadão quiser. Nossa hipótese é que poucos conhecem o CRAS e que há desconfiança em mandar documento por app, mesmo com a dor do presencial. Por isso estamos testando em campo, com 20 perguntas e áudios no WhatsApp, para construir a solução com quem realmente vai usar."
