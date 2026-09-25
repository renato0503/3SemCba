# Contexto do App — Fila Cidadã

**Grupo 2 — Fila Cidadã** · Prof. Renato · Integrantes: Amanda, Stefanny Rosa, Stefany, Kemylly.
Código de coleta: `G2-<nnn>` · Formulário: 20 perguntas · Meta: 20 respostas.

---

## 1. Pitch em uma frase

O Fila Cidadã diz ao cidadão, antes de sair de casa, **quais documentos levar, qual órgão procurar e quanto tempo ele provavelmente vai esperar na fila** — para que ninguém mais perca uma viagem por falta de informação.

## 2. O problema e a oportunidade (por que agora)

Ir ao INSS, ao Detran, a um posto do Poupatempo, a uma prefeitura, a um cartório ou a uma UBS ainda é uma tarefa de tentativa e erro. O cidadão não sabe:

- se o órgão está com fila grande naquele dia e horário;
- se vai conseguir ser atendido hoje ou se é melhor remarcar;
- exatamente quais documentos levar (RG, CPF, comprovante de residência, NIS, comprovantes específicos);
- em qual unidade ou setor ele deve realmente ir — muitas vezes o serviço não está no endereço que ele imaginou.

**Hipótese de campo do grupo:** a maior dor é o tempo de fila, e muitos cidadãos já perderam uma viagem por não saber quais documentos levar.

**Por que agora.** Três movimentos se encontram:

1. **Digitalização dos serviços** — portais de órgãos, Poupatempo, agendamento online e gov.br já concentram parte do atendimento, mas a informação está fragmentada e desatualizada.
2. **Onipresença do WhatsApp no Brasil** — o canal que o cidadão já usa pode virar canal de consulta, sem exigir app novo nem letramento digital avançado.
3. **Cultura de dados abertos e atendimento por agendamento** — órgãos públicos passaram a produzir dados de fila e tempo de atendimento que hoje quase não são usados pelo público.

A oportunidade não é substituir o órgão público — é **orientar o cidadão antes do deslocamento** e reduzir atendimentos repetidos, filas presenciais desnecessárias e viagens perdidas.

## 3. Público e personas

**Persona 1 — Dona Marlene, 58 anos, aposentada (Venâncio Aires–RS)**
Precisa resolver uma revisão de benefício no INSS. Usa WhatsApp todos os dias, mas tem medo de baixar aplicativo novo e de errar o preenchimento. Não sabe se o atendimento é por agendamento ou por ordem de chegada. Dor: chegar às 7h, pegar fila longa e descobrir que falta o comprovante de residência atualizado. O que ela quer: "o que eu levo e quanto tempo eu espero?"

**Persona 2 — Amanda, 29 anos, atendente/auxiliar administrativa**
Precisa resolver RG, CNH e cadastro do NIS em curto prazo, sempre encaixando entre seus horários de trabalho. Compara unidades pela distância e pelo tempo de espera. Dor: perder meio dia de expediente (e salário) numa repartição com fila longa. O que ela quer: escolher o melhor dia e horário, e sair de casa sabendo que está tudo certo.

**Persona 3 — Ricardo, 41 anos, microempreendedor**
Frequenta cartório, prefeitura e junta comercial para abrir e manter o MEI. Tem urgência: cada ida ao centro custa uma tarde inteira. Dor: fazer agendamento no lugar errado e voltar duas vezes com a mesma documentação. O que ele quer: um roteiro de documentos e unidade, e alerta quando a fila fica crítica.

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
| --- | --- |
| **Tarefa do usuário** | Resolver um serviço público presencial com o mínimo de idas e espera. |
| **Dores** | Fila longa, tempo de espera imprevisível, documentação incompleta, ida ao órgão errado, perda de dia de trabalho. |
| **Ganhos esperados** | Chegar com os documentos certos na primeira tentativa, escolher melhor horário, saber a quem se dirigir, ter previsibilidade de tempo. |
| **Solução** | Orientação de documentos + situação de fila + tempo estimado de espera + indicação da unidade/setor. |
| **Canais** | WhatsApp (principal), web responsiva; opção por fila/agendamento. |
| **Proposta de valor** | "Antes de sair de casa, saiba onde ir, o que levar e quanto tempo esperar." |
| **Alternativa atual** | Site do órgão, telefone, 0800, balcão de informação, boca a boca. |

## 5. Jornada do usuário

**Antes de sair de casa**
O cidadão descreve o serviço (ex.: "2ª via de RG", "cadastro do NIS", "revisão de benefício"). O app lista os documentos obrigatórios (RG, CPF, comprovante de residência, NIS, comprovantes específicos do serviço), mostra a unidade mais adequada (INSS, Detran, Poupatempo/postos, prefeitura, cartório, UBS) e o tempo estimado de espera naquele dia/horário. Ele decide: ir agora, ir mais tarde ou agendar.

**No órgão**
Ele chega com a documentação completa, sabe qual setor procurar e usa o acompanhamento para saber se a fila está andando. Se algo estiver errado, o próprio app sinaliza o que pode faltar.

**Depois**
O cidadão avalia o atendimento, confirma se o tempo estimado bateu com o real e, se o serviço não puder ser concluído no dia, recebe o lembrete do que ainda falta. Cada retorno alimenta o histórico e melhora as estimativas.

## 6. Funcionalidades — MVP | v1 | v2

| Capacidade | MVP | v1 | v2 |
| --- | --- | --- | --- |
| Checklist de documentos por serviço | Sim (manual, serviços prioritários) | Ampliado (mais serviços e órgãos) | Personalizado por tipo de cidadão |
| Situação de fila | Indicador simples (baixa/média/alta) | Atualização frequente com histórico | Previsão por dia e horário |
| Tempo estimado de espera | Estimativa por faixa | Estimativa por unidade | Modelo preditivo com dados reais |
| Indicação de onde ir | Nome + endereço da unidade | Mapa e orientação de setor | Roteiro multiunidade |
| Agendamento | Link para o canal do órgão | Pré-agendamento integrado | Reagendamento automático |
| Acompanhamento | Não | Acompanhar posição/status | Alertas inteligentes |
| Canal | WhatsApp + web | WhatsApp + web | WhatsApp, web e totem/balcão |
| Alertas | Não | Lembrete de documentos | Aviso de fila crítica e melhor janela |

## 7. Diferenciais e alternativas

| Alternativa | Limitação | Diferencial do Fila Cidadã |
| --- | --- | --- |
| Site oficial do órgão | Informação técnica, dispersa e nem sempre atualizada | Linguagem simples e checklist por serviço |
| Telefone / 0800 | Espera longa, horário restrito, sem visão de fila | Resposta imediata e disponível por WhatsApp |
| WhatsApp do órgão | Atende o serviço, mas não orienta o deslocamento nem a fila | Foco na viagem: onde ir, o que levar, quanto esperar |
| Aplicativos de fila isolados | Cobertura de um só órgão ou unidade | Visão multiórgão com o mesmo padrão de resposta |
| "Ir e ver no balcão" | Custo alto: viagem, tempo, dia de trabalho perdido | Consulta antes de sair de casa |

**Diferencial central:** o app não é do órgão nem contra o órgão — é **do cidadão**, organizando a informação pública para reduzir atrito no atendimento presencial.

## 8. Dados, governo e LGPD

**Integração com órgãos e dados públicos.** A base inicial usa dados públicos: endereços e horários de unidades, serviços oferecidos, canais de agendamento e indicadores de atendimento já divulgados. A situação e o tempo de fila combinam três fontes:

1. dados abertos e divulgação oficial do órgão;
2. informações de agendamento, quando disponíveis;
3. contribuições anônimas e agregadas dos usuários (tempo real percebido), nunca obrigatórias.

**LGPD.** Princípios adotados:

- **Minimização:** coletar apenas o necessário para orientar — tipo de serviço, unidade e horário.
- **Anonimização/agregação:** indicadores de fila são publicados de forma agregada; o dado individual não identifica ninguém.
- **Finalidade explícita:** uso exclusivo para orientar o atendimento; nada de perfil comercial.
- **Consentimento e transparência:** aviso claro sobre uso dos dados e retirada de consentimento.
- **Segurança:** dados sensíveis (benefício, saúde) nunca em texto livre; acesso restrito.
- **Direitos do titular:** consulta, correção e exclusão de dados.

O app não substitui o órgão, não garante atendimento e deixa explícito que o tempo de espera é **estimativa**.

## 9. Impacto público e sustentabilidade

**Impacto público.** Menos viagens perdidas; menos filas formadas por falta de informação; uso mais racional do horário de pico; melhor experiência para idosos e trabalhadores; apoio à inclusão digital via canal que a população já domina.

**Sustentabilidade.** Caminhos possíveis, sem promessas de números:

- parceria com órgãos públicos e consórcios municipais para custeio e uso da base;
- versão institucional para prefeituras e postos de atendimento;
- patrocínio/apoio de programas de inovação e governança pública;
- projeto de extensão acadêmica como origem e prova de conceito, evoluindo para produto.

O modelo precisa ser **de interesse público**, com dados abertos e sem monetização sobre a vulnerabilidade do cidadão.

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede |
| --- | --- |
| % de usuários que chegaram com a documentação completa | Eficácia do checklist |
| Redução de viagens repetidas por mesmo serviço | Impacto direto na dor principal |
| Erro médio entre tempo estimado e tempo real | Qualidade da previsão de fila |
| Tempo médio economizado por atendimento | Benefício percebido |
| Taxa de uso de horário fora de pico | Melhoria de distribuição da fila |
| Retenção e reuso (consulta por serviço) | Utilidade recorrente |
| Cobertura de serviços e órgãos mapeados | Escopo da base |
| NPS / satisfação do cidadão | Percepção geral |

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Informação de documentos desatualizada | Alto | Revisão periódica, fonte oficial, aviso "confirme no órgão" |
| Estimativa de fila imprecisa | Alto | Exibir faixas, não números exatos; revisar com dados reais |
| Órgão não divulgar dados | Médio | Começar com dados públicos + contribuição agregada |
| Baixa adesão inicial dos cidadãos | Médio | Entrada pelo WhatsApp, serviços de maior demanda |
| Dependência de parceria institucional | Médio | Piloto independente antes de escalar |
| Uso indevido de dados pessoais | Alto | LGPD desde o MVP: minimização, agregação, consentimento |
| Confundir o app com canal oficial | Médio | Identidade clara de orientação, não de atendimento |

## 12. Roadmap de sprints

| Sprint | Nome | Entregáveis |
| --- | --- | --- |
| 0 | Fundação | Estrutura do app de coleta e do projeto; definição do perfil (exceção) |
| 1 | Perguntas | Implementação das 20 perguntas em escala de 1 a 5 |
| 2 | Código + planilha | Geração do código `G2-<nnn>` e integração com a planilha de respostas |
| 3 | Campo + correlação | Coleta em campo (meta de 20 respostas) e leitura de correlações |
| 4 | Análise | Cruzamento dos blocos, leitura da hipótese e dos áudios |
| 5 | Refino final | Ajustes, consolidação e apresentação do resultado |

## 13. Como o formulário valida a hipótese (blocos + áudio)

**Regras do app de coleta**

- **Bloco 0 — Perfil:** exceção, identificado por observação, com dados gerais do respondente (sem ser uma das 20 perguntas).
- **20 perguntas:** marcadas de **1 a 5**, onde **1 = um polo e 5 = o oposto**. Escala fechada, comparável.
- **Não há respostas abertas** no formulário.
- **Falas do cidadão:** vão para um **áudio no WhatsApp que começa com o código `G2-<nnn>`**, ligando a narrativa à resposta registrada.

**Blocos das 20 perguntas**

| Bloco | Perguntas | O que investiga |
| --- | --- | --- |
| 1 | Q1–Q5 | Acesso a órgãos e filas |
| 2 | Q6–Q10 | Documentos e informação |
| 3 | Q11–Q14 | Impacto: tempo, dia de trabalho, frustração |
| 4 | Q15–Q20 | Solução digital: documentos, tempo de fila, agendamento, acompanhamento |

**Como isso valida a hipótese.** A hipótese é: *a maior dor é o tempo de fila, e muitos já perderam uma viagem por não saber quais documentos levar.* O bloco 1 mede a percepção de fila; o bloco 3 quantifica o impacto (tempo, trabalho, frustração); o bloco 2 mostra o peso da falta de informação sobre documentos. Se o bloco 3 e a falta de documento no bloco 2 aparecerem como os pontos mais críticos, a hipótese se confirma — e o bloco 4 indica qual solução o cidadão prioriza (documentos, fila, agendamento ou acompanhamento). O áudio com o código `G2-<nnn>` dá o contexto humano que a escala 1–5 não captura.

## 14. Pitch de 30 segundos

"Você já perdeu uma manhã de trabalho numa fila do INSS por causa de um papel que faltava? O Fila Cidadã resolve isso. Antes de sair de casa, o cidadão descobre quais documentos levar, em qual órgão ou posto ir e quanto tempo provavelmente vai esperar na fila — tudo pelo WhatsApp, sem instalar nada. Menos viagem perdida, menos fila desnecessária e mais tempo de volta para o cidadão. Simples, público e feito para quem mais precisa."
