# Context — Projeto Customer Discovery (AdmCBA / Unifacc)

Registro do que foi pedido e feito neste projeto, para continuar depois.
**Pasta raiz:** `D:\Dev\UnifaccApps\AdmCBA`
**Tema:** preparação, validação e execução de uma **pesquisa de campo (Customer Discovery)** com alunos de Tecnologia e Inovação indo a um shopping entrevistar pessoas reais sobre 6 ideias de app/serviço público.

---

## 1. Objetivo geral

Montar todo o material didático e operacional da atividade, dividido em **3 partes**:

- **Parte 1 — Preparação para a visita técnica** (como abordar, o que entregar).
- **Parte 2 — Validação dos questionários + construção do app de formulário.**
- **Parte 3 — A ida ao shopping + log de sprints** do desenvolvimento do app até ficar pronto.

Além disso: **documentar cada grupo** (README, formulário e contexto de produto).

---

## 2. Regras fixas do app de coleta (protocolo)

Definidas pelo professor e aplicadas em **todos** os grupos:

1. **Bloco 0 — Perfil** é a **exceção**: o entrevistador **marca por observação** (não pergunta).
   - Faixa etária · Sexo · Classe social (estimada) · Raça/cor (estimada).
   - Na dúvida, “Não sei estimar”. Nunca perguntar raça ou renda.
2. **Todas as demais perguntas são marcadas de 1 a 5**, sendo **1 uma dimensão e 5 a dimensão oposta** (cada bloco com os seus polos rotulados).
3. **Todo formulário tem exatamente 20 perguntas** (fora o perfil).
4. **Não existem respostas abertas no formulário.**
5. As falas/justificativas interessantes são **anotadas em um áudio no WhatsApp** pelo aluno gravador.
6. Cada resposta salva gera um **CÓDIGO** `G<grupo>-<nnn>` (ex.: `G2-014`), **lido no início do áudio** → correlação **quanti (formulário) × quali (áudio)**.
7. Em campo: **dupla** com 2 celulares (um do formulário, um do áudio).

---

## 3. Os 6 grupos

| Grupo | Projeto | Professor | Integrantes | Código | Meta |
|---|---|---|---|---|---|
| 1 | **AgroPrevisãoMT** | Heitor | Bruna, Keila, Yanni, Célia | `G1-<nnn>` | 15–20 |
| 2 | **Fila Cidadã** | Renato | Amanda, Stefanny Rosa, Stefany, Kemylly | `G2-<nnn>` | 20 |
| 3 | **Ocupações Irregulares** | Heitor | Robson, Isabela, Reinaldo, Emanoeli | `G3-<nnn>` | 15 |
| 4 | **CRAS Online** | Renato | Anna, Maria Eduarda, Marcelly, Kaique | `G4-<nnn>` | 15–20 |
| 5 | **CuideBem** | Pantalião | Maria Clara, Kaua, Marilene, Cristiane | `G5-<nnn>` | 15–20 |
| 6 | **Dados Públicos** | Pantalião | Erilin, Emilly, Juarez, Flavia | `G6-<nnn>` | 15–20 |

### Ideias
- **G1 AgroPrevisãoMT:** prever quando o crescimento do agro vai aumentar a demanda de emprego, investimento, transporte, moradia e serviços públicos numa região.
- **G2 Fila Cidadã:** indicar quais documentos levar, se o órgão está com fila e o tempo estimado, e onde o cidadão deve ir.
- **G3 Ocupações Irregulares:** levantamento com dados reais (quantas ocupações, famílias, infraestrutura/precariedade), exemplo do loteamento invadido, o que os gestores fazem e o que poderiam fazer.
- **G4 CRAS Online:** subir/registrar documentos online e resolver serviços do CRAS sem ir ao local.
- **G5 CuideBem:** suporte psicológico gratuito via app vinculado ao gov.br, com acompanhamento pelo CAPS.
- **G6 Dados Públicos:** simplificar dados públicos para o cidadão decidir sobre candidatos e agentes políticos.

---

## 4. Estrutura de pastas e arquivos

```
AdmCBA/
├── context.md                      ← este arquivo
├── SPRINTS.md                      ← log de sprints do app + track de pesquisa/apresentação
├── _pesquisa/
│   ├── openalex_busca.py           ← script (stdlib) de busca OpenAlex + conferência Crossref
│   ├── INDICE-PESQUISA.md          ← índice mestre dos dados/papers/apresentações (a criar)
│   └── saidas/                     ← JSON/MD brutos das buscas (a criar)
├── assets/
│   ├── caderno.css                 ← CSS compartilhado dos cadernos (Partes 2 e 3)
│   └── reveal/                     ← reset.css, reveal.css, reveal.js
├── Parte 1/
│   ├── Slides-Shopping.html / .pdf        (10 slides · capa, regra de ouro, 6 grupos, checklist, dica)
│   ├── caderno-shopping.html / .pdf       (20 pág · Customer Discovery completo)
│   ├── Renato.jpg
│   └── CerradoTechLogo.png
├── Parte 2/
│   ├── Slides-Shopping-Parte2.html / .pdf (12 pág · validação + construção do app)
│   └── caderno-shopping-parte2.html / .pdf(11 pág)
├── Parte 3/
│   ├── Slides-Shopping-Parte3.html / .pdf (9 pág · ida ao shopping + sprints)
│   ├── caderno-shopping-parte3.html / .pdf(7 pág)
│   └── SPRINTS.md                         (log de sprints do app)
├── Grupo1-AgroPrevisaoMT/
│   ├── README.md                        (dados do grupo + questionário recebido)
│   ├── formulario-app.md                 (as 20 perguntas na lógica do app)
│   ├── ContextoApp.md                    (visão de produto/inovação)
│   ├── Pesquisa-Dados.md                 (a criar: dados/notícias reais + 12 papers 2021–2026)
│   ├── Slides-<Grupo>.html / .pdf        (a criar: apresentação de defesa da ideia, reveal.js)
│   └── questionario-google-forms-item5.pdf  (questionário enviado pelo grupo)
├── Grupo2-FilaCidada/          → README.md + formulario-app.md + ContextoApp.md
├── Grupo3-OcupacoesIrregulares/→ README.md + formulario-app.md + ContextoApp.md
├── Grupo4-CRAS-Online/         → README.md + formulario-app.md + ContextoApp.md
├── Grupo5-CuideBem/            → README.md + formulario-app.md + ContextoApp.md
└── Grupo6-DadosPublicos/       → README.md + formulario-app.md + ContextoApp.md
```

### O que é cada arquivo de grupo
- **README.md** — ficha do grupo (professor, integrantes, objetivo, hipótese, roteiro de campo, pitch, questionário recebido, protocolo de coleta, checklist, materiais).
- **formulario-app.md** — o formulário final organizado na lógica do app: Bloco 0 (perfil) + **20 perguntas** em escala 1–5 (com os dois polos), sem resposta aberta, código e áudio.
- **ContextoApp.md** — documento de produto/inovação: pitch, problema/oportunidade, personas, proposta de valor, jornada, **MVP | v1 | v2**, diferenciais, dados/governo/LGPD, impacto, KPIs, riscos, roadmap de sprints, validação pela pesquisa e pitch de 30s.

---

## 5. O que já foi feito (histórico)

1. **Parte 1** criada do zero no estilo da pasta `D:\Dev\Aula_IA_Farma` (reveal.js para slides; caderno em HTML com CSS próprio).
   - Slides com os 9 blocos pedidos + **Grupo 6** adicionado depois.
   - Corrigido o slide “Checklist Final” (estava escuro com letra preta) → fundo claro em degradê.
2. **PDFs** da Parte 1 gerados.
3. **Pastas por grupo** criadas (6), depois reorganizadas pelo professor em `Parte 1/`.
4. **README.md de cada grupo** com dados + questionários recebidos:
   - G1 (PDF enviado, 20 perguntas; descartadas 7, 2, 16, 20; destrinchar 2).
   - G2, G4, G5, G6 (enviados por chat e transcritos).
5. **Protocolo único de coleta** documentado (perfil + resposta marcada + áudio com código).
6. **Parte 2** criada (validação dos questionários + construção no app) e **Parte 3** criada (ida ao shopping + **SPRINTS.md**).
7. **Protocolo corrigido**: todas as perguntas em **escala 1–5** (exceto perfil), **20 perguntas por formulário**, **sem respostas abertas** (quali no áudio).
8. **formulario-app.md** criado nos 6 grupos com 20 perguntas cada (subagentes ajudaram no G5/G6 e na auditoria).
9. **ContextoApp.md** criado nos 6 grupos (inicialmente na raiz por engano; movido para os grupos) e depois **reescrito com visão de produto/inovação** (~2.200–2.350 palavras cada).
10. **PDFs da Parte 2** regerados após as mudanças.

### Auditoria dos formulários (resultado)
Os 6 `formulario-app.md` foram verificados: **20 perguntas cada**, Bloco 0 como exceção, escala 1–5, sem resposta aberta, com código `G<grupo>-<nnn>`.

---

## 6. Notas técnicas (geração de PDF)

- Os **slides** usam **reveal.js** e são exportados com a URL `...html?print-pdf`.
- **Só funciona via `file://`** — servido por HTTP local o `print-pdf` sai em branco.
- A geração no Chrome headless é **instável** (às vezes sai 1 página em branco). Solução: **repetir até sair a contagem certa** de páginas.
- Espaços no caminho precisam ser `%20` (ex.: `Parte%202`).
- Comando base (Chrome):
  ```
  chrome --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
    --virtual-time-budget=20000 --print-to-pdf="OUT.pdf" \
    "file:///D:/Dev/UnifaccApps/AdmCBA/Parte%202/Slides-Shopping-Parte2.html?print-pdf"
  ```
- Páginas esperadas: Parte 1 slides = 10 · Parte 2 slides = 12 · Parte 3 slides = 9.

---

## 7. Pendências / próximos passos

- [ ] **Transformar os `formulario-app.md` no app real** (Google Forms/app) — Sprint 0/1 da Parte 3.
- [ ] Implementar **código por resposta** + **planilha automática** (Sprint 2).
- [ ] Criar um **script `.ps1` de regeneração dos PDFs** com o retry (evita a instabilidade do reveal).
- [ ] Opcional: **versão mobile** dos slides/cadernos.
- [ ] Confirmar com a Yanni (G1) o conflito da **pergunta 2** (aparece como descartada e como a destrinchar).
- [ ] Alinhar o G4 (CRAS) e demais às 20 perguntas definidas no `formulario-app.md`.
- [ ] Atualizar `SPRINTS.md` conforme o app evolui.
- [x] **Pesquisa de dados/notícias reais** por grupo (defesa da ideia) — ver seção 10.
- [x] **Referencial científico**: 12 papers por grupo (72 no total, 2021–2026, OpenAlex/Crossref) — ver seção 10.
- [x] Escrever `Grupo<N>/Pesquisa-Dados.md` (6 arquivos) + `_pesquisa/INDICE-PESQUISA.md`.
- [x] Montar **apresentação de defesa por grupo** (reveal.js, 12 slides, estilo Parte 1).
- [x] Gerar os **PDFs** de 3 decks (G1, G2, G3) com 12 páginas cada.
- [ ] Gerar os **PDFs** dos decks G4, G5 e G6 (overflow no `print-pdf`; ver seção 10.4).

---

## 8. Comandos úteis

```powershell
# Listar tudo do projeto
Get-ChildItem -LiteralPath "D:\Dev\UnifaccApps\AdmCBA" -Recurse -File | Select-Object FullName, Length

# Contar páginas de um PDF
$b=[IO.File]::ReadAllText("ARQUIVO.pdf",[Text.Encoding]::GetEncoding(28591)); ([regex]::Matches($b,"/Type\s*/Page[^s]")).Count

# Abrir os materiais
Start-Process "D:\Dev\UnifaccApps\AdmCBA\Parte 1\Slides-Shopping.html"
Start-Process "D:\Dev\UnifaccApps\AdmCBA\Parte 2\caderno-shopping-parte2.html"
```

---

## 9. Contato / responsáveis
- **Coordenação/professor:** Renato Rosa (Cerrado Tech · Unifacc)
- **Professores orientadores:** Heitor, Renato, Pantalião
- **Turma:** Tecnologia e Inovação · Administração e Gestão Pública — FACC/CBA

---

## 10. Demanda atual — pesquisa de dados + referencial científico + apresentação por grupo

**Pedido em:** 21/09/2026.

### 10.1 O que foi pedido
1. Fazer uma **pesquisa de dados e contexto** para trazer mais conteúdo para **defender a ideia de cada app** (6 grupos).
2. Trazer **dados e notícias reais** (Brasil, últimos anos).
3. Fazer **pesquisa científica** sobre o **comportamento do consumidor/cidadão** na temática de cada grupo, com **papers dos últimos 5 anos (2021–2026)**, para comparar/embasar as ideias — **pelo menos 12 por grupo**.
4. Usar as **APIs do projeto `D:\Dev\EscritaArtigos`**.
5. **Depois:** montar uma **apresentação em cada grupo** (defesa da ideia).

### 10.2 Decisões tomadas
- **Onde guardar:** um arquivo `Pesquisa-Dados.md` por grupo + índice mestre `_pesquisa/INDICE-PESQUISA.md`.
- **Volume de papers:** **12 por grupo** (72 no total), peer-reviewed, 2021–2026.
- **Apresentação:** **slides HTML estilo reveal.js**, como a Parte 1, em cada pasta de grupo.
- **APIs:** OpenAlex (`https://api.openalex.org/works`) e Crossref (`https://api.crossref.org/works`) — as mesmas do EscritaArtigos (skill `enriquecer-referencial`; scripts `temp_busca_dois.py` e `referencias_crossref.py`).
- **Cortesia/limites:** `mailto=renato.rosa@unifacc.edu.br`; OpenAlex limita por IP (HTTP 429) → retry com backoff.

### 10.3 O que já foi feito (nesta demanda)
- [x] Lição dos 6 `ContextoApp.md` (problema, personas, hipótese, pitch).
- [x] Mapeadas as APIs do EscritaArtigos: **OpenAlex + Crossref**.
- [x] Testadas as duas APIs (funcionando).
- [x] Criada a pasta `_pesquisa/` e o script `_pesquisa/openalex_busca.py` (só stdlib: busca OpenAlex, monta resumo do abstract, confere DOI na Crossref, retry no 429).
- [x] **115 buscas** salvas em `_pesquisa/saidas/` (4 a 9 por grupo, `.md` + `.json`).
- [x] **72 papers curados** (12 por grupo) e **os 72 DOIs conferidos na Crossref** (existem, `journal-article`, 2021–2025).
- [x] **6 a 10 dados/notícias reais por grupo** com número, ano e link (IBGE, CAGED, INSS, CRAS/CadÚnico, CAPS, Portal da Transparência, etc.).
- [x] **6 arquivos** `Grupo<N>/Pesquisa-Dados.md` (resumo, tabela de dados, leitura, síntese em blocos, 12 papers com DOI, argumentos de defesa, lacunas, fontes).
- [x] **Índice mestre** `_pesquisa/INDICE-PESQUISA.md` com os 72 papers e os dados de destaque.
- [x] **6 apresentações** `Grupo<N>/Slides-<Grupo>.html` (reveal.js, 12 slides cada) + CSS compartilhado `assets/slides-defesa.css`.
- [x] **PDFs de 3 decks** gerados (Chrome headless + retry): G1 AgroPrevisãoMT, G2 Fila Cidadã e G3 Ocupações Irregulares, **12 páginas cada**.
- [x] `context.md` e `SPRINTS.md` atualizados (Track B: P0 a P4 concluídas, P5 em andamento).

### 10.4 O que falta fazer
- [ ] **PDFs dos decks G4, G5 e G6**: a geração não fechou em 12 páginas (G4 saiu com 13, G6 com 15 e G5 saiu em branco com 1 página). Causa: conteúdo de alguns slides estoura a altura de 720 px no `print-pdf`. Ação: enxugar os slides pesados (tabelas, `stat-grid` e ref-cards) e/ou ajustar o CSS, repetindo até sair 12 páginas.
- [ ] Revisar o visual dos 6 decks no navegador (caber em 1280×720).
- [ ] Opcional: aprofundar dados **locais** (município do shopping / região) na defesa de cada grupo.
- [ ] Opcional: versão mobile das apresentações.
- [ ] Atualizar este `context.md` e o `SPRINTS.md` ao fim de cada etapa.

### 10.5 Temas de busca por grupo (rascunho)
| Grupo | Tema do app | Comportamento alvo | Consultas OpenAlex (exemplo) |
|---|---|---|---|
| G1 | AgroPrevisãoMT | percepção de impactos do agro / planejamento urbano | agribusiness regional economic impact; rural growth urban services forecasting |
| G2 | Fila Cidadã | filas, agendamento e acesso a serviços públicos | public service queue waiting time; e-government service adoption |
| G3 | Ocupações Irregulares | moradia, regularização fundiária e percepção | informal settlements regularization; housing policy perception |
| G4 | CRAS Online | digitalização da assistência social e confiança | social assistance digital services; trust e-government documents |
| G5 | CuideBem | busca de ajuda em saúde mental e estigma | mental health help-seeking stigma; digital mental health access |
| G6 | Dados Públicos | transparência, participação e decisão do voto | open government data use; transparency accountability voting behavior |

---

## 11. Sessão 23/09/2026 — correção do curso, nomes completos e CONFACC 2026

### 11.1 Correção importante
- **O curso desta turma é Administração (FACC-CBA, Cuiabá)**, disciplina *Tecnologia da Informação e Sistemas de Gestão*, turma 1020251-N (lista de chamada de 21/09/2026). Onde este projeto diz "Tecnologia e Inovação", **está errado** — corrigir nos materiais (pendente, aguardando ok do professor).
- "Pantalião" (aqui) × "Pantaleão" (3SemVG): confirmar a grafia do nome do professor.

### 11.2 Nomes completos (chamada de 21/09/2026)
| Grupo | Integrantes |
|---|---|
| G1 AgroPrevisãoMT | Bruna da Cunha e Silva, Keila da Costa Campos, Yanni Gabrielli Stabilito do Espírito Santo, Célia Regina Dias de Almeida |
| G2 Fila Cidadã | Amanda Bento Brandão, Stefany Rosa Araujo Correia ("Stefanny Rosa"), Steffany Natilin Campos Mendes ("Stefany"), Kemylly Monique da Silva Prado |
| G3 Ocupações Irregulares | Robson Lucas de Arruda Dias, Izabela Cristina da Cruz Corrêa, Reinaldo da Silva Barreto, Emanoeli Regina de Arruda Leite |
| G4 CRAS Online | Anna Júlia Ferreira de Paula, Maria Eduarda Figueiredo Campos, Marcelly Regina de Figueiredo, Kaique Junior dos Santos |
| G5 CuideBem | Maria Clara de Oliveira Gallio, Kauã Felipe Brandão de Araújo, Marilene da Luz e Silva, Cristiane Agnes Bastos Silva |
| G6 Dados Públicos | Erilin Sabrina Navarro Carvalho, Emilly Gabrielly Navarro Carvalho, Juarez França Ventura da Rocha, Flávia Arruda Dias |

- Laerte Lopes Regis está na chamada, mas **não entra em nenhum trabalho** (decisão do professor, 25/09/2026).
- **Orientador de todos os trabalhos do CONFACC:** Renato de Oliveira Rosa (25/09/2026).

### 11.3 CONFACC 2026
- Os 6 resumos expandidos desta turma estão em `D:\Dev\UnifaccApps\Confacc2026\AdmCBA\`. Todos os DOIs usados existem nos brutos da API (`_pesquisa/saidas`); a única referência não encontrada nos brutos (1 no G2) ficou de fora.
- Esta turma não tem MVP em código: os resumos relatam a especificação do produto (MVP/v1/v2 do `ContextoApp.md`).

### 11.4 Próximos passos
1. Corrigir o rótulo do curso nos materiais.
2. Ida ao shopping e sprints 3–5 (ver `SPRINTS.md`).
