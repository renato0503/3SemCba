# Log de Sprints — App de Formulário (Customer Discovery)

Registro do desenvolvimento do app de formulário usado na **Parte 3** (ida ao shopping), desde a fundação até o app ficar **pronto**.

> Regra: **se não está escrito, não aconteceu.** Toda sprint fecha com data, entrega, verificação e bloqueios.

---

## Roadmap

| Sprint | Objetivo | Entrega | Verificação | Status |
|---|---|---|---|---|
| **0** | Fundação | Estrutura do app + Bloco de perfil | Perfil aparece em nova resposta | ⏳ a fazer |
| **1** | Perguntas do grupo | Blocos de perguntas no app | Perguntas na ordem e tipos corretos | ⏳ a fazer |
| **2** | Código + planilha | Código por resposta + respostas na planilha | Salvar gera linha e incrementa o código | ⏳ a fazer |
| **3** | Campo + correlação | Coleta no shopping + áudios ligados por código | Todo áudio começa por código válido | ⏳ a fazer |
| **4** | Análise | Tabulação quanti + leitura quali | Achados com % e frases por código | ⏳ a fazer |
| **5** | Refino final | App pronto + relatório de achados | DoD cumprido e relatório entregue | ⏳ a fazer |

**Legenda de status:** ⏳ a fazer · 🔄 em andamento · ✅ concluída · ⛔ bloqueada

---

## Definição de pronto (DoD)

- [ ] Testado no celular com respostas reais de teste
- [ ] Bloco de perfil gravando corretamente
- [ ] Perguntas na ordem final, sem erro de tipo
- [ ] Código aparecendo e incrementando a cada resposta
- [ ] Respostas caindo automaticamente na planilha
- [ ] Áudios correlacionáveis (todo áudio tem código)
- [ ] Sem erro bloqueante em uso contínuo

---

## Modelo de registro

```
SPRINT ___   Data: __/__   Responsável: ____________

Objetivo:    ______________________________________
Entregue:    ______________________________________
Verificação: ______________________________________
Bloqueios:   ______________________________________
Próxima:     ______________________________________
Status:      ⏳ / 🔄 / ✅ / ⛔
```

---

## Registro

### Sprint 0 — Fundação
- **Data:** 21/09/2026
- **Responsável:** (definir)
- **Objetivo:** criar a base do app e o Bloco 0 (perfil).
- **Entregue:** estrutura do app + blocos de perfil (faixa etária, sexo, classe social, raça).
- **Verificação:** uma resposta de teste mostra os 4 campos de perfil.
- **Bloqueios:** —
- **Próxima:** inserir os blocos de perguntas de cada grupo (Sprint 1).
- **Status:** 🔄 em andamento

### Sprint 1 — Perguntas do grupo
- **Data:** —
- **Responsável:** —
- **Objetivo:** inserir as perguntas validadas (Parte 2) de cada grupo.
- **Entregue:** —
- **Verificação:** —
- **Bloqueios:** depende da validação dos questionários (Parte 2). Casos já tratados: Grupo 1 (cortes 7, 2, 16, 20) e Grupo 6 (padronizar escalas).
- **Próxima:** código + planilha (Sprint 2).
- **Status:** ⏳ a fazer

### Sprint 2 — Código + planilha
- **Data:** —
- **Objetivo:** gerar o código por resposta e gravar na planilha automática.
- **Entregue:** —
- **Verificação:** —
- **Bloqueios:** —
- **Próxima:** coleta em campo (Sprint 3).
- **Status:** ⏳ a fazer

### Sprint 3 — Campo + correlação
- **Data:** —
- **Objetivo:** coletar no shopping e ligar cada áudio à sua resposta pelo código.
- **Entregue:** —
- **Verificação:** todo áudio começa por um código válido.
- **Bloqueios:** —
- **Próxima:** análise (Sprint 4).
- **Status:** ⏳ a fazer

### Sprint 4 — Análise
- **Data:** —
- **Objetivo:** tabular o quanti e ler o quali.
- **Entregue:** —
- **Verificação:** achados com % e frases citadas por código.
- **Bloqueios:** —
- **Próxima:** refino final (Sprint 5).
- **Status:** ⏳ a fazer

### Sprint 5 — Refino final
- **Data:** —
- **Objetivo:** deixar o app pronto e entregar o relatório de achados.
- **Entregue:** —
- **Verificação:** DoD cumprido.
- **Bloqueios:** —
- **Próxima:** —
- **Status:** ⏳ a fazer

---

# Track B — Pesquisa e defesa da ideia por grupo

**Pedido em 21/09/2026.** Roda em paralelo ao track do app (Sprints 0–5 acima). Objetivo:
**embasar cada ideia** com dados e notícias reais + **12 papers por grupo (2021–2026)** e montar a
**apresentação de defesa** de cada grupo (reveal.js, estilo Parte 1).

> Regra: **se não está escrito, não aconteceu.** Busca só entra se o metadado veio da API
> (OpenAlex/Crossref); número/notícia só entra com fonte e link.

## Decisões do Track B

- **Um arquivo por grupo** (`Grupo<N>/Pesquisa-Dados.md`) + **índice mestre** `_pesquisa/INDICE-PESQUISA.md`.
- **12 papers por grupo** (72 no total), peer-reviewed, **2021–2026**, relevância + citações.
- **Apresentação por grupo**: slides HTML reveal.js (`Grupo<N>/Slides-<Grupo>.html`) + PDF.
- **APIs**: OpenAlex (`https://api.openalex.org/works`) e Crossref (`https://api.crossref.org/works`)
  — as mesmas do `D:\Dev\EscritaArtigos`. `mailto=renato.rosa@unifacc.edu.br`; retry no HTTP 429.

## Roadmap do Track B

| Sprint | Objetivo | Entrega | Verificação | Status |
|---|---|---|---|---|
| **P0** | Ferramenta de busca | `_pesquisa/openalex_busca.py` (OpenAlex + Crossref, stdlib) | Script retorna papers 2021–2026; testes de API OK | ✅ concluída |
| **P1** | Busca bruta por grupo | 115 arquivos de busca salvos em `_pesquisa/saidas/` | 4 a 9 consultas por grupo sem erro | ✅ concluída |
| **P2** | Curadoria dos papers | 12 papers peer-reviewed por grupo (72 no total) | 72 DOIs conferidos na Crossref, 2021–2025 | ✅ concluída |
| **P3** | Dados e notícias | Levantamento IBGE/CAGED/INSS/CRAS/CAPS/Transparência | Cada número com fonte e link | ✅ concluída |
| **P4** | Redação | `Grupo<N>/Pesquisa-Dados.md` (6) + `_pesquisa/INDICE-PESQUISA.md` | Arquivo por grupo com 12 papers + dados | ✅ concluída |
| **P5** | Apresentação | `Grupo<N>/Slides-<Grupo>.html` (6) + PDF | 6 decks de 12 slides; PDFs de G1/G2/G3 OK, G4/G5/G6 pendentes | 🔄 em andamento |

**Legenda de status:** ⏳ a fazer · 🔄 em andamento · ✅ concluída · ⛔ bloqueada

---

## Registro — Track B

### Sprint P0 — Ferramenta de busca
- **Data:** 21/09/2026
- **Responsável:** (IA + Renato)
- **Objetivo:** montar a ferramenta de busca científica usando as APIs do EscritaArtigos.
- **Entregue:**
  - Pasta `_pesquisa/` criada.
  - Script `_pesquisa/openalex_busca.py` (só stdlib): busca OpenAlex filtrando `type:article`,
    `from_publication_date=2021-01-01` a `2026-12-31`, ordena por relevância; reconstrói o resumo
    do `abstract_inverted_index`; confere DOI na Crossref; faz retry com backoff no HTTP 429.
  - APIs testadas: **Crossref OK**; **OpenAlex OK** (exige retry por rate limit).
- **Verificação:** script retornou artigos 2021–2026 com DOI e citações nos testes.
- **Bloqueios:** OpenAlex devolve HTTP 429 de forma intermitente (mitigado no script).
- **Próxima:** rodar as buscas por grupo e salvar os brutos (Sprint P1).

### Sprint P1 — Busca bruta por grupo
- **Data:** 21/09/2026
- **Objetivo:** rodar consultas temáticas por grupo no OpenAlex e salvar em `_pesquisa/saidas/`.
- **Entregue:** 115 arquivos (`.md` e `.json`) em `_pesquisa/saidas/`, com 4 a 9 consultas por grupo.
- **Verificação:** cada grupo tem buscas `G<n>_*.md`/`.json`; nenhum arquivo vazio.
- **Bloqueios:** rate limit do OpenAlex (HTTP 429), mitigado pelo retry do script.
- **Próxima:** curadoria dos 12 papers por grupo (Sprint P2).
- **Status:** ✅ concluída

### Sprint P2 — Curadoria dos papers
- **Data:** 21/09/2026
- **Objetivo:** escolher 12 papers peer-reviewed por grupo (2021–2026) e conferir DOI.
- **Entregue:** 72 papers selecionados (12 por grupo).
- **Verificação:** os 72 DOIs foram conferidos na Crossref; todos existem, tipo `journal-article`, 2021–2025.
- **Bloqueios:** —
- **Próxima:** dados e notícias (Sprint P3).
- **Status:** ✅ concluída

### Sprint P3 — Dados e notícias reais
- **Data:** 21/09/2026
- **Objetivo:** levantar dados/notícias reais por tema (IBGE, CAGED, INSS, CRAS/CadÚnico, CAPS, Transparência).
- **Entregue:** 6 a 10 dados/notícias por grupo, com número, ano e link, dentro de cada `Pesquisa-Dados.md`.
- **Verificação:** cada número tem fonte e URL; números sem confirmação marcados `[verificar]`.
- **Bloqueios:** —
- **Próxima:** redação dos arquivos (Sprint P4).
- **Status:** ✅ concluída

### Sprint P4 — Redação dos arquivos de pesquisa
- **Data:** 21/09/2026
- **Objetivo:** escrever `Grupo<N>/Pesquisa-Dados.md` (6) + `_pesquisa/INDICE-PESQUISA.md`.
- **Entregue:** 6 arquivos `Pesquisa-Dados.md` + `_pesquisa/INDICE-PESQUISA.md` (índice mestre com os 72 papers).
- **Verificação:** cada arquivo tem resumo, tabela de dados, síntese em blocos, 12 papers com DOI e argumentos de defesa.
- **Bloqueios:** —
- **Próxima:** apresentação (Sprint P5).
- **Status:** ✅ concluída

### Sprint P5 — Apresentação de defesa por grupo
- **Data:** 21/09/2026 (HTML + parte dos PDFs)
- **Objetivo:** montar `Grupo<N>/Slides-<Grupo>.html` (reveal.js) + PDF por grupo.
- **Entregue:**
  - 6 decks de 12 slides (`Slides-AgroPrevisaoMT`, `Slides-FilaCidada`, `Slides-OcupacoesIrregulares`, `Slides-CRAS-Online`, `Slides-CuideBem`, `Slides-DadosPublicos`) + `assets/slides-defesa.css` compartilhado.
  - **PDFs de G1, G2 e G3** com **12 páginas cada** (Chrome headless + retry).
- **Verificação:** cada deck tem 12 `<section>`, linka o CSS/reveal corretos e traz 12 DOIs.
- **Bloqueios:** os PDFs de **G4 (13 pág), G5 (saiu em branco, 1 pág) e G6 (15 pág)** não fecharam em 12 páginas. Causa: slides com conteúdo além da altura de 720 px no `?print-pdf`. Ação: enxugar slides pesados (tabelas, `stat-grid`, ref-cards) e/ou ajustar CSS, repetindo até 12 páginas.
- **Próxima:** corrigir G4/G5/G6 e revisar o visual no navegador.
- **Status:** 🔄 em andamento

---

## Registro — MVPs (Track C)

### Sprint C1 — MVPs, landings, hub e publicação
- **Data:** 25/09/2026
- **Objetivo:** transformar a especificação de cada grupo em um app funcional e publicar a turma.
- **Entregue:**
  - 6 `Grupo<N>/app.html` com arquitetura própria (store pub/sub, estimador de fila, mini-planilha, máquina de passos, triagem anônima, motor de tradução).
  - 6 landings `Grupo<N>/index.html` no estilo do próprio app, com o app ao vivo.
  - Hub raiz + PWA (`manifest.json`, `sw.js` rede-primeiro, `.nojekyll`) e marca neutra (`assets/logos/projeto.svg`).
  - Logos dos grupos (SVG + PNG), `assets/md-viewer.html` e `_gerador/site.py` (identidade + manifests + sw).
- **Verificação:** `py _ferramentas/smoke.py` OK nos 6 apps; `landing_shots.py` OK em 1280/375; `py build.py` (kit CONFACC) → OK: 17 trabalhos validados.
- **Publicação:** https://github.com/renato0503/3SemCba — commit `ffed147`.
- **Bloqueios:** —
- **Próxima:** app de coleta do AdmCBA (opcional), e-mails/imagens do CONFACC e revisão dos textos.
- **Status:** ✅ concluída

---

## Registro — App de Coleta (Track C2)

### Sprint C2.1 — Identificação do aluno + Likert com 5 rótulos + confirmação
- **Data:** 05/10/2026
- **Objetivo:** identificar quem está coletando antes de cada resposta; mostrar label em todas as 5 opções da escala Likert; confirmar cada resposta.
- **Entregue:**
  - Tela **"Quem está coletando?"** após iniciar coleta — card com nome e iniciais do aluno, extraído dos 4 membros de cada grupo (nomes completos da chamada, seção 11.2 do context).
  - Função `interpolar(n, a, b)` — preenche labels das opções 2, 3 e 4 com base no tipo semântico dos polos (frequência, conhecimento, concordância, utilidade, magnitude, genérico).
  - Modal customizado `confirmCustom()` (estilo app, tema verde escuro, blur backdrop) substitui `window.confirm()` em dois pontos: antes de começar as 20 perguntas (confirma perfil) e antes de registrar cada resposta Likert.
  - Campo `aluno` gravado em cada registro (localStorage, CSV, JSON e Sheets).
  - Termo de Consentimento em PDF (`Termo_Consentimento_AdmCBA.pdf`) — uma página, formato folder, para imprimir e entregar ao participante antes da entrevista. Inclui: identificação da pesquisa, 6 temas dos grupos, procedimentos, riscos/benefícios, direitos, ciência e dados do professor.
- **Verificação:** Playwright test passou — 4 botões de aluno, nomes corretos, sem erros JS; modal visível com texto e botões corretos; commit `b56c023` e `7c70209` no ar.
- **Bloqueios:** —
- **Próxima:** Sprint C2.2 (Sheets com aluno)
- **Status:** ✅ concluída

### Sprint C2.2 — Sheets com campo aluno + nova implantação
- **Data:** 05/10/2026
- **Objetivo:** fazer o Apps Script gravar o nome do aluno na planilha junto com cada resposta.
- **Entregue:**
  - Código `doPost` com `aluno` na mesma posição no `cab` (cabeçalho) e no `linha` (dados).
  - **Problema:** as duas primeiras versões criaram a aba `Respostas` com 31 colunas (faltava `orgao` no `cab`) — todas as colunas ficavam deslocadas a partir de `aluno`. **Solução:** terceira implantação (versão 2, URL nova) com `cab` completo de 32 colunas: `recebidoEm, codigo, aluno, grupo, grupoNome, criadoEm, faixaEtaria, sexo, classe, raca, orgao, Q1–Q20, email_contato`.
  - App atualizado com nova URL do Apps Script: `https://script.google.com/macros/s/AKfycbyqKWcLJnc7XJKUbmvNDdEmWER5eHwCm-uffi6m5ZNTGeQWgfNlopRpYgLNE3yfJaWNew/exec` (commit `7f1d347`).
- **Planilha:** `1hdR-swgduz5jqhra3OqUNp109xQbrMP42CC_evDXupM` (aba **Respostas**).
- **Verificação:** POST de teste `G5-NOVA / Marilene da Luz e Silva` — todas as 32 colunas na ordem correta, Q20 e email com valor.
- **Bloqueios:** dados antigos das versões 1 e 2 ficaram com coluna `aluno` vazia e `orgao` ausente — se necessário, apagar a aba e deixar a versão 3 recriar o cabeçalho.
- **Próxima:** uso real em campo.
- **Status:** ✅ concluída

## Registro — Painel de resultados (Track R)

### Sprint R1 — Painel de resultados 100% mobile ✅
- **Data do registro:** 20/10/2026 (pedido do professor; ainda não iniciada)
- **Objetivo:** o painel de resultados (`resultados/index.html`, link do GitHub Pages compartilhado com os alunos) deve **caber na tela do celular**, sem rolagem horizontal e com leitura confortável, em qualquer largura de 320 a 430 px (e paisagem).
- **Escopo previsto:**
  - Garantir zero rolagem horizontal em 320, 360, 390 e 430 px: tabelas (análise estatística, "Ver como tabela", literatura) viram **cartões empilhados** ou ganham versão compacta, sem estourar a largura.
  - Reorganizar o topo para telas estreitas: título, botão **Atualizar agora**, tema, abas de turma e seletor de grupo (chips) em linhas que quebram bem, com alvos de toque de pelo menos 44 px.
  - Substituir o **tooltip de passar o mouse** por toque (abrir/fechar um detalhe da pergunta ao tocar na barra).
  - Gráfico das 20 perguntas: pergunta acima da barra em largura total, média em destaque, polos A e B legíveis; testar a escala de fonte (16 px mínimo no corpo, sem zoom automático).
  - Cartões de indicadores (KPIs) e gráfico "Respostas por grupo" (linhas 15, 30 e 35) legíveis em coluna única; rótulos das metas sem sobreposição.
  - Textos longos (síntese, interpretação, hipótese × resultado × literatura): parágrafos curtos, seções recolhíveis (abrir/fechar) para reduzir a rolagem.
  - Modo escuro e claro mantidos; botão de atualizar fixo ou de fácil acesso no celular.
- **Critérios de aceite:** (1) sem rolagem horizontal nas larguras acima; (2) todos os controles tocáveis com o polegar; (3) nenhum texto cortado; (4) carrega em rede móvel em poucos segundos; (5) testado em Chrome Android e Safari iOS (ou emulação) e com teste automatizado de largura (Playwright) em 320/360/390/430 px.
- **Onde mexer:** `_ferramentas/resultados-coleta/template2.html` (CSS responsivo e JS de renderização); regerar com `build_html.py` e atualizar os dados com `atualizar-resultados.py`; republicar os 3 `resultados/index.html` e `Resultados-Coleta.html`.
- **Estado atual (ponto de partida):** já há regras responsivas básicas (grade em coluna única abaixo de 700 px, sem rolagem horizontal na página em 390 px), mas as tabelas largas, o tooltip por mouse e os textos longos não foram otimizados para celular.
- **Entregue em 20/10/2026:**
  - **Tabelas viram cartões** em telas de até 700 px (análise estatística e "Ver como tabela"): pergunta, polos, contagens 1–5 e média empilhados; sem rolagem horizontal.
  - **Toque no lugar do tooltip:** tocar numa pergunta abre o detalhe (contagem de cada nota, média, n); teclado (Enter/espaço) também funciona. O tooltip por mouse continua no desktop.
  - **Seções recolhíveis** (síntese geral, análise estatística, hipótese × resultado × literatura): abertas no desktop; no celular a síntese geral e a literatura começam fechadas. O estado aberto/fechado é mantido ao trocar de grupo.
  - Topo reorganizado (botão Atualizar agora em largura total), abas/chips/botões com **mínimo de 44 px**, texto base de 16 px, cartões de indicadores em 2 colunas, links DOI com quebra de linha e área de toque.
- **Verificação (Playwright, toque emulado, 320/360/390/430 px; 360 px em modo escuro):** excesso horizontal de **174 px para 0 px**; alvos de toque menores que 44 px de **17–18 para 0**; sem erro no console; desktop sem regressão. Teste reutilizável: `_ferramentas/resultados-coleta/audit_mobile.py <url>`.
- **Status:** ✅ concluída (20/10/2026). Pendente apenas teste em aparelho real (Chrome Android e Safari iOS).

### Sprint R2 — Painel regerado e textos revisados (26/10/2026) ✅

- **Data:** 26/10/2026
- **Objetivo:** regerar o painel com a planilha atual e revisar os textos de interpretação/análise/síntese contra os números de hoje.
- **Entregue:**
  - Planilha baixada (`dados.csv`, 424 linhas) e 4 HTMLs regerados: `Resultados-Coleta.html` + `resultados/index.html` de AdmCBA, 3SemVG e 8AdmVG (snapshot de 26/10/2026, 19:04).
  - Descritivos regerados: `Resultados/Resultados-<Turma>.md` e `estatisticas-por-pergunta.csv` das 3 turmas; `Sintese-Resultados.md` na raiz.
  - **AdmCBA:** 91 respostas válidas (14/12/18/18/15/14), textos inalterados porque n e médias não mudaram.
  - **8AdmVG:** 151→164 respostas; `interp.json`, `analise_grupos.json` e `sintese.json` atualizados (HoraCerta 32, GuiaMobi 34, VozGuia 34, CasaPiloto 34, CasaHumanizada 30).
  - **Total 3 turmas:** 419→432 respostas válidas (4 duplicatas removidas; 12 respostas de arquivo do 3SemVG).
  - `ninterp.json` e `atual.json` regerados com n e estatísticas por grupo.
  - **Gerador:** `compila.py` passou a usar a data da leitura, faixa de n por turma e a incluir as respostas de arquivo do 3SemVG (G4 29, G5 33).
- **Verificação:** `audit_mobile.py` em 320/360/390/430 px = **0 px de excesso horizontal**, **0 alvos < 44 px**, **0 erro de JS**; `analisar()` no navegador sem avisos de “dados mudaram”; 8AdmVG com Holm 6/5/17/9/5.
- **Bloqueios:** nenhum.
- **Próxima:** nova rodada de coleta no AdmCBA (Sprint R3) e então o resumo executivo; teste em aparelho real e correção do Apps Script continuam pendentes.
- **Status:** ✅ concluída.

### Sprint R3 — Nova rodada de coleta (campo) 🔄

- **Data:** 26/10/2026
- **Objetivo:** os alunos em campo ampliarem a amostra do AdmCBA, mirando 30–35 respostas por grupo (hoje: G1 14, G2 12, G3 18, G4 18, G5 15, G6 14; total 91).
- **Entregue até agora:** coleta em andamento; painel no snapshot de 26/10/2026, 19:04, com botão **Atualizar agora** lendo a planilha ao vivo. **Campo confirmado pelo professor em 26/10/2026** (não é teste); às 20:24 o AdmCBA estava em **138 respostas** e subindo.
- **Verificação (ao fechar a rodada):** baixar `dados.csv`, rodar `compila.py`, `build_html.py`, `gerar_md.py` e `atualizar-resultados.py`; conferir duplicatas, respostas de arquivo e avisos de “dados mudaram”; revisar `interp`/`analise`/`sintese` dos grupos cujo n mudou.
- **Bloqueios:** depende da sincronização dos celulares e da devolução dos arquivos CSV/JSON.
- **Próxima:** reprocessar tudo, revisar os textos e então montar o resumo executivo.
- **Status:** 🔄 em andamento.
