---
name: nieuw-spel
description: Bouw één nieuw spel voor Ik oefen uit WENSLIJST.md (argument = slug). Gebruik bij "/nieuw-spel <slug>" of wanneer de dagelijkse workflow draait.
---

# Een spel bouwen uit de wenslijst

Argument: de slug van een open idee (`## [ ] <slug> — …`) in `WENSLIJST.md`. Je bouwt dat spel helemaal af, zonder iets te vragen: niemand kijkt mee. Je commit en pusht **niet**; dat doet de workflow.

## 1. Voorbereiden

1. Lees `CLAUDE.md` helemaal. De harde regels, "Een spelpagina", "Nieuw spel toevoegen" en beide "Lessen uit de spellen" gelden onverkort.
2. Lees het idee in `WENSLIJST.md`. Je mag het verbeteren als het tegen een regel ingaat, maar houd het leerdoel.
3. Bekijk twee bestaande spellen die er het meest op lijken (bijv. `splitsen/` of `verdelen/` voor een rekenspel met een handeling, `spelling/` voor een keuzespel, `provincies/` voor een kaart) en neem hun opbouw over: kop met `.koptekst` en terugknop, niveauknoppen in `.leskop`, tijdbalk, beloning, einde ronde met sterren, records per niveau in `localStorage` (in try/catch), layout die met de schermhoogte schaalt.

## 2. Bouwen

Raak alleen deze bestanden aan:

- `<slug>/index.html`: het spel, één bestand met inline CSS en JS in een IIFE, alles in het Nederlands, Fredoka via `../fonts/fredoka.css`, favicon, meta's en canonical `https://ik-oefen.nl/<slug>/`. Eigen kleuren op `:root`, eigen SVG-tekeningen, geen externe verzoeken, geen geluid.
- `index.html` (startpagina): een kaart in dezelfde stijl als de andere, met eigen kleuren en een inline SVG-tekeningetje, achteraan in de lijst. Voeg het onderwerp toe aan `description` en `og:description`.
- `sitemap.xml`: de URL.
- `CLAUDE.md`: een rij in de structuurtabel en een korte sectie met de spelregels van dit spel (zoals bij de andere spellen).
- `WENSLIJST.md`: zet het idee op `## [x] <slug> — …` en voeg `- Gebouwd: /dev/<slug>/` toe.

## 3. Testen (verplicht)

Gebruik Python Playwright (`from playwright.sync_api import sync_playwright`, Chromium is geïnstalleerd). Start een server met `timeout 900 python3 -m http.server 8765 --bind 127.0.0.1` op de achtergrond (via een Python-script met `subprocess.Popen` is het makkelijkst) en zet testscripts in een tijdelijke map buiten de repo (bijv. `/tmp/test/`), niet in de repo.

Controleer en herstel tot alles klopt:

1. Op 390×844, 820×1180, 1366×650 en 1600×900: geen `pageerror` of consolefout, geen horizontaal scrollen (`document.documentElement.scrollWidth <= innerWidth`), de bediening in beeld zonder scrollen waar `CLAUDE.md` dat vraagt. Maak screenshots en bekijk ze (Read op het png-bestand): klopt de tekening, overlapt niets, is het leesbaar?
2. Speel een hele ronde op elk niveau: zowel goede als foute antwoorden, met toetsenbord en met klikken/tikken. Een autospeler voeg je alleen in een **kopie** in een tijdelijke map in (vóór de laatste `})();`), nooit in het echte bestand.
3. Einde ronde: sterren, terugblik, records blijven na herladen.
4. De startpagina toont de nieuwe kaart goed op 390 en 1280 breed.

## 4. Afronden

Geef als laatste antwoord de gevraagde JSON:

- `gelukt`: `true` alleen als het spel af is en alle tests slagen.
- `naam`: de spelnaam.
- `bericht`: het commitbericht, Nederlands, met spelnaam als voorvoegsel, bijv. `De Bakkerij: nieuw spel om breuken te oefenen`.
- `reden`: bij `false` in één zin waarom het niet lukte; bij `true` leeg.

Lukt het niet binnen redelijke tijd, of is het idee niet goed te bouwen binnen de regels, geef dan `gelukt: false` met de reden, in plaats van een half spel.
