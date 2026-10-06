# Bez rutiny: tři weby, jeden funnel

Stejná struktura jako Fit Na Cestách. Každá složka je samostatný web, který se nasazuje zvlášť.

| Složka | Doména | Role ve funnelu |
|---|---|---|
| `hlavni/` | bezrutiny.cz | Vstup: tým, příběh, výsledky, reference, dvě tlačítka |
| `program/` | program.bezrutiny.cz | Prodej: video, formulář, rezervace termínu auditu |
| `vyzva/` | vyzva.bezrutiny.cz | Lead magnet: 3denní výzva, po registraci stránka Den 1 |

## Cesty zákazníka

```
bezrutiny.cz ──► program.bezrutiny.cz ──► formulář → výběr termínu → potvrzení ──► nabídka výzvy
      │
      └─────────► vyzva.bezrutiny.cz ──► formulář ──► /den1-start ──► bonusový hovor ──► program.bezrutiny.cz
```

Logo na podstránkách vrací na hlavní web. Odkazy mezi weby jsou označené `data-site` a skript je na doméně `bezrutiny.cz` (a `bezrutiny.localhost`) přepíše na správnou subdoménu.

## Spuštění lokálně

```
python3 dev-server.py        # port 8080
```

Poté otevřete http://bezrutiny.localhost:8080 (nebo rozcestník na http://localhost:8080).

## Nasazení

Každou složku nasaďte jako samostatný web (Netlify, Cloudflare Pages, GitHub Pages ve třech repozitářích) a nastavte DNS:

- `bezrutiny.cz` → `hlavni/`
- `program.bezrutiny.cz` → `program/`
- `vyzva.bezrutiny.cz` → `vyzva/`

## Před spuštěním doplnit

- sekce označené `DOPLNIT` (tým, příběh, reference, obchodní údaje, ochrana osobních údajů)
- videa: `hlavni/videos/rozhovor.mp4`, `program/videos/uvod.mp4`
- formuláře (audit, výzva) nikam neodesílají: napojit na e-mail/CRM a kalendář
- ukázkové výsledky nahradit skutečnými, garanci a ceny uvádět jen pravdivě
- odkazy na sociální sítě v patičce hlavního webu

Mapa funnelu a e-maily: `FUNNEL.md`, checklist: `podklady/lead-magnet-checklist.md`.
