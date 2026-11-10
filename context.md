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

---

## 12. Sessão 25/09/2026 — os 6 MVPs, landings, hub, publicação no 3SemCba e Figura 1 do CONFACC

Até aqui o AdmCBA tinha documentos e especificação, mas **nenhum app em código**. Nesta sessão os 6 MVPs foram construídos, testados, publicados e viraram imagem para o CONFACC.

### 12.1 MVPs (`Grupo<N>/app.html`)
Cada app é autocontido (sem backend, roda 100% no navegador), tem design e arquitetura próprios, e segue o protocolo de dados rotulados (`exemplo`, `simulado`, `a validar`).

| Grupo | App | Arquitetura / destaque |
|---|---|---|
| G1 | AgroPrevisãoMT | store pub/sub + seletores memoizados; mapa em hexágonos SVG; cenário de sensibilidade; alertas |
| G2 | Fila Cidadã | estimador de fila por curva de chegada/capacidade por hora; relatos do usuário ajustam a espera |
| G3 | Ocupações Irregulares | mini-planilha (esquema de colunas + CSV); croqui em canvas; gerador de proposta ao gestor |
| G4 | CRAS Online | máquina de passos declarativa; protocolo com linha do tempo; anexo com selo; WhatsApp; leitura em voz alta |
| G5 | CuideBem | triagem anônima por pontuação com **porta de saída de crise (CVV 188) primeiro**; encaminhamento; respiração |
| G6 | Dados Públicos | base normalizada + **motor de tradução**; comparador lado a lado; método e neutralidade como regra |

- `_gerador/site.py` gera as logos (`assets/logos/gN.svg` + PNG 32/96/192/512), o `manifest.json` e o `sw.js` (rede-primeiro) de cada grupo. A marca neutra do projeto é `assets/logos/projeto.svg` (+ PNG 192/512).
- `assets/md-viewer.html` (novo) renderiza os `.md` dos grupos no site (só funciona hospedado em http, não em `file://`).

### 12.2 Landing de cada grupo + hub
- Cada `Grupo<N>/index.html` virou uma **landing no estilo do próprio app** (hero, pitch, “como funciona”, dados reais, índice de materiais e o app ao vivo num mockup de celular).
- `index.html` na raiz é o **hub da turma**, no visual das outras turmas: nav, hero, faixa de logos, cards dos 6 MVPs, materiais das Partes 1–3 e apresentações de defesa. PWA próprio (`manifest.json`, `sw.js`, `.nojekyll`).

### 12.3 Testes
- `py _ferramentas/smoke.py` (375×740) nos 6 apps: rotas, cliques, **overflow=0** e estado persistindo após reload.
- `py _ferramentas/landing_shots.py` nas 6 landings + hub, em 1280 e 375: **overflow=0**, sem erro de console.

### 12.4 Publicação
- O AdmCBA passou a ser o repositório **https://github.com/renato0503/3SemCba** (branch `main`, Pages já ativo). Foi adicionado **`.nojekyll`** para o Pages não esconder `_pesquisa/` e `_gerador/`.
- Commit da publicação: **`ffed147`** (rebaseado sobre o commit inicial `505afdf`, que só tinha `LICENSE`).
- URL: **https://renato0503.github.io/3SemCba/**

### 12.5 CONFACC 2026 — Figura 1 (telas do MVP)
- O kit `D:\Dev\UnifaccApps\Confacc2026\` agora tem **`Gx-Nome-figura1-mvp.png`** (3 telas, 2330×1440) para os 6 trabalhos do AdmCBA, no mesmo padrão de 3SemVG/8AdmVG.
- `build.py`: a captura de telas passou a reconhecer apps que navegam por **rota em hash** (lê `window.__rotas`), além do padrão `data-aba`/`data-screen`; o `preparo` roda protegido por `try/except`.
- `conteudo_admcba.py`: `app=True` nos 6 e `preparo` para G1 (muda o cenário), G4 (conclui um pedido para aparecer o protocolo) e G5 (roda a triagem).
- Preparos desatualizados corrigidos no 3SemVG: **Quita.AI** (clica “família de exemplo”) e **EDA** (clica os dados de exemplo — o app é trancado por PIN 1234).
- `py build.py` → **OK: 17 trabalhos validados**.

### 12.6 Pendências e próximos passos
1. **Não existe app de coleta do AdmCBA** (os formulários estão só em `formulario-app.md`). Se for aplicar o protocolo de campo (perfil por observação + código + áudio), criar um app como o `coleta/` do 3SemVG.
2. **CONFACC — submissão:** preencher o **e-mail** de cada autor (nome completo já está no `.md`), **subir as imagens** (quadro1 + figura1) e revisar o texto com o grupo. O `lote/` do kit mostra **11/17 prontos** (depende das inscrições/e-mails).
3. **Publicar o kit CONFACC?** — o `index.html` do kit tem nomes dos alunos do AdmCBA, ainda não publicados em site; decisão do professor.
4. **Nomes completos no site:** landings/hub usam os primeiros nomes. Se quiser os completos da chamada (seção 11.2), editar landings/hub (ou `_gerador/site.py`).
5. **Rótulo do curso:** o site diz “Administração e Gestão Pública” (o que os README dos grupos usam); a chamada registra **Administração (FACC-CBA)**. Padronizar quando o professor confirmar.
6. **`Pesquisa-Dados.md` do AdmCBA:** a varredura de citações fabricadas foi feita no 3SemVG, não aqui. O kit registra 1 referência do G2 não encontrada nos brutos; vale conferir os DOIs do AdmCBA contra `_pesquisa/saidas`.
7. Ao editar documentos do AdmCBA, **commitar no 3SemCba** para o site acompanhar (esta seção 12 foi escrita depois do commit `ffed147` e ainda não foi publicada).

## 13. Sessão 20/10/2026 — Resultados da coleta, análise por grupo e publicação

### 13.1 Fonte dos dados e regras de tratamento
- **Planilha de respostas (banco único das 3 turmas):** `1hdR-swgduz5jqhra3OqUNp109xQbrMP42CC_evDXupM`, aba **Respostas** (gid 2144392800), compartilhada como "qualquer pessoa com o link". Colunas: `recebidoEm, codigo, aluno, grupo, grupoNome, criadoEm, faixaEtaria, sexo, classe, raca, orgao, Q1..Q20, email_contato`.
- **Não há coluna de turma.** A turma se deduz por `grupoNome` (nomes únicos entre turmas; na planilha o G5 do 8AdmVG aparece como "CasaHumanizada"). Os códigos `G<n>-<nnn>` **se repetem** (contador local em cada celular), então a chave de unicidade usada é (grupoNome, codigo, criadoEm); 4 duplicatas exatas foram removidas na leitura de 26/10/2026.
- **A triagem de cada grupo (ex.: situação acadêmica, quem cuida das contas, convivência no EDA) NÃO chega à planilha**: o Apps Script só tem a coluna `orgao` (usada pelo Fila Cidadã). Está nos celulares/CSV exportado. Correção pendente: coluna genérica de triagem (e coluna `turma`) no Apps Script.
- **Respostas de arquivo (celular que não sincronizou), somadas ao HTML e fora da planilha:** `coleta-3semvg.json` (8 respostas, G4 SuaCasaSuaVida, atribuídas a Julimary da Silva Amorim) e `cassia_coleta-3semvg.json` (4 respostas de 20 e 21/10, G5 EDA, Cássia Virgínia Aparecida da Silva Nobrega). A G5-001 desse arquivo, de 07/10 (antes da coleta), foi **ignorada** por parecer teste; incluir se for válida (lista `ARQUIVOS` em `_ferramentas/resultados-coleta/build_html.py`). Se o celular sincronizar depois, a deduplicação remove a cópia.
- **Metas por grupo (linhas no gráfico):** 15 (meta inicial), **30 (mínimo total)** e **35 (margem de segurança)**.

### 13.2 Painel de resultados (HTML) e publicação
- **Link da turma (GitHub Pages, repositório próprio):** https://renato0503.github.io/3SemCba/resultados/
- Arquivos: `resultados/index.html` (só esta turma) e, na raiz de `D:\Dev\UnifaccApps`, `Resultados-Coleta.html` (3 turmas) e `Sintese-Resultados.md` (texto completo das análises).
- Conteúdo: síntese da turma, respostas por grupo, perfil observado, 20 perguntas em barras divergentes (polo A à esquerda, polo B à direita, 3 ao centro), análise estatística, interpretação e **hipótese × resultado × literatura** por grupo.
- **Botão "Atualizar agora":** lê a planilha ao vivo e recalcula tudo no navegador. Em `https://` usa `fetch`; aberto como arquivo local (`file://`) usa JSONP do Google (`gviz`). Alternativa: `python atualizar-resultados.py` (raiz) regrava a cópia embutida nos 4 HTMLs.
- **Privacidade:** o HTML não traz e-mails (coluna `email_contato` removida antes de embutir); traz o nome dos alunos coletores por grupo.
- **Gerador e fontes:** `_ferramentas/resultados-coleta/` (README com o fluxo para regerar).

### 13.3 Método estatístico
- Escala 1–5 entre dois polos (1 = polo A, 5 = polo B); **o sentido de cada pergunta varia**, e média baixa pode significar pouco problema (erro corrigido no EDA, ver 3SemVG).
- Por pergunta: média, DP, %1–2, %4–5, **IC95% por bootstrap** e **teste de permutação (inversão de sinais) contra o ponto neutro 3**, com **correção de Holm** nas 20 perguntas do grupo. "Interesse/utilidade médio" = média por respondente dos itens que começam com Utilidade ou Interesse.
- Amostra de conveniência com 10 a 33 respostas por grupo: leitura exploratória, sem generalização. Efeito de teto e concordância automática reduzem o valor dos itens de utilidade; pesam mais os itens de comportamento e de dor.

### 13.4 Literatura: verificação dos DOIs
- Todos os DOIs dos `Pesquisa-Dados.md` (213 únicos) foram conferidos na API da Crossref (existência e título); só os verificados são citados nas análises.
- **AdmCBA e 8AdmVG:** todas as referências existem e os títulos batem.
- **3SemVG:** 24 referências **não se confirmam** (DOIs inexistentes, de outros artigos ou com autores genéricos como "Doe; Lee", "Smith; Jones", "fake"): Dinheiro na Mão 2 (Chong et al.; Fonseca e Matray; e Kaiser et al. com autoria errada, DOI real), LifePath 2, Quita.AI 2, SuaCasaSuaVida 2, EDA 2 (um DOI aponta para "Issue Information"), **Vida no Controle 14 (todas)**. Para o Vida no Controle e para a parte de carreira do LifePath usei artigos achados por busca na Crossref. **Pendente: avisar os grupos para corrigir os arquivos `Pesquisa-Dados.md`.**
- As notas de paralelo só afirmam o que título e resumo sustentam; resumos vêm dos arquivos dos grupos. Gelper et al. (2026) está só como leitura sugerida (sem resumo na API).

### 13.5 Situação dos grupos (leitura de 20/10/2026, 91 respostas válidas)
| Grupo | Projeto | n | Veredito (hipótese de campo) |
|---|---|---|---|
| G1 | AgroPrevisãoMT | 14 | Parcialmente sustentada |
| G2 | Fila Cidadã | 12 | Parcialmente sustentada |
| G3 | Ocupações Irregulares | 18 | Não sustentada como formulada; achado principal é o desconhecimento |
| G4 | CRAS Online | 18 | Parcialmente sustentada |
| G5 | CuideBem | 15 | Não sustentada na primeira parte; segunda parte parcialmente |
| G6 | Dados Públicos | 14 | Sustentada na primeira parte; segunda parte parcial |

### 13.6 Pendências
- Os textos (`interp.json`, `analise_grupos.json`, `sintese.json`) foram revisados em 26/10/2026 (seção 14); **reler e atualizar de novo quando o n mudar** (a página avisa).
- Recrutar mais respostas nos grupos abaixo de 30 (mínimo total) e de 35 (margem de segurança).
- Corrigir o Apps Script: coluna genérica de triagem e coluna `turma`; reimplantar.
- Commit/push pendentes (não foram feitos de propósito): `context.md`, `Termo_Consentimento_*.pdf` e a pasta local `Resultados/` (Resultados-*.md e estatisticas-por-pergunta.csv, versão descritiva inicial).
- **Sprint R1 (painel 100% mobile): ✅ concluída em 20/10/2026** (tabelas em cartões, toque no lugar de tooltip, seções recolhíveis; zero rolagem horizontal em 320–430 px). Pendente só o teste em aparelho real (Chrome Android e Safari iOS). Detalhes em `SPRINTS.md` (Track R).

## 14. Sessão 26/10/2026 — painel regerado e textos revisados

- **AdmCBA segue com 91 respostas válidas** (12–18 por grupo), sem novidades desde 19–20/10.
- **8AdmVG ganhou 13 respostas** desde 21/10 (HoraCerta 28→32; GuiaMobi 32→34; VozGuia 31→34; CasaPiloto 32→34; CasaHumanizada 28→30), então o painel de 3 turmas passou de **419 para 432 respostas válidas** (4 duplicatas removidas; 12 respostas de arquivo do 3SemVG somadas).
- **Regerado** com a planilha de 26/10 (19:04): os 4 HTMLs (`Resultados-Coleta.html` e `resultados/index.html` das 3 turmas), os descritivos (`Resultados/*.md` e `estatisticas-por-pergunta.csv`) e o `Sintese-Resultados.md`.
- **Textos revisados** em `interp.json`, `analise_grupos.json` e `sintese.json`: só o 8AdmVG mudou de números; os textos do AdmCBA continuam válidos (n e médias não mudaram). Atualizados também `ninterp.json` e `atual.json` (n e estatísticas por grupo).
- **Correções no gerador:** `compila.py` agora usa a data da leitura (não mais 20/10 fixo), calcula a faixa de n por turma e **inclui as respostas de arquivo do 3SemVG** (G4 21→29; G5 29→33), ficando consistente com o HTML.
- **Verificação:** painel do AdmCBA e de 3 turmas em 320/360/390/430 px com **0 px de excesso horizontal**, **0 alvos < 44 px** e **0 erro de JS**; sem avisos de “dados mudaram” para nenhum grupo; `analisar()` confirma 8AdmVG com Holm 6/5/17/9/5.
- **Resumo executivo:** fica para depois de nova rodada de coleta, como combinado.
- **Pendências que continuam:** recrutar até 30–35 por grupo no AdmCBA; testar em aparelho real; corrigir o Apps Script (coluna `turma` e triagem genérica); commit/push.

### 14.1 Coleta em campo — 26/10/2026

- **Os alunos saíram para coletar** uma nova rodada. O painel está no snapshot de **26/10/2026, 19:04**: AdmCBA com **91 respostas válidas** e 3 turmas com **432** até a planilha receber as novas respostas.
- **Confirmado em 26/10/2026: as novas respostas são de campo, não teste.** A coleta segue ativa (138 respostas no AdmCBA às 20:24, ainda subindo); por isso o painel e os textos só serão reprocessados quando o lote estabilizar.
- Enquanto estiverem em campo, o botão **Atualizar agora** (`resultados/index.html`) mostra o que já sincronizou. Respostas de celular sem internet entram depois por CSV/JSON (ver `ARQUIVOS` em `build_html.py` e `compila.py`).
- **Quando voltarem, reprocessar nesta ordem:**
  1. baixar a planilha para `dados.csv` (comando no `README.md` do gerador);
  2. `python compila.py` (descritivos + CSV);
  3. `python build_html.py` (4 HTMLs);
  4. `python gerar_md.py` (`Sintese-Resultados.md`);
  5. `python atualizar-resultados.py` (snapshot e data/hora);
  6. revisar `interp.json`, `analise_grupos.json` e `sintese.json` **só nos grupos cujo n mudou** e regerar 3–5.
- **Conferir:** duplicatas pela chave (grupoNome, codigo, criadoEm); respostas de arquivo (`coleta-3semvg.json` e `cassia_coleta-3semvg.json`, ignorando a G5-001 anterior à coleta); e se o painel mostra algum aviso de “dados mudaram”.
- **Resumo executivo:** só depois de fechar essa rodada, como combinado.

---

## 15. Sessão 09/11/2026 — Relato Autoetnográfico (formulário e geração de PDFs)

- **Participam:** G2 Fila Cidadã e G4 CRAS Online (8 alunos; o professor responsável é Renato, os demais grupos ficam de fora).
- **Nos relatos sai:** Faculdade Católica de Cuiabá, 4º Semestre, Bacharelado em Administração, FACC-CBA (semestre confirmado pelo professor em 09/11/2026; o nome do repositório, 3SemCba, não reflete isso).
- **O que é:** cada aluno orientado pelo Prof. Renato responde a um formulário, e as respostas preenchem o modelo oficial do relato autoetnográfico. Um DOCX e um PDF são gerados por aluno.
- **Formulário:** https://renato0503.github.io/relato-autoetnografico/ (repositório `renato0503/relato-autoetnografico`; só a pasta `formulario/` é publicada).
- **Respostas:** planilha privada `1GbpdlfNvbRuIYr051hxfl4SceSFN_l4mEo-LwIV_Kws`, abas `Respostas` (1 linha por aluno; reenvio atualiza) e `Historico` (todos os envios).
- **Geração:** `python gerar.py` em `D:\Dev\UnifaccApps\RelatoAutoetnografico\`; os arquivos saem em `saida/` e o terminal lista quem não respondeu. Fluxo completo no `README.md` de lá.
- **Testado em 09/11/2026:** envio real pela página publicada, reenvio sem duplicar, leitura pelo gerador e geração de DOCX e PDF pelo Word com dados de teste.
- **Pendente:** preencher a área do mestrado em `TITULACAO` no `gerar.py` (sem isso não gera) e apagar a linha `TESTE - APAGAR ESTA LINHA` da planilha, se ainda estiver lá (o gerador a ignora).

---

## 16. Sessão 09/11/2026 — Banner e ficha da III Mostra Synergeia (G4 CRAS Online)

- **Pedido:** banner e ficha do trabalho da **Anna Júlia** e da **Marcelly** (G4 CRAS Online), no modelo `Modelo-banner III MOSTRA SYNERGEIA 2026.pptx`.
- **Entregue em** `D:\Dev\UnifaccApps\Mostra-Synergeia-2026\AdmCBA-G4-CRAS-Online\`:
  - `Banner-CRAS-Online.pptx`, `Banner-CRAS-Online.pdf`, `Ficha-Inscricao-CRAS-Online.docx`, `Ficha-Inscricao-CRAS-Online.pdf`.
- **Banner:** 80 × 120 cm, identidade do modelo preservada; título do trabalho; autores completos (Anna Júlia Ferreira de Paula; Maria Eduarda Figueiredo Campos; Marcelly Regina de Figueiredo; Kaique Junior dos Santos) + orientador Renato de Oliveira Rosa; Introdução/Referencial teórico (esquerda) e Procedimentos metodológicos/Considerações finais (direita); Referências na base.
- **Texto:** encurtado, justificado e direto. Fontes: `Confacc2026/AdmCBA/G4-CRAS-Online.md`, `ContextoApp.md`, `Pesquisa-Dados.md` e `Resultados/Resultados-AdmCBA.md` (**n = 18**). Só DOIs verificados.
- **Faixa visual:** logo do app, print das 3 telas do MVP, gráfico das principais respostas (% de respostas 4–5) com destaque (72% não confiam em número oficial no WhatsApp) e QR code.
- **QR code (HTTP 200 em 09/11/2026):** https://renato0503.github.io/3SemCba/Grupo4-CRAS-Online/app.html
- **Ficha:** Campus **Cuiabá**; modalidade **Apresentação de banner**; autores completos (linhas I–IV); orientador; curso **Administração**; disciplina **Tecnologia da Informação e Sistemas de Gestão**; **4º Semestre**; figura do MVP na área de apresentação; espaçamento ajustado para **1 página A4**.
- **Testes:** `validate.py` do kit PPTX → **All validations PASSED**; ficha em 1 página (PDF); QR apontando para o app publicado.
- **Scripts preservados:** `Mostra-Synergeia-2026\_scripts\` (gerar_graficos.py, gerar_qr.py, gerar_banners_v2.py, layout_banners.ps1, gerar_fichas.py, exportar_fichas.ps1).
- **Pendente:** revisão do conteúdo pelo grupo (nomes, curso, semestre) e commit/push. Nada foi commitado nesta sessão.
