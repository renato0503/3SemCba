# App de Coleta — Customer Discovery · AdmCBA (publicado)

Cópia publicada para o GitHub Pages (`https://renato0503.github.io/3SemCba/coleta/`).
A **fonte** é `AdmCBA/App/` — ao editar, sincronize:

```powershell
Copy-Item .\App\index.html .\coleta\index.html -Force
```

Formulário de campo **offline** em arquivo único (`index.html`), usado na **Parte 3**
(ida ao shopping). Roda no navegador do celular, **sem instalar nada** e **sem internet**.

## Como usar

1. Abra o `index.html` no navegador do celular (Chrome/Safari).
   - **Dica:** menu → *Adicionar à tela inicial* para virar ícone.
2. Escolha o **grupo da dupla** (fica salvo no aparelho). Cada grupo tem sua cor.
3. Toque em **Iniciar nova coleta** → marque o **Bloco 0 (perfil) por observação** →
   responda as **20 perguntas** (escala 1–5).
4. Ao salvar, aparece o **CÓDIGO** (`G<n>-<nnn>`). **Leia o código no início do áudio do WhatsApp.**
5. Ao final, pergunte se a pessoa quer **deixar o e-mail** para receber o **TCLE** (opcional).
6. No fim do dia, use **Exportar dados** → **CSV** (Excel) ou **JSON** (backup/correlação).

## Protocolo (fixo, vale para todos os grupos)

- **Bloco 0 — Perfil** é a **exceção**: marcado **por observação** (não se pergunta).
  - Faixa etária · Sexo · Classe social (estimada) · Raça/cor (estimada). Em dúvida, **“Não sei estimar”**.
  - **Nunca** pergunte raça nem renda.
- As **demais 20 perguntas** são marcadas de **1 a 5**: `1` = um polo, `5` = polo oposto.
- **Sem resposta aberta.** Falas/justificativas vão no **áudio** (quanti = app · quali = áudio).
- Cada resposta salva gera um **código** `G<n>-<nnn>` para correlacionar com o áudio.
- Em campo: **dupla** com 2 celulares (um do formulário, um do áudio).

## Os 6 grupos

| # | Projeto | Professor | Observação |
|---|---|---|---|
| G1 | AgroPrevisãoMT | Prof. Heitor | — |
| G2 | Fila Cidadã | Prof. Renato | triagem: órgão que mais usa |
| G3 | Ocupações Irregulares | Prof. Heitor | tema sensível |
| G4 | CRAS Online | Prof. Renato | — |
| G5 | CuideBem | Prof. Pantalião | tema sensível (saúde mental) |
| G6 | Dados Públicos | Prof. Pantalião | tema político (sem citar partidos) |

> Documentação completa (backup em Google Sheets, manutenção, formato do CSV) em
> `../App/README.md`.
