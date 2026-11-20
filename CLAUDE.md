# Ik oefen

Kleine oefenspelletjes voor kinderen (basisschoolleeftijd), live op https://ik-oefen.nl via GitHub Pages (`CNAME`). Geen build, geen dependencies: elke pagina is één zelfstandig HTML-bestand met inline CSS en JS.

## Structuur

| Pad | Spel |
|---|---|
| `index.html` | Startpagina: een kaart per spel, beloftes, link naar GitHub-issues |
| `typen/` | De Letterhof — blind leren typen |
| `tafels/` | De Sterrenwacht — tafels oefenen |
| `provincies/` | De Berenkaart — provincies oefenen |
| `rekenen/` | De Rekentrein — plussen en minnen tot 20/50/100/1000 |
| `klok/` | De Klokkentoren — klokkijken, van hele uren tot digitaal |
| `geld/` | De Winkel — betalen en wisselgeld, tot €10/€20/€100 en met centen |
| `spelling/` | Het Ballonnenfeest — spelling: ei/ij, au/ou, d/t, g/ch |
| `splitsen/` | Het Kippenhok — splitsen tot 10: hoeveel eieren liggen onder de kip? |
| `fonts/` | Zelf gehoste Fredoka (`fredoka.css` + woff2 + `OFL-fredoka.txt`) |
| `robots.txt`, `sitemap.xml` | Vindbaarheid |

## Harde regels

- **Geen cookies, geen tracking, geen reclame** — dat belooft de startpagina. Dus ook geen verzoeken naar derden: geen Google Fonts, CDN's, analytics of embeds. Fonts en andere bestanden host je zelf in de repo.
- **Voortgang alleen in `localStorage`**, elke lees/schrijf in `try/catch`; de pagina moet ook zonder opslag werken.
- **Alles in het Nederlands**: teksten, variabelen, functies, commentaar en commitberichten.
- **Font: Fredoka** op alle pagina's, via `fonts/fredoka.css` (`../fonts/fredoka.css` vanuit een spelmap).
- **Kindvriendelijk**: korte zinnen, aanmoedigend, nooit straffend. Bij een fout: laat het goede antwoord zien en laat het overtypen.

## Een spelpagina

- Kop: ronde terugknop (`.terug`, pijl links van de titel, `href="../"`), titel met de spelnaam, korte ondertitel.
- Eigen kleurwereld per spel met CSS-variabelen op `:root`.
- Speelbaar met een echt toetsenbord én op een tablet/telefoon. Rekenspellen hebben een schermtoetsenbord (1–9, ⌫, 0, OK) met `touch-action:manipulation`.
- Moet werken op telefoonbreedte (390px) zonder horizontaal scrollen. Vermijd verspringende layout: reserveer ruimte voor elementen die later verschijnen.
- `<head>`-meta per pagina: `description`, `canonical` (`https://ik-oefen.nl/<map>/`) en Open Graph (`og:title`, `og:description`, `og:url`, `og:locale nl_NL`).
- Elke pagina begint met `<!doctype html>` en `<html lang="nl">` (geen quirks-modus).
- `hidden` werkt niet op `<svg>`; verberg een omhullende `<div>`.

## Nieuw spel toevoegen

1. Nieuwe map met `index.html` volgens bovenstaande opbouw.
2. Kaart op de startpagina (`index.html`) met eigen kleuren en inline SVG-tekeningetje.
3. URL toevoegen aan `sitemap.xml`.

## Het Kippenhok (splitsregels)

- Op het bordje van het hok staat het totaal N (2–10); naast de kip liggen k eieren (k ≥ 1, rijen van 5), de rest ligt onder de kip. Het antwoord N − k is altijd één cijfer: toetsen 0–4 / 5–9 (bij Tot 5 alleen 0–4, want het antwoord is hooguit 4), één tik = antwoord, geen OK of ⌫.
- Niveaus: Tot 5 → Tot 10 (~3 op 4 met N 6–10) → Samen 10 (N altijd 10, hartje op het bordje) → Alles. Elk paar even vaak, nooit twee keer hetzelfde antwoord achter elkaar, geen paar uit de laatste 5; antwoord 0 hooguit één keer per ronde; eerste vraag antwoord 1–3.
- Goed: de kip staat op en je ziet de eieren eronder. Fout: de kip tilt zich even op om te tellen, het goede cijfer licht groen op en het kind tikt het aan. Geen uitleg, alleen een "?"-wolkje bij de kip.
- Beloning: een **kuiken** dat blijvend in de ren loopt (hooguit 40 zichtbaar, totaal ernaast), op tijd (8 s, Alles 10 s) en in één keer goed. 12 eieren per ronde; ★ uitgespeeld, ★★ 9 kuikens, ★★★ alle 12. Einde ronde: elk ei als splitshuisje op de plek van het toetsenbord.
- De poten van de kip staan achter de eieren, anders dekken ze de verstopte eieren af.

## De Rekentrein (rekenregels)

- Ketting: elke som gebruikt de laatste twee getallen (`a op b`), het antwoord rijdt mee naar de volgende som.
- **Nooit onder 0**: bij min staat het grootste getal voorop. Wordt de som groter dan de grens, dan wordt het een min; anders ~1 op 3 toch een min. Antwoord 0 wordt vermeden.
- Om de 4–6 sommen stapt een vers getal in (bordje "nieuw!"), en recente paren worden vermeden om rondjes te doorbreken.
- Getallenlijn-hulp: verschijnt na 8 s zonder invoer (12 s bij tot 1000) of na een fout, **niet** als het tweede getal < 10. Hooguit **2 boogjes**, geen getallen of streepjes op de lijn, alleen de sprong boven de boog: eerst tientallen (incl. honderdtallen), dan eenheden; bij 8 of 9 een tiental te ver en terug (31 + 18 → +20, −2), tenzij dat over de grens gaat. Een terugsprong staat onder de lijn.
- Gouden munt: alleen als de som in één keer goed is vóór de balk leeg is (en zonder lijn). Sterren: ★ uitgespeeld, ★★ 15 munten, ★★★ alle 20.

## De Klokkentoren (klokregels)

- Niveaus volgen de school: heel en half (hele en halve uren) → kwartieren → per 5 minuten → per minuut → digitaal (24 uur). Op een niveau gaat ~3 op 4 vragen over wat nieuw is.
- Vraagsoorten: wijzers zelf slepen (de kern), "hoe laat is het?" (keuze), "over een kwartier" (vanaf kwartieren), en bij digitaal: 15:30 zetten, digitale tijd kiezen, en digitaal → woorden.
- Grote wijzer blauw, kleine wijzer rood. Alleen de grote wijzer is te draaien (overal op de wijzerplaat te pakken), de kleine loopt mee zoals bij het knopje van een echte klok. Tijdens slepen volgt hij soepel je vinger; bij loslaten glijdt hij naar de dichtstbijzijnde stap van het niveau. De klok start 1 à 2 uur van het antwoord (ervoor of erna); bij "over een kwartier" op de gegeven tijd. De grote wijzer pulseert geel tot je hem pakt.
- Tijden in woorden zoals op school: "tien voor half vijf", "één over half één". Afleiders doen echte vergissingen na (uur ernaast, over/voor omgedraaid, wijzers verwisseld).
- **Geen hulp en geen uitlegzinnen** (groep 3 leest nog niet vlot, en het kind moet het zelf doen). Geen Klaar-knop: staat de klok goed bij het loslaten (of na een pijltjestoets), dan telt het meteen. Fout bij kiezen: het goede antwoord licht groen op en het kind tikt het aan.
- 12 vragen per ronde, elk een raampje in de toren (goud = munt). Sterren: ★ uitgespeeld, ★★ 9 munten, ★★★ alle 12.

## De Winkel (geldregels)

- Bedragen intern in centen. Niveaus: tot €10 (munten 1, 2 en briefjes 5, 10), tot €20, tot €100, met centen (10, 20, 50 cent).
- Twee soorten: **Betaal** (gepast betalen) en **Geef terug** (wisselgeld: klant betaalt met het eerstvolgende briefje boven de prijs). Niveau 1 alleen betalen; daarna 6 betaal + 4 terug per ronde van 10.
- Tik geld uit de beurs op de toonbank, tik op de toonbank om terug te pakken. Klopt het precies, dan gaat het vanzelf verder (geen knop). Te veel: de toonbank wiebelt en het laatste geld springt terug (telt als fout). Geen lopend totaal tonen: tellen is de oefening.
- Beloning heet hier **blije klant 😊** (niet "munt", want munten zijn het onderwerp): op tijd en in één keer goed. Elke blije klant zet het gekochte ding (emoji) blijvend in het schap. Sterren: ★ uitgespeeld, ★★ 7 blij, ★★★ alle 10.
- Einde ronde (geen "dicht"-bordje): grote sterren, en op de toonbank elke klant van de ronde als kaartje met wat hij kocht en 😊 (blij) of 🙂. De beurs verdwijnt.
- Munten en briefjes zijn eigen CSS-tekeningen, geen afbeeldingen van echte euro's. Weinig tekst: alleen "Betaal" / "Geef terug" en prijskaartjes.

## Het Ballonnenfeest (spellingregels)

- Niveaus: ei / ij → au / ou → d / t (aan het eind) → g / ch → Alles. Vanaf niveau 2: 9 woorden van het niveau + 3 herhaling, de eerste altijd van het niveau. Per soort ongeveer half/half verdeeld over de twee antwoorden.
- Een woord = plaatje (emoji) + het woord met een gat (`"🐐 g[ei]t"`); de letters eromheen maken duidelijk welk woord het is. Kies uit twee grote knoppen, altijd in dezelfde volgorde. Toetsenbord: de eerste letter (e/i, a/o, d/t, g/c).
- Kies woorden waarbij het andere antwoord geen bestaand woord is (dus geen "licht/ligt"), en emoji die maar één ding betekenen.
- Fout: het gat wiebelt, de goede knop licht groen op en het kind tikt die aan. Geen uitleg.
- Geen geluid of voorlezen: voegt weinig toe.
- Beloning: een **ballon** die opstijgt in de lucht (eigen SVG, blijvend, zweeft zachtjes), op tijd (10 s) en in één keer goed. 12 woorden per ronde; ★ uitgespeeld, ★★ 9 ballonnen, ★★★ alle 12. Einde ronde: sterren en alle woorden van de ronde als kaartjes (met ballon als verdiend).

## Lessen uit de spellen (ontwerp)

- **Weinig tekst, geen uitleg.** Een kind in groep 3 leest nog niet vlot: geen uitlegzinnen of hulptekst in beeld, alleen korte labels ("Betaal") en lof ("Goed zo!"). Liever een hulpmiddel weglaten dan het uitleggen; hulp alleen als erom gevraagd wordt.
- **Geen Klaar/OK-knop als het antwoord een toestand is** (klok gezet, geld neergelegd): controleer vanzelf zodra het klopt (bij loslaten / na elke tik). Een fout telt pas bij een echte vergissing (te veel geld, verkeerde keuze).
- **Slepen**: één ding tegelijk sleepbaar, geen overlappende grijpvlakken. Pointer events met `setPointerCapture`, `touch-action:none` op het sleepvlak. Tijdens slepen soepel de vinger volgen, pas bij loslaten naar een stap laten glijden (niet tussen stappen laten verspringen). Draaien met een "uitgerolde" hoek in `style.transform`, zodat iets altijd de korte kant op draait.
- **Beloning past bij het thema** en heet niet zoals het onderwerp (in De Winkel "blije klant", geen "munt"). Elk spel een eigen wereld: geen thema hergebruiken (De Letterhof is al de tuin). Een blijvende verzameling (het schap) motiveert over dagen heen.
- **Einde ronde**: laat in het speelveld iets zien dat terugblikt (sterren, wat je deze ronde deed), geen leeg vak of bordje als "dicht". Verberg dan de bediening die niets meer doet (beurs, "Begin opnieuw").
- **Niveaus en records**: 4 of 5 niveaus zodat de recordkaarten mooi uitlijnen; houd niveaunamen kort zodat ze niet afbreken ("Heel en half").

## Lessen uit de spellen (techniek)

- `hidden` verliest van een `display:flex/grid` in de CSS: zet er `.x[hidden]{display:none}` bij.
- `overflow:hidden` op een ouder knipt een `box-shadow`-rand (bijv. groene rand bij goed) af: geef de ouder wat padding.
- Emoji tonen niet in de headless browser hier (geen emojifont): vakjes in een screenshot zijn normaal, controleer emoji op een echt apparaat.
- Een testpagina die het spel in een `<iframe>` zet, heeft `<meta charset="utf-8">` nodig (anders gaat "één" mis).
- Het script staat in een IIFE en de pagina heeft geen `</body>`: voeg een autospeler voor een testkopie in vóór de laatste `})();`, zodat hij bij de interne functies kan.
- Start de testserver met `timeout 60 python3 -m http.server …`; `pkill -f http.server` kan je eigen shell meenemen.
- De eerste vraag van een ronde is bewust de makkelijkste soort: speel door om andere vraagsoorten te zien.

## Testen

Er zijn geen tests; controleer in een headless browser via een lokale server (fonts laden niet via `file://`):

```bash
python3 -m http.server 8765 --bind 127.0.0.1 &
~/.cache/ms-playwright/chromium_headless_shell-1255/chrome-headless-shell-linux64/chrome-headless-shell \
  --no-sandbox --hide-scrollbars --window-size=390,820 --virtual-time-budget=3000 \
  --screenshot=/tmp/shot.png http://127.0.0.1:8765/rekenen/
```

Kijk op 390px en ~900px breed. Om een toestand te testen (bijv. de hulp), maak een kopie in de scratchpad en pas daar timers of de begintoestand aan; nooit in het echte bestand laten staan.

## Werkwijze

- Commit en push alleen als daarom gevraagd wordt.
- Commitberichten in het Nederlands, met het spel als voorvoegsel: `Rekentrein: …`, `Sterrenwacht: …`.
