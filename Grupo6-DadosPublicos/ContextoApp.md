# Contexto do App — Grupo 6 · Dados Públicos

**Professor:** Prof. Pantalião
**Integrantes:** Erilin · Emilly · Juarez · Flavia
**Código de coleta:** `G6-<nnn>` · **Formulário:** 20 perguntas · **Meta:** 15–20 respostas
**Tema político:** nunca perguntar em quem vota nem citar partidos — o foco é entender os dados.

---

## 1. Pitch em uma frase

Transformamos dados públicos abertos em linguagem simples e comparável, para que qualquer cidadão consiga decidir sobre candidatos e agentes de cargos políticos sem ser especialista em orçamento.

---

## 2. O problema e a oportunidade (dados abertos x uso real)

Há uma distância entre a existência do dado e o uso real dele. Os dados públicos estão disponíveis em portais oficiais, mas são publicados em formatos técnicos, dispersos entre vários órgãos e escritos numa linguagem administrativa que exige conhecimento prévio.

**O problema:** os dados abertos existem, mas são complexos e pouco usados na hora de decidir o voto.
**A oportunidade:** a mesma base pública já disponível pode ser traduzida, contextualizada e comparada, gerando uma camada de leitura que o cidadão comum consegue entender em segundos.

| Dimensão | Situação atual | Oportunidade |
|---|---|---|
| Disponibilidade | Dado publicado em portais oficiais | Base já existe, não precisa ser criada |
| Formato | Tabelas, CSV, PDF, planilhas | Converter em ficha e resumo visual |
| Linguagem | Técnica, orçamentária, jurídica | Traduzir para o português do dia a dia |
| Comparação | Cada órgão com sua estrutura | Padronizar por candidato e por cargo |
| Uso | Baixo e concentrado em especialistas | Ampliar para o eleitor comum |

A hipótese central é que o obstáculo não é a falta de dado, e sim a falta de tradução. Se essa leitura simplificada resolver a barreira, o dado público deixa de ser um arquivo consultado por poucos e passa a ser uma ferramenta de decisão usada por muitos.

---

## 3. Público e personas

O público é o cidadão eleitor em geral, com níveis diferentes de tempo, interesse e repertório técnico. Três personas representam a faixa de uso do produto.

**Persona 1 — Eleitor comum ("Ana, 34 anos, comerciária"):** vota, comenta política no grupo da família, mas nunca abriu um Portal da Transparência. Quer uma resposta direta: "esse candidato fez o que prometeu?". Precisa de ficha curta, linguagem simples e zero burocracia.

**Persona 2 — Fiscal cidadão ("Carlos, 52 anos, aposentado e assíduo em conselhos locais"):** já conhece a LAI e cobra prestação de contas. Quer comparar, cruzar e acompanhar a evolução ao longo do mandato. Precisa de histórico, filtros e alertas.

**Persona 3 — Jornalista ("Renata, 29 anos, repórter de cidade"):** trabalha com dados, mas contra prazos curtos. Quer checar rápido um número, contextualizar uma denúncia e citar a fonte oficial. Precisa de rastreabilidade, links para a origem e resumo exportável.

| Persona | Dor principal | O que o app entrega |
|---|---|---|
| Eleitor comum | Acha os dados complicados demais | Ficha simples e resumo em linguagem clara |
| Fiscal cidadão | Perde tempo pulando entre portais | Comparador, histórico e alertas |
| Jornalista | Prazo curto para checar dado | Fonte oficial, data e exportação rápida |

---

## 4. Proposta de valor (mini canvas)

| Bloco | Conteúdo |
|---|---|
| Problema | Dados públicos existem, mas são complexos e pouco usados na decisão do voto |
| Segmentos | Eleitor comum, fiscal cidadão, jornalista |
| Proposta de valor | Traduzir dados oficiais em informação clara, comparável e neutra |
| Canais | Aplicativo web/mobile, compartilhamento por link e redes |
| Relação | Leitura em segundos, sem cadastro obrigatório, com fonte sempre visível |
| Recursos-chave | Base oficial integrada, motor de tradução de linguagem, comparador |
| Atividades-chave | Coletar de fontes oficiais, padronizar, resumir, checar e publicar |
| Parcerias | Órgãos públicos detentores dos dados, instituições de ensino, imprensa |
| Custos | Integração e manutenção da base, curadoria, infraestrutura, LGPD |
| Receitas | Financiamento público/edital, apoio institucional, versões para imprensa e conselhos |

---

## 5. Jornada do usuário (do interesse ao voto informado)

1. **Motivação:** o cidadão ouve falar de gastos, emendas ou obras e quer entender melhor.
2. **Descoberta:** encontra o app num link compartilhado, numa busca ou por indicação.
3. **Identificação:** busca o candidato ou agente pelo nome e pelo cargo.
4. **Leitura simples:** vê a ficha com resumo em linguagem clara e indicadores visuais.
5. **Comparação:** coloca lado a lado dois ou mais candidatos e observa diferenças.
6. **Aprofundamento:** clica na fonte oficial para conferir o dado na origem.
7. **Acompanhamento:** ativa alertas para novas informações e mudanças de mandato.
8. **Decisão:** usa a leitura traduzida como insumo, junto com seus próprios critérios, para um voto informado.
9. **Retorno:** compartilha o comparador e contribui com dúvidas que alimentam novas melhorias.

O ponto de virada da jornada é o passo 4: se a ficha não for entendida em segundos, o usuário abandona. Todo o desenho do produto é otimizado para essa primeira leitura.

---

## 6. Funcionalidades — tabela MVP | v1 | v2

| Funcionalidade | MVP | v1 | v2 |
|---|---|---|---|
| Ficha simples do candidato | Simples, dados essenciais | Completa, com histórico | Personalizável pelo usuário |
| Resumo em linguagem clara | Texto curto e visual | Resumo por tema (orçamento, emendas) | Resumo gerado e revisado por curadoria |
| Comparador | Dois candidatos, poucos indicadores | Múltiplos candidatos e filtros | Comparador por cargo e por período |
| Fonte oficial e data | Link para a origem do dado | Vários portais integrados | Trilha de auditoria completa |
| Alertas | Não | Alertas por candidato | Alertas por tema, obra e emenda |
| Busca | Por nome | Por nome, cargo e região | Busca semântica por tema |
| Exportação | Não | Link do comparador | Exportação para imprensa e conselhos |

Critério de MVP: provar que uma ficha simples e um comparador básico já resolvem a barreira da linguagem. Só depois avançar para alertas e personalização.

---

## 7. Diferenciais e alternativas

| Alternativa | O que oferece | Limite | Nosso diferencial |
|---|---|---|---|
| Portais da Transparência | Dado bruto oficial e completo | Linguagem técnica e dispersa | Tradução e experiência simples |
| Ranking dos Políticos | Nota consolidada por parlamentar | Metodologia opaca para leigos | Comparação com fonte e critério visíveis |
| Monitor de Gastos | Acompanhamento de despesas | Foco orçamentário, pouco didático | Explicação do que o gasto significa |
| Lei de Acesso à Informação (LAI) | Direito de pedir informação | Exige pedido e espera | Leitura imediata do que já é público |

O diferencial não é criar dado novo, e sim ser a camada de tradução neutra que conecta o dado oficial ao cidadão. Não competimos com os portais: usamos o que eles publicam.

---

## 8. Dados, governo e LGPD

**Fontes oficiais possíveis:** Portal da Transparência (União), dados.gov.br (dados abertos federais), TSE (candidaturas, prestação de contas de campanha), Câmara dos Deputados e Senado Federal (atividade parlamentar, emendas, votações). Também podem ser usados portais estaduais e municipais de transparência, conforme alcance do projeto.

| Tema | Diretriz |
|---|---|
| Origem do dado | Apenas fontes oficiais ou dados abertos públicos |
| Checagem | Conferir o valor na origem antes de publicar |
| Atualização | Registrar data de extração em cada informação |
| Neutralidade | Critérios iguais para todos os agentes, sem juízo de valor |
| LGPD | Tratar somente dados públicos e de interesse coletivo, sem dado sensível |
| Correção | Canal para apontar erro e corrigir com registro de versão |
| Transparência | Metodologia e fontes acessíveis a qualquer usuário |

A regra é simples: o app cita, contextualiza e compara dados públicos, mas nunca opina sobre o mérito político. Toda afirmação precisa ter uma fonte clicável.

---

## 9. Impacto público e sustentabilidade

**Impacto:** aproximar o cidadão do dado público reduz a assimetria de informação entre quem acompanha o orçamento e quem apenas vota. Isso fortalece o controle social, melhora a qualidade do debate público e cria pressão saudável por transparência.

**Sustentabilidade:** o produto se apoia em bases já públicas, o que reduz custo de criação de dado. Os custos concentram-se em integração, curadoria e infraestrutura.

| Frente | Caminho possível |
|---|---|
| Institucional | Editais de inovação e civic tech, apoio de universidades |
| Público | Convênio com órgãos de transparência e controle |
| Imprensa | Versões e exportações para redações e jornalistas |
| Educação | Uso em escolas e conselhos como material cívico |
| Operacional | Curadoria enxuta e reaproveitamento de dados abertos |

O impacto é tanto individual (melhor decisão de voto) quanto coletivo (debate público mais informado).

---

## 10. Métricas de sucesso (KPIs)

| KPI | O que mede | Meta inicial (a definir na validação) |
|---|---|---|
| Respostas de campo | Aderência à hipótese | 15–20 respostas com código `G6-<nnn>` |
| Compreensão do resumo | Usuário entende a ficha em segundos | Alta taxa de leitura sem ajuda |
| Uso do comparador | Interesse em comparar candidatos | Uso recorrente na sessão |
| Cliques na fonte oficial | Confiança e checagem | Parte dos usuários confere a origem |
| Retorno ao app | Hábito de acompanhamento | Reuso em visitas seguintes |
| Compartilhamento | Alcance orgânico | Links compartilhados por usuário |
| Cobertura de dados | Candidatos e cargos disponíveis | Ampliar por sprint |

As metas numéricas finais dependem do resultado da coleta e do tamanho da amostra do grupo.

---

## 11. Riscos e mitigação

| Risco | Descrição | Mitigação |
|---|---|---|
| Desinformação | Resumo mal interpretado vira conclusão errada | Linguagem neutra, fonte visível e contexto |
| Viés | Recorte de dados favorece ou prejudica alguém | Critérios iguais e metodologia publicada |
| Neutralidade | Aparência de posicionamento político | Zero menção a partidos e zero juízo de valor |
| Desatualização | Dado defasado leva a decisão errada | Data de extração e rotina de atualização |
| Fonte incorreta | Informação fora de contexto | Checagem na origem antes de publicar |
| LGPD | Exposição indevida de dado pessoal | Só dado público de interesse coletivo |
| Baixa adoção | Cidadão não usa mesmo com dado fácil | MVP enxuto e teste com a hipótese de campo |
| Dependência de terceiros | Mudança no formato dos portais | Camada de integração flexível |

A neutralidade é tratada como requisito de produto, não como detalhe editorial: o app descreve dados, não avalia pessoas.

---

## 12. Roadmap de sprints

| Sprint | Objetivo | Entrega |
|---|---|---|
| 0 | Fundação | Estrutura + Bloco 0 (perfil) |
| 1 | Perguntas | 20 perguntas em escala 1–5 |
| 2 | Código + planilha | Código por resposta + respostas na planilha |
| 3 | Campo + correlação | Coleta no campo + áudios por código |
| 4 | Análise | Tabulação quanti + leitura quali |
| 5 | Refino final | App pronto + relatório de achados |

O roadmap conecta a validação de hipótese (sprints 1 a 4) ao desenho do produto final (sprint 5).

---

## 13. Como o formulário valida a hipótese (blocos + áudio)

O formulário tem 20 perguntas e um bloco de perfil. Bloco 0 é exceção: marcado por observação, sem pergunta direta. As 20 perguntas são medidas de 1 a 5, sendo 1 um polo e 5 o oposto, sem respostas abertas. As falas do entrevistado vão para um áudio no WhatsApp que começa com o código `G6-<nnn>`, permitindo correlacionar o quantitativo com o qualitativo.

| Bloco | Perguntas | O que mede |
|---|---|---|
| 1 | Q1–Q8 | Conhecimento e acesso (portais, LAI, orçamento, emendas, transparência local) |
| 2 | Q9–Q13 | Interesse e hábito (notícias, política, transparência, fiscalização) |
| 3 | Q14–Q18 | Percepção de transparência (governo, clareza, confiança, fiscalização) |
| 4 | Q19–Q20 | Participação e comportamento (compartilhar, votar por transparência) |

**Como a hipótese é testada:** a hipótese afirma que as pessoas não acompanham e acham os dados públicos complicados demais, mas usariam uma versão traduzida em linguagem simples. Os blocos 1 e 2 medem acompanhamento e acesso; o bloco 3 mede a percepção de complexidade; o bloco 4 mede disposição de uso. O áudio explica o "porquê" por trás da nota.

Cada resposta salva gera o código `G6-<nnn>`, lido no início do áudio. Meta de coleta: 15–20 respostas.

**Leitura dos resultados:**
- Hipótese confirmada: baixo acesso e alta percepção de complexidade, com alta disposição de uso.
- Hipótese parcial: dificuldade relatada, mas pouco interesse em usar.
- Hipótese derrubada: pessoas acompanham e entendem os dados sem precisar de tradução.

---

## 14. Pitch de 30 segundos

Os dados públicos estão abertos, mas quem realmente consegue usá-los? Hoje o cidadão que quer decidir sobre candidatos e agentes políticos esbarra em portais técnicos, planilhas e linguagem orçamentária. Nossa proposta é simples: pegar o dado oficial que já existe e traduzir em linguagem clara, comparável e neutra. Uma ficha simples, um comparador e a fonte sempre visível. Não criamos dado novo nem opinamos sobre política: damos ao eleitor comum a mesma leitura que hoje só especialistas têm. Nossa pergunta de campo é direta: as pessoas usariam uma versão simplificada para decidir o voto? Estamos testando isso com 20 perguntas, código `G6-<nnn>` e áudios por código. Se a hipótese se confirmar, a transparência deixa de ser arquivo e passa a ser decisão.
