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
