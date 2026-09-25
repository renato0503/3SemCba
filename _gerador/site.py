"""Gera a identidade e os arquivos PWA do site AdmCBA (publicado em renato0503/3SemCba).

- assets/logos/gN.svg + PNGs 32/96/192/512 (render via Playwright)
- GrupoN-*/manifest.json e sw.js (rede primeiro)

As landing pages (index.html) e os MVPs (app.html) de cada grupo são feitos à mão, cada um com design próprio.
Uso (da raiz AdmCBA):  py _gerador/site.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

GRUPOS = {
    1: dict(pasta="Grupo1-AgroPrevisaoMT", nome="AgroPrevisãoMT", curto="AgroPrevisão", slug="agroprevisao", cor="#3f6212", cor2="#ca8a04", fundo="#f5efe0",
            desc="Antecipa como o crescimento do agro pressiona emprego, moradia, transporte e serviços nas cidades de MT.",
            glifo='<path d="M256 400V230" stroke="#fff" stroke-width="30" stroke-linecap="round"/><path d="M256 250c-70 0-110-40-120-110 70 0 110 40 120 110z" fill="#fff"/><path d="M256 290c60 0 100-35 110-95-60 0-100 35-110 95z" fill="ACC2"/><path d="M140 400h232" stroke="ACC2" stroke-width="22" stroke-linecap="round"/>'),
    2: dict(pasta="Grupo2-FilaCidada", nome="Fila Cidadã", curto="Fila Cidadã", slug="filacidada", cor="#111827", cor2="#f59e0b", fundo="#0b0f19",
            desc="Diz quais documentos levar, como está a fila, quanto tempo esperar e onde ir.",
            glifo='<rect x="136" y="150" width="240" height="212" rx="26" fill="none" stroke="#fff" stroke-width="26"/><text x="256" y="300" text-anchor="middle" font-family="monospace" font-weight="700" font-size="120" fill="ACC2">42</text><path d="M136 206h240" stroke="#fff" stroke-width="18"/>'),
    3: dict(pasta="Grupo3-OcupacoesIrregulares", nome="Ocupações Irregulares", curto="Ocupações", slug="ocupacoes", cor="#9a3412", cor2="#fbbf24", fundo="#f3f1ee",
            desc="Levantamento com dados reais das ocupações, das famílias e da infraestrutura para orientar a política pública.",
            glifo='<path d="M126 270L256 160l130 110" fill="none" stroke="#fff" stroke-width="28" stroke-linejoin="round" stroke-linecap="round"/><path d="M156 250v122h200V250" fill="none" stroke="#fff" stroke-width="28" stroke-linejoin="round"/><circle cx="256" cy="300" r="34" fill="ACC2"/><path d="M256 334v40" stroke="ACC2" stroke-width="16" stroke-linecap="round"/>'),
    4: dict(pasta="Grupo4-CRAS-Online", nome="CRAS Online", curto="CRAS Online", slug="crasonline", cor="#1d4ed8", cor2="#facc15", fundo="#eff4ff",
            desc="Envia documentos, agenda e acompanha pedidos do CRAS sem precisar ir até o local.",
            glifo='<rect x="170" y="126" width="172" height="220" rx="18" fill="#fff"/><path d="M204 186h104M204 226h104M204 266h64" stroke="#1d4ed8" stroke-width="16" stroke-linecap="round"/><path d="M150 330c40 0 60 20 106 20s80-30 110-30v60H150z" fill="ACC2"/>'),
    5: dict(pasta="Grupo5-CuideBem", nome="CuideBem", curto="CuideBem", slug="cuidebem", cor="#0f766e", cor2="#5eead4", fundo="#f0fbf8",
            desc="Porta de entrada anônima para apoio psicológico gratuito, com triagem e caminho até o CAPS.",
            glifo='<path d="M256 380s-120-70-120-150a66 66 0 01120-38 66 66 0 01120 38c0 80-120 150-120 150z" fill="#fff"/><path d="M196 262h40l20-36 24 70 18-34h38" fill="none" stroke="#0f766e" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'),
    6: dict(pasta="Grupo6-DadosPublicos", nome="Dados Públicos", curto="Dados Públicos", slug="dadospublicos", cor="#1e1b4b", cor2="#a3e635", fundo="#fafaf9",
            desc="Traduz dados públicos sobre candidatos e agentes políticos para o cidadão decidir melhor.",
            glifo='<rect x="150" y="270" width="44" height="90" rx="8" fill="#fff"/><rect x="214" y="220" width="44" height="140" rx="8" fill="#fff"/><rect x="278" y="180" width="44" height="180" rx="8" fill="#fff"/><circle cx="330" cy="170" r="52" fill="none" stroke="ACC2" stroke-width="22"/><path d="M366 208l38 38" stroke="ACC2" stroke-width="24" stroke-linecap="round"/>'),
}


def logo(g):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{g["cor"]}"/><stop offset="1" stop-color="{g["cor"]}" stop-opacity=".82"/></linearGradient></defs>'
            f'<rect width="512" height="512" rx="112" fill="url(#g)"/>{g["glifo"].replace("ACC2", g["cor2"])}</svg>\n')


def manifest(n, g):
    return json.dumps({
        "name": g["nome"], "short_name": g["curto"], "description": g["desc"], "lang": "pt-BR",
        "start_url": "app.html", "scope": "./", "display": "standalone", "orientation": "portrait",
        "background_color": g["fundo"], "theme_color": g["cor"],
        "icons": [{"src": f"../assets/logos/g{n}-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": f"../assets/logos/g{n}-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
    }, ensure_ascii=False, indent=2) + "\n"


def sw(n, g):
    return f"""const CACHE = '{g['slug']}-v1';
const PRE = ['./', './index.html', './app.html', './manifest.json', '../assets/logos/g{n}.svg'];

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting()));
}});

self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(v => v !== CACHE).map(v => caches.delete(v)))).then(() => self.clients.claim()));
}});

self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  // rede primeiro (conteúdo sempre atualizado); sem internet, usa o cache
  e.respondWith(fetch(e.request).then(res => {{
    if (res && res.ok && new URL(e.request.url).origin === location.origin) {{
      const copia = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, copia));
    }}
    return res;
  }}).catch(() => caches.match(e.request).then(r => r || caches.match('./app.html'))));
}});
"""


def pngs():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        for n in GRUPOS:
            svg = (RAIZ / f"assets/logos/g{n}.svg").read_text(encoding="utf-8")
            for tam in (32, 96, 192, 512):
                pg = nav.new_page(viewport={"width": tam, "height": tam})
                pg.set_content(f'<html><body style="margin:0;background:transparent">{svg.replace("<svg ", f"<svg width={tam} height={tam} ")}</body></html>')
                pg.screenshot(path=str(RAIZ / f"assets/logos/g{n}-{tam}.png"), omit_background=True)
                pg.close()
        nav.close()


def main():
    (RAIZ / "assets/logos").mkdir(parents=True, exist_ok=True)
    for n, g in GRUPOS.items():
        (RAIZ / f"assets/logos/g{n}.svg").write_text(logo(g), encoding="utf-8")
        pasta = RAIZ / g["pasta"]
        (pasta / "manifest.json").write_text(manifest(n, g), encoding="utf-8")
        (pasta / "sw.js").write_text(sw(n, g), encoding="utf-8")
    pngs()
    print("logos, manifests e sw gerados para", len(GRUPOS), "grupos")


if __name__ == "__main__":
    main()
