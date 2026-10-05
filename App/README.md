# App de Coleta — Customer Discovery · AdmCBA

Formulário de campo **offline** em arquivo único (`index.html`), usado na **Parte 3**
(ida ao shopping). Roda no navegador do celular, **sem instalar nada** e **sem internet**.

> Publicado também no site da turma: `https://renato0503.github.io/3SemCba/coleta/`
> (a pasta `coleta/` é uma cópia idêntica desta).

## Como usar

1. Copie a pasta `App/` (ou só o `index.html`) para o celular.
2. Abra o `index.html` no navegador (Chrome/Safari).
   - **Dica:** no Chrome, menu → *Adicionar à tela inicial* para virar ícone.
3. Escolha o **grupo da dupla** (fica salvo no aparelho). Cada grupo tem sua cor.
4. Toque em **Iniciar nova coleta** → marque o **Bloco 0 (perfil) por observação** →
   responda as **20 perguntas** (escala 1–5).
5. Ao salvar, aparece o **CÓDIGO** (`G<n>-<nnn>`). **Leia o código no início do áudio do WhatsApp.**
6. Ao final das 20 perguntas, pergunte se a pessoa quer **deixar o e-mail** para receber o
   **TCLE** (Termo de Consentimento Livre e Esclarecido) e saber o resultado da pesquisa —
   campo opcional, não entra nas notas.
7. No fim do dia, use **Exportar dados** → **CSV** (Excel) ou **JSON** (backup/correlação).

## Protocolo (fixo, vale para todos os grupos)

- **Bloco 0 — Perfil** é a **exceção**: marcado **por observação** (não se pergunta).
  - Faixa etária · Sexo · Classe social (estimada) · Raça/cor (estimada). Em dúvida, **“Não sei estimar”**.
  - **Nunca** pergunte raça nem renda.
- As **demais 20 perguntas** são marcadas de **1 a 5**: `1` = um polo, `5` = polo oposto (os dois vêm rotulados na tela).
- **Sem resposta aberta.** Falas/justificativas vão no **áudio** (quanti = app · quali = áudio).
- Cada resposta salva gera um **código** `G<n>-<nnn>` para correlacionar com o áudio.
- Em campo: **dupla** com 2 celulares (um do formulário, um do áudio).

## Os 6 grupos

| # | Projeto | Professor | Perguntas | Observação |
|---|---|---|---|---|
| G1 | AgroPrevisãoMT | Prof. Heitor | 20 | — |
| G2 | Fila Cidadã | Prof. Renato | 20 | triagem: órgão que mais usa |
| G3 | Ocupações Irregulares | Prof. Heitor | 20 | tema sensível |
| G4 | CRAS Online | Prof. Renato | 20 | — |
| G5 | CuideBem | Prof. Pantalião | 20 | tema sensível (saúde mental) |
| G6 | Dados Públicos | Prof. Pantalião | 20 | tema político (sem citar partidos) |

## O que o app faz (Sprints)

| Sprint | Status | Entrega no app |
|---|---|---|
| 0 — Fundação | ✅ | Estrutura, seleção de grupo, Bloco 0 (perfil) por observação |
| 1 — Perguntas | ✅ | 20 perguntas por grupo (G1–G6) com polos rotulados |
| 2 — Código + planilha | ✅ | Código `G<n>-<nnn>` por resposta + export CSV/JSON |
| 3 — Campo + correlação | ⏳ | Uso real no shopping (log em `SPRINTS.md`) |
| 4 — Análise | ⏳ | Tabulação do CSV + leitura dos áudios |
| 5 — Refino final | ⏳ | Ajustes e relatório de achados |

## Estrutura do código (para manutenção)

- `PERFIL` — campos do Bloco 0 (comuns a todos os grupos).
- `GRUPOS` — dados por grupo: `nome`, `prof`, `cor`/`corDark`/`rgb` (tema), `triagem` (opcional),
  `sensivel`/`aviso` (opcional) e `blocos[]` com `perguntas[]` no formato `{ q, a, b }`
  (`a` = polo 1 · `b` = polo 5). **Cada grupo tem exatamente 20 perguntas.**
- `localStorage` — chaves `cdadmcba_respostas`, `cdadmcba_seq`, `cdadmcba_grupo`, `cdadmcba_sheet_url`.
- Exportação — `gerarCSV()` (separador `;`, BOM UTF-8) e JSON completo.

### Formato do CSV

`codigo; grupo; grupo_nome; data; faixaEtaria; sexo; classe; raca; orgao; Q1; Q2; …; Q20; email_contato`

> A coluna `orgao` é a triagem do G2; nos demais grupos fica vazia.

### Adicionar/editar perguntas

Edite o objeto do grupo em `GRUPOS`. Cada grupo **precisa ter exatamente 20 perguntas**
com os dois polos (`a` e `b`) — o app não aceita meia pergunta.

Depois de editar, **sincronize a cópia publicada**:
```powershell
Copy-Item .\App\index.html .\coleta\index.html -Force
```

## Onde os dados ficam salvos (importante)

O app **não tem backend** — é só HTML/JS local. Os dados moram em duas camadas:

1. **`localStorage` do navegador** daquele celular específico — automático, mas preso àquele
   aparelho. Se limpar dados do navegador ou trocar de celular, perde o que não foi exportado.
2. **Arquivo exportado** (CSV/JSON) — só existe quando alguém clica em exportar/compartilhar.

Para consolidar as respostas de várias duplas em um só lugar, use (na ordem de menor pra maior esforço):

- **Compartilhar + Importar/Mesclar** (já pronto no app): cada dupla manda seu JSON por WhatsApp
  pro celular "central"; nesse celular, usa **Importar/mesclar JSON** — junta tudo sem duplicar
  (mescla pelo código `G<n>-<nnn>`).
- **Backup automático (Google Sheets)** — abaixo, para quem quer que cada resposta vá sozinha
  pra nuvem no momento em que é salva, sem depender de ninguém lembrar de exportar.

## Backup automático — Google Apps Script + Google Sheets (opcional, grátis)

> **Passo a passo rápido:** 1) criar planilha → 2) Extensões → Apps Script → colar o código →
> 3) Implantar como **App da Web** ("Qualquer pessoa") → 4) copiar a URL `/exec` →
> 5) no app: **Exportar dados → cole a URL → Salvar URL de sincronização**. Pronto: cada
> resposta salva sobe sozinha. (O app já trata o CORS do Apps Script: o `POST` sai como
> requisição simples e é marcado como enviado — sem reenviar/duplicar.)

Isso faz cada resposta salva tentar um `POST` automático para uma planilha Google. Exige
internet no momento do salvamento; sem internet, a resposta fica marcada como **pendente** e
sincroniza sozinha assim que o celular reconectar (ou ao tocar em **"Sincronizar pendentes agora"**).

### 1. Criar a planilha e o script

1. Crie uma planilha nova em [sheets.google.com](https://sheets.google.com) (ex.: `Coleta AdmCBA`).
2. Menu **Extensões → Apps Script**.
3. Apague o conteúdo padrão e cole:

```javascript
function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Respostas")
             || SpreadsheetApp.getActiveSpreadsheet().insertSheet("Respostas");
  const dados = JSON.parse(e.postData.contents);

  if (sheet.getLastRow() === 0) {
    const cab = ["recebidoEm","codigo","grupo","grupoNome","criadoEm",
      "faixaEtaria","sexo","classe","raca","orgao"];
    for (let i = 1; i <= 20; i++) cab.push("Q" + i);
    cab.push("email_contato");
    sheet.appendRow(cab);
  }

  const p = dados.perfil || {};
  const r = dados.respostas || {};
  const linha = [new Date(), dados.codigo, dados.grupo, dados.grupoNome, dados.criadoEm,
    p.faixaEtaria || "", p.sexo || "", p.classe || "", p.raca || "", p.orgao || ""];
  for (let i = 0; i < 20; i++) linha.push(r[i] != null ? r[i] : "");
  linha.push(dados.email || "");

  sheet.appendRow(linha);
  return ContentService.createTextOutput(JSON.stringify({ ok: true }))
    .setMimeType(ContentService.MimeType.JSON);
}
```

4. **Implantar → Nova implantação → tipo "App da Web"**.
   - Executar como: **Eu**.
   - Quem pode acessar: **Qualquer pessoa**.
5. Copie a **URL do app da Web** (termina em `/exec`).

### 2. Configurar no app de coleta

1. Abra o app → **Exportar dados**.
2. Cole a URL em **"Sincronização automática"** → **Salvar URL de sincronização**.
3. Pronto — cada resposta nova tenta subir sozinha. O status mostra quantas ficaram pendentes.

> Cada celular/dupla configura a **mesma URL**, então todas as respostas caem na mesma planilha,
> já consolidadas — sem precisar mesclar JSON manualmente no fim do dia.

## Observações técnicas

- **Offline por completo** para a coleta em si — sem CDN, sem fonte externa, sem build.
  A sincronização automática é o único ponto que pede internet, e é opcional.
- `localStorage` funciona em `file://` no Chrome/Safari; se o navegador bloquear, o app avisa
  e o ideal é **exportar** com frequência (o backup em JSON nunca depende do navegador).
- Rodar a partir de um servidor local (`python -m http.server`) é ainda mais seguro, mas não é obrigatório.
