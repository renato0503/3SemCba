# Pesquisa e Dados — Grupo 4 · CRAS Online
> Apoio à defesa da ideia: dados/notícias reais (Brasil) + 12 artigos peer-reviewed (2021–2026). Metadados dos papers vêm de OpenAlex/Crossref; números têm fonte com link. Nada foi inventado; o não confirmado está marcado `[verificar]`.

**Grupo:** 4 · CRAS Online · **Professor:** Renato · **Integrantes:** Anna, Maria Eduarda, Marcelly, Kaique · **Código:** G4-<nnn> · **Meta:** 15–20

**Hipótese de campo:** Poucas pessoas conhecem o CRAS e há desconfiança em enviar documentos por aplicativo, mesmo quando reconhecem a dor de resolver serviços socioassistenciais presencialmente.

---

## 1. Resumo executivo

O "CRAS no bolso" parte de uma escala concreta: o Brasil tem dezenas de milhões de famílias inscritas no CadÚnico e cerca de 20 milhões recebendo Bolsa Família, mas a rede que atende essa população é finita. São pouco mais de 8 mil unidades de CRAS, presentes em quase todos os municípios, e em 2024 elas somaram cerca de 40 milhões de atendimentos. Só no Distrito Federal foram 485,7 mil atendimentos em 2024, dos quais 155,7 mil ocorreram apenas na recepção, sem agendamento prévio: ou seja, uma parcela enorme do trabalho é gente indo ao balcão para informação básica e orientação, exatamente o tipo de demanda que pode ser antecipada por um canal digital.

Ao mesmo tempo, o gov.br já tem 166 milhões de contas (175 milhões em março de 2026), o que mostra que a base de identidade digital necessária para autenticar um serviço público já está posta. O problema não é "falta de login", é inclusão e confiança. A TIC Domicílios 2024 (Cetic.br) mostra 29 milhões de não usuários de internet, 16 milhões deles nas classes DE; a internet está em 100% dos domicílios de classe A, contra 68% das classes DE. E apenas 18% dos usuários com Ensino Fundamental sabem alterar configurações de privacidade, contra 58% com Ensino Superior.

A literatura dos últimos cinco anos confirma o diagnóstico: digitalizar serviços sociais amplia eficiência, mas cria novas barreiras para quem tem menos letramento digital (Sung; Lee, 2024; Morte-Nadal; Esteban Navarro, 2025), pode perder a dimensão humana da orientação (Considine et al., 2022; Ball et al., 2023) e depende de confiança e de apoio presencial/humano para funcionar com público vulnerável (Lindgren; Madsen, 2025; Wihlborg; Iacobaeus, 2023; Singh, 2024). É exatamente aí que o app entra: digitalizar o que é repetitivo e agendar o que precisa de escuta, sem tirar o CRAS da vida do cidadão.

---

## 2. Dados e notícias reais (Brasil)

### 2.1 Tabela de dados

| Dado | Número | Ano | Fonte |
|---|---|---|---|
| Famílias inscritas no Cadastro Único (CadÚnico) | 40.652.068 famílias | 2025 (jan) | MDS, CadInsan 2025 ([gov.br/mds](https://www.gov.br/mds/pt-br/Sisan/vigilancia-do-sisan/documento-cadinsan/cadinsan-2025.pdf)) |
| Famílias beneficiárias do Bolsa Família | 20,56 milhões de famílias | 2025 (fev) | MDS / Agência Gov ([agenciagov.ebc.com.br](https://agenciagov.ebc.com.br/noticias/202502/bolsa-familia-chega-a-mais-de-20-5-milhoes-de-familias-a-partir-desta-segunda-17)) |
| Pessoas alcançadas pelo Bolsa Família | quase 54 milhões de pessoas | 2025 (fev) | MDS / Agência Gov ([agenciagov.ebc.com.br](https://agenciagov.ebc.com.br/noticias/202502/bolsa-familia-chega-a-mais-de-20-5-milhoes-de-familias-a-partir-desta-segunda-17)) |
| Unidades de CRAS no país | mais de 8 mil centros | 2024 | MDS / Censo SUAS, via Brasil 61 ([brasil61.com](https://brasil61.com/n/cras-porta-de-entrada-do-suas-garante-acesso-a-assistencia-social-em-todo-o-brasil-bras2615744)) |
| Presença do SUAS nos municípios | cerca de 99% dos municípios com ao menos um CRAS | 2024 | MDS / Censo SUAS, via Brasil 61 ([brasil61.com](https://brasil61.com/n/cras-porta-de-entrada-do-suas-garante-acesso-a-assistencia-social-em-todo-o-brasil-bras2615744)) |
| Atendimentos realizados nos CRAS | cerca de 40 milhões de atendimentos | 2024 | MDS, via Brasil 61 ([brasil61.com](https://brasil61.com/n/cras-porta-de-entrada-do-suas-garante-acesso-a-assistencia-social-em-todo-o-brasil-bras2615744)) |
| Atendimentos mensais nos CRAS (RMA) | 3.393.518 atendimentos em outubro | 2024 | MDS/SNAS, RMA Série Histórica ([aplicacoes.cidadania.gov.br](https://aplicacoes.cidadania.gov.br/vis/data3/v.php?q%5B%5D=oNOhlMHqwGZsemeZ6au8srNei5Gvm7mlxve6ma%2FEsbb1qQ%3D%3D)) |
| Atendimentos no CRAS do DF, sendo 155.738 só na recepção e sem agendamento | 485.700 atendimentos no total | 2024 | Sedes-DF ([sedes.df.gov.br](https://www.sedes.df.gov.br/w/mais-de-155-mil-familias-vulneraveis-foram-atendidas-nas-recepcoes-do-cras-em-2024)) |
| Usuários cadastrados no gov.br | 166 milhões de contas | 2025 (abr) | MGI, via Folha ([folha.uol.com.br](https://www1.folha.uol.com.br/colunas/ronaldolemos/2025/04/govbr-chega-a-166-milhoes-de-usuarios-sob-ataque.shtml)) |
| Pessoas sem acesso à internet no Brasil | 29 milhões de não usuários, 16 milhões nas classes DE | 2024 | Cetic.br, TIC Domicílios 2024 ([cetic.br](http://cetic.br/pt/noticia/em-duas-decadas-proporcao-de-lares-urbanos-brasileiros-com-internet-passou-de-13-para-85-aponta-tic-domicilios-2024)) |
| Uso de governo eletrônico (16 anos ou mais) | 61% dos usuários de internet usaram algum serviço | 2024 | Cetic.br, TIC Domicílios 2024 ([resumo executivo](https://cetic.br/media/docs/publicacoes/2/20250512115624/tic_domicilios_2024_resumo_executivo.pdf)) |

Dado complementar de confiança/letramento: alterar configurações de privacidade é relatado por 58% dos usuários com Ensino Superior e por apenas 18% dos que têm Ensino Fundamental (TIC Domicílios 2024, [cetic.br](http://cetic.br/pt/noticia/em-duas-decadas-proporcao-de-lares-urbanos-brasileiros-com-internet-passou-de-13-para-85-aponta-tic-domicilios-2024)).

### 2.2 Leitura dos dados

1. **A demanda é gigante e o balcão continua sendo a porta.** Dezenas de milhões de famílias no CadÚnico e cerca de 20 milhões no Bolsa Família contrastam com pouco mais de 8 mil CRAS. Em 2024 a rede fez cerca de 40 milhões de atendimentos, e o RMA de outubro/2024 sozinho registrou 3,39 milhões. A conta não fecha só com mais prédio: precisa reduzir atendimento repetitivo.

2. **A fila presencial é, em boa parte, informação e agendamento.** No DF, 155.738 dos 485.700 atendimentos de 2024 aconteceram na recepção, "sem agendamento prévio", para informação básica e casos urgentes. Isso é o alvo direto de um app que orienta, agenda e acompanha o pedido antes de a pessoa sair de casa.

3. **A infraestrutura de identidade já existe.** Com 166 milhões de contas em 2025 (e 175 milhões em março de 2026, segundo o próprio gov.br), usar login gov.br para autenticar o pedido no CRAS não cria uma barreira nova, aproveita o que o cidadão já usa. Em 2025, 130,6 milhões de brasileiros usaram serviços digitais no gov.br, com 3,5 bilhões de autenticações ([Valor/MGI](https://valor.globo.com/brasil/noticia/2025/09/18/mais-de-130-milhoes-de-brasileiros-utilizaram-servicos-digitais-do-govbr-em-2025.ghtml)).

4. **O gargalo é inclusão e confiança, não conectividade bruta.** 29 milhões de pessoas ainda estão fora da internet e 16 milhões delas são das classes DE. A internet chega a 100% dos lares de classe A e a 68% dos lares DE. Some-se a isso a baixa habilidade de privacidade entre quem tem menos escolaridade (18% contra 58%). A hipótese de campo ("desconfiança em enviar documentos por app") tem base empírica.

5. **Governo eletrônico cresce, mas a assistência fica atrás.** 61% dos usuários de internet usaram serviços de governo eletrônico em 2024, principalmente saúde (32%) e documentos (31%). Serviços ligados a trabalho e previdência caíram de 33% (2023) para 25% (2024). Existe espaço para serviços socioassistenciais ocuparem esse lugar de forma confiável.

6. **O desenho tem que ser "digital com apoio humano".** Os dados mostram um público que usa muito o celular, mas com letramento desigual. Isso favorece um app simples, com selo de verificação, linguagem clara e um canal humano de apoio (telefone/CRAS) para quem travar, em vez de um sistema 100% autosserviço.

---

## 3. Referencial científico (12 artigos, 2021–2026)

Todos os itens são artigos peer-reviewed (tipo `article`/`journal-article`), 2021 a 2026, com metadados do OpenAlex e DOI conferido na Crossref. Acesso "aberto" ou "fechado" vem do campo de Open Access do OpenAlex.

### 3.1 Síntese em blocos

**Bloco A. Digitalizar o social: eficiência com risco de exclusão.** A literatura sobre o "Estado de bem-estar digital" mostra que a automação melhora eficiência, mas pode excluir quem mais precisa. Considine et al. (2022) e Ball et al. (2023) estudam a digitalização do welfare-to-work e alertam que o algoritmo não substitui o julgamento humano de quem atende; Larasati et al. (2022) sintetizam riscos de discriminação e desigualdade; Larsson e Haldar (2021) mostram que sistemas proativos ainda encontram obstáculos com cidadãos de baixa familiaridade digital.

**Bloco B. Quem fica de fora e por quê.** Sung e Lee (2024) acompanham longitudinalmente o uso de e-gov por cidadãos vulneráveis na Coreia e mostram que o "divide" persiste mesmo com difusão da tecnologia. Morte-Nadal e Esteban Navarro (2025) mapeiam barreiras de inclusão digital nos serviços públicos europeus e recomendam ações específicas para grupos vulneráveis. Lopes e Leal (2024) trazem o caso brasileiro de mulheres quilombolas e mostram que a desconexão vira violação de direitos.

**Bloco C. Confiança, privacidade e identidade.** Paguay-Chimarro et al. (2025) analisam riscos de privacidade em 21 instituições de e-gov e mostram que transparência e exposição de dados andam juntas. Alanoca et al. (2021) discutem governança para gerar confiança em apps de governo na América Latina, tema direto para o "temor de golpe". Ziller et al. (2025) medem experimentalmente a disposição de compartilhar dados pessoais e o peso da influência social.

**Bloco D. O fator humano e os canais.** Lindgren e Madsen (2025) mostram que muita gente ainda prefere canais tradicionais para pedir benefícios, mesmo com autosserviço digital disponível. Wihlborg e Iacobaeus (2023) e Singh (2024) evidenciam o papel dos intermediários e do apoio no balcão para incluir digitalmente quem tem menos habilidade. É a justificativa direta para o app ter "apoio humano" e não só formulário.

### 3.2 Os 12 artigos

**1. Sung; Lee (2024).** A longitudinal study on the diffusion and the divide in the use of e-government services among vulnerable citizens in Korea. *Government Information Quarterly*. DOI: 10.1016/j.giq.2024.101938. Citações: 21. Acesso: fechado.
- **O que sustenta:** acompanha ao longo do tempo como cidadãos vulneráveis usam (ou não) serviços de governo digital, mostrando que a difusão da tecnologia não elimina sozinha a desigualdade de uso.
- **Como usar na defesa:** argumento central de que "ter internet e ter conta não basta". O app precisa de desenho e apoio específicos para público de baixa renda e baixa familiaridade digital.

**2. Morte-Nadal; Esteban Navarro (2025).** Recommendations for digital inclusion in the use of European digital public services. *Humanities and Social Sciences Communications*. DOI: 10.1057/s41599-025-04576-7. Citações: 26. Acesso: aberto.
- **O que sustenta:** revisão sistemática mais entrevistas e survey sobre barreiras de adoção de serviços públicos digitais por grupos vulneráveis, com recomendações de inclusão.
- **Como usar na defesa:** usar as recomendações como checklist de acessibilidade do CRAS Online (linguagem simples, múltiplos canais, suporte).

**3. Considine; McGann; Ball; Nguyen (2022).** Can Robots Understand Welfare? Exploring Machine Bureaucracies in Welfare-to-Work. *Journal of Social Policy*. DOI: 10.1017/s0047279422000174. Citações: 61. Acesso: aberto.
- **O que sustenta:** defende que a discricionariedade do atendente de linha de frente importa e que a automação total pode piorar o acesso.
- **Como usar na defesa:** justificar por que o app digitaliza o repetitivo e escala o caso complexo para o atendimento humano no CRAS.

**4. Ball; McGann; Nguyen; Considine (2023).** Emerging modes of digitalisation in the delivery of welfare-to-work: Implications for street-level discretion. *Social Policy and Administration*. DOI: 10.1111/spol.12939. Citações: 36. Acesso: aberto.
- **O que sustenta:** distingue tipos de digitalização e mostra que cada um afeta de modo diferente o acesso do cidadão e o papel do atendente.
- **Como usar na defesa:** definir o CRAS Online como "digitalização de apoio" (orienta e agenda), e não como substituição do atendimento.

**5. Larasati; Yuda; Syafa'at (2022).** Digital welfare state and problem arising: an exploration and future research agenda. *International Journal of Sociology and Social Policy*. DOI: 10.1108/ijssp-05-2022-0122. Citações: 26. Acesso: fechado.
- **O que sustenta:** revisa experiências de Índia, Quênia e Suécia e sistematiza riscos de discriminação, exclusão e desigualdade na entrega automatizada de benefícios.
- **Como usar na defesa:** antecipar riscos e mostrar salvaguardas (revisão humana, direito a recurso, canal presencial).

**6. Lindgren; Madsen (2025).** Digital First? Understanding Citizens' Communication Needs in Digital Public Encounters. *Social Policy and Administration*. DOI: 10.1111/spol.70017. Citações: 5. Acesso: aberto.
- **O que sustenta:** mostra que, para pedir benefícios, muitos cidadãos ainda preferem canais tradicionais, e propõe analisar o comportamento de canal ao longo de todo o atendimento.
- **Como usar na defesa:** defender o modelo híbrido (app como opção, nunca como única porta) e o agendamento como ponte para o presencial.

**7. Wihlborg; Iacobaeus (2023).** Context matters—different entrepreneurial approaches among street-level bureaucrats enhancing digital inclusion. *European Policy Analysis*. DOI: 10.1002/epa2.1197. Citações: 12. Acesso: aberto.
- **O que sustenta:** analisa como servidores de linha de frente criam práticas para incluir digitalmente quem não tem acesso ou habilidade.
- **Como usar na defesa:** basear o "apoio humano" do app no que os próprios atendentes do CRAS já fazem, com treinamento e papel definido.

**8. Singh (2024).** Intermediaries as infrastructure: Interrogating the phatic labor of state-building. *Journal of Sociology*. DOI: 10.1177/14407833241234675. Citações: 8. Acesso: fechado.
- **O que sustenta:** etnografia sobre intermediários que ajudam cidadãos a navegar a burocracia (caso Aadhaar, na Índia) e mostra que eles são infraestrutura invisível do Estado digital.
- **Como usar na defesa:** reconhecer que muita gente depende de um "ajudante" (parente, vizinho, CRAS) e transformar o app em ferramenta que facilita essa intermediação, não em barreira.

**9. Lopes; Leal (2024).** Quilombola women confronting digital discrimination in Brazil. *The International Journal of Information, Diversity & Inclusion (IJIDI)*. DOI: 10.33137/ijidi.v8i2.43500. Citações: 3. Acesso: aberto.
- **O que sustenta:** pesquisa brasileira com 41 lideranças de comunidades quilombolas em Minas Gerais mostra que a falta de acesso a TIC se converte em violação de direitos.
- **Como usar na defesa:** evidência nacional de exclusão digital de público vulnerável; sustenta a necessidade de canal off-line e de busca ativa.

**10. Paguay-Chimarro; Cevallos-Salas; Rodríguez-Hoyos; Estrada-Jiménez (2025).** Transparency Unleashed: Privacy Risks in the Age of E-Government. *Informatics*. DOI: 10.3390/informatics12020039. Citações: 5. Acesso: aberto.
- **O que sustenta:** analisa riscos de privacidade em 21 instituições públicas que operam e-gov e mostra que transparência e exposição de dados pessoais caminham juntas.
- **Como usar na defesa:** embasa o "selo verificado" e as regras de minimização de dados e LGPD como resposta ao medo de golpe.

**11. Alanoca; Guetta-Jeanrenaud; Ferrari; Weinberg et al. (2021).** Digital contact tracing against COVID-19: a governance framework to build trust. *International Data Privacy Law*. DOI: 10.1093/idpl/ipab001. Citações: 11. Acesso: aberto.
- **O que sustenta:** discute governança de apps de governo na América Latina e mostra que confiança depende de propósito claro, proteção de dados e prestação de contas.
- **Como usar na defesa:** lista de princípios de confiança a aplicar no CRAS Online (dizer para que servem os dados, quem acessa e como recorrer).

**12. Ziller; Loepp; Kindermann; Köchling et al. (2025).** Willingness to share personal data online: The role of social influence and sustainability. *Technology in Society*. DOI: 10.1016/j.techsoc.2025.102974. Citações: 10. Acesso: aberto.
- **O que sustenta:** experimento de survey em larga escala mostra que a disposição de compartilhar dados pessoais é desigual e sofre influência social.
- **Como usar na defesa:** reforça que a adesão ao app depende de confiança transmitida (verificação oficial, recomendação do CRAS, testemunho de vizinhos).

### 3.3 Quadro-resumo

| # | Autor(es) | Ano | Título (curto) | Periódico | DOI | Citações |
|---|---|---|---|---|---|---|
| 1 | Sung; Lee | 2024 | E-government divide among vulnerable citizens (Korea) | Government Information Quarterly | 10.1016/j.giq.2024.101938 | 21 |
| 2 | Morte-Nadal; Esteban Navarro | 2025 | Digital inclusion in European digital public services | Humanities and Social Sciences Communications | 10.1057/s41599-025-04576-7 | 26 |
| 3 | Considine; McGann; Ball; Nguyen | 2022 | Can Robots Understand Welfare? | Journal of Social Policy | 10.1017/s0047279422000174 | 61 |
| 4 | Ball; McGann; Nguyen; Considine | 2023 | Digitalisation in welfare-to-work and discretion | Social Policy and Administration | 10.1111/spol.12939 | 36 |
| 5 | Larasati; Yuda; Syafa'at | 2022 | Digital welfare state and problem arising | International Journal of Sociology and Social Policy | 10.1108/ijssp-05-2022-0122 | 26 |
| 6 | Lindgren; Madsen | 2025 | Digital First? Citizens' communication needs | Social Policy and Administration | 10.1111/spol.70017 | 5 |
| 7 | Wihlborg; Iacobaeus | 2023 | Street-level bureaucrats enhancing digital inclusion | European Policy Analysis | 10.1002/epa2.1197 | 12 |
| 8 | Singh | 2024 | Intermediaries as infrastructure | Journal of Sociology | 10.1177/14407833241234675 | 8 |
| 9 | Lopes; Leal | 2024 | Quilombola women confronting digital discrimination (Brazil) | International Journal of Information, Diversity & Inclusion | 10.33137/ijidi.v8i2.43500 | 3 |
| 10 | Paguay-Chimarro; Cevallos-Salas; Rodríguez-Hoyos; Estrada-Jiménez | 2025 | Privacy risks in the age of e-government | Informatics | 10.3390/informatics12020039 | 5 |
| 11 | Alanoca; Guetta-Jeanrenaud; Ferrari; Weinberg et al. | 2021 | Governance to build trust in gov apps (Latin America) | International Data Privacy Law | 10.1093/idpl/ipab001 | 11 |
| 12 | Ziller; Loepp; Kindermann; Köchling et al. | 2025 | Willingness to share personal data online | Technology in Society | 10.1016/j.techsoc.2025.102974 | 10 |

---

## 4. Como usar isso na defesa (argumentos prontos)

1. **Escala do problema (dado).** São mais de 8 mil CRAS e cerca de 40 milhões de atendimentos em 2024 para uma base de 20 milhões de famílias no Bolsa Família. É volume que justifica um canal digital de triagem e agendamento.

2. **Fila que dá para evitar (dado).** No DF, 155.738 dos 485.700 atendimentos de 2024 foram na recepção sem agendamento. Boa parte era informação e orientação: é o que o app resolve antes da pessoa sair de casa.

3. **Login já existe (dado).** 166 milhões de contas no gov.br em 2025. Não estamos pedindo ao cidadão uma senha nova, e sim reaproveitando a identidade digital que ele já tem.

4. **O medo tem base (dado + paper 10 e 11).** Só 18% dos usuários com Ensino Fundamental mexem em configurações de privacidade, e Paguay-Chimarro et al. (2025) mostram riscos reais de exposição de dados em e-gov. Resposta: selo verificado, linguagem clara sobre uso dos dados e canal de recurso (Alanoca et al., 2021).

5. **Digital tem que ter apoio humano (papers 3, 6, 7 e 8).** Considine et al. (2022) e Ball et al. (2023) mostram os limites da automação; Lindgren e Madsen (2025) mostram que muita gente ainda prefere o canal tradicional; Wihlborg e Iacobaeus (2023) e Singh (2024) mostram o papel dos atendentes e intermediários. Conclusão: o CRAS Online acelera o simples e mantém o humano no complexo.

6. **Inclusão não é só acesso (papers 1, 2 e 9).** Sung e Lee (2024) e Morte-Nadal e Esteban Navarro (2025) provam que difusão de internet não elimina o "divide", e Lopes e Leal (2024) mostram isso no Brasil. Conclusão: prever canal off-line, busca ativa e letramento digital dentro do projeto.

7. **Riscos a declarar de frente (papers 5 e 12).** Larasati et al. (2022) listam exclusão e discriminação como riscos do Estado digital; Ziller et al. (2025) mostram que a adesão depende de confiança. Conclusão: política de uso de dados, revisão humana das decisões e transparência desde o MVP.

8. **Hipótese de campo testável.** As 20 perguntas em escala 1 a 5 (Bloco 0 por observação) medem exatamente familiaridade com o CRAS, dor do presencial e confiança em enviar documentos por app. Os dados e papers acima são o "chão" para comparar o que a pesquisa de campo encontrar.

---

## 5. Lacunas, limites e cuidados

- **Sem paper específico sobre CRAS/app brasileiro.** A busca no OpenAlex não retornou artigo peer-reviewed diretamente sobre aplicativo de CRAS ou do SUAS. O referencial foi montado com a literatura equivalente (digitalização de bem-estar, inclusão digital, confiança e privacidade em e-gov) e com o caso brasileiro de exclusão digital (Lopes; Leal, 2024). Marcar isso na apresentação como frente de pesquisa futura.
- **Números do CadÚnico incluem cadastros desatualizados.** O total de 40,65 milhões inclui famílias com cadastro vencido; em janeiro de 2025, 21,46 milhões (52,8%) tinham atualização nos últimos 12 meses (CadInsan 2025). Usar a nuance, não o número bruto isolado.
- **"40 milhões de atendimentos" e "mais de 8 mil CRAS" vêm de nota de imprensa citando o MDS.** Preferir o RMA (dado oficial mensal, 3,39 milhões em out/2024) quando precisar de série auditável.
- **gov.br em 166 milhões (2025) é conta cadastrada, não uso ativo.** O uso efetivo é menor (130,6 milhões de pessoas usaram serviços em 2025), então tratar as duas métricas separadamente.
- **TIC Domicílios é amostra (23.856 domicílios em 2024).** Números são estimativas com margem de erro; citar a fonte (Cetic.br/NIC.br) sempre.
- **Citação do Google Forms/ContextoApp.** A hipótese e as personas do grupo devem dialogar com os dados; não substituir o dado real por achismo na apresentação.
- **Acesso fechado a 3 dos 12 papers** (Sung; Lee 2024; Larasati et al. 2022; Singh 2024): para a defesa, usar título, resumo e as ideias centrais, sem copiar trechos protegidos.

---

## 6. Fontes e proveniência

**Termos de busca OpenAlex (campo `title_and_abstract`, filtro `type:article`, 2021-01-01 a 2026-12-31, ordenado por relevância, retry em HTTP 429):**
1. "social assistance digitalization welfare services" (21 resultados)
2. "digital inclusion low income e-government" (10 resultados)
3. "trust privacy personal data public services" (25 resultados)
4. "welfare service delivery digital citizen" (15 resultados)
5. "e-government adoption vulnerable citizens digital divide" (2 resultados)
6. "social protection digital identification beneficiaries" (4 resultados)
7. "digital government citizen adoption Brazil" (4 resultados)
8. "social work digital technology Brazil" (25 resultados)
9. "Bolsa Familia conditional cash transfer digital Brazil" (0 resultados)

**Arquivos brutos salvos em `_pesquisa/saidas/`:** `G4_social_assistance_digitalization.{md,json}`, `G4_digital_inclusion_low_income.{md,json}`, `G4_trust_privacy_public_services.{md,json}`, `G4_welfare_service_delivery.{md,json}`, `G4_egov_vulnerable_adoption.{md,json}`, `G4_social_protection_digital_id.{md,json}`, `G4_digital_government_brazil.{md,json}`, `G4_social_work_brasil.{md,json}`, `G4_bolsa_familia_brasil.{md,json}`.

**Ferramenta:** `_pesquisa/openalex_busca.py` (OpenAlex + saúde de DOI conferida na Crossref). Os 12 DOIs desta seção foram conferidos individualmente na API do Crossref (todos retornaram `journal-article` com ano e periódico compatíveis).

**Fontes dos dados brasileiros:**
- MDS, CadInsan 2025: https://www.gov.br/mds/pt-br/Sisan/vigilancia-do-sisan/documento-cadinsan/cadinsan-2025.pdf
- MDS / Agência Gov (Bolsa Família, fev/2025): https://agenciagov.ebc.com.br/noticias/202502/bolsa-familia-chega-a-mais-de-20-5-milhoes-de-familias-a-partir-desta-segunda-17
- Brasil 61 (CRAS/SUAS, dados MDS): https://brasil61.com/n/cras-porta-de-entrada-do-suas-garante-acesso-a-assistencia-social-em-todo-o-brasil-bras2615744
- MDS/SNAS, RMA Série Histórica (VIS): https://aplicacoes.cidadania.gov.br/vis/data3/v.php?q%5B%5D=oNOhlMHqwGZsemeZ6au8srNei5Gvm7mlxve6ma%2FEsbb1qQ%3D%3D
- Sedes-DF (atendimentos CRAS DF 2024): https://www.sedes.df.gov.br/w/mais-de-155-mil-familias-vulneraveis-foram-atendidas-nas-recepcoes-do-cras-em-2024
- Folha (gov.br 166 milhões, MGI): https://www1.folha.uol.com.br/colunas/ronaldolemos/2025/04/govbr-chega-a-166-milhoes-de-usuarios-sob-ataque.shtml
- Valor/MGI (130,6 milhões usaram serviços digitais em 2025): https://valor.globo.com/brasil/noticia/2025/09/18/mais-de-130-milhoes-de-brasileiros-utilizaram-servicos-digitais-do-govbr-em-2025.ghtml
- Cetic.br, TIC Domicílios 2024 (notícia): http://cetic.br/pt/noticia/em-duas-decadas-proporcao-de-lares-urbanos-brasileiros-com-internet-passou-de-13-para-85-aponta-tic-domicilios-2024
- Cetic.br, TIC Domicílios 2024 (resumo executivo): https://cetic.br/media/docs/publicacoes/2/20250512115624/tic_domicilios_2024_resumo_executivo.pdf

**Observação de proveniência:** títulos, autores, ano, periódico, DOI, contagem de citações e status de acesso aberto são exatamente os devolvidos pela API (OpenAlex) e reconferidos na Crossref. Nenhum número, DOI, autor ou link foi criado manualmente.
