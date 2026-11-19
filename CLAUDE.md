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

## De Rekentrein (rekenregels)

- Ketting: elke som gebruikt de laatste twee getallen (`a op b`), het antwoord rijdt mee naar de volgende som.
- **Nooit onder 0**: bij min staat het grootste getal voorop. Wordt de som groter dan de grens, dan wordt het een min; anders ~1 op 3 toch een min. Antwoord 0 wordt vermeden.
- Om de 4–6 sommen stapt een vers getal in (bordje "nieuw!"), en recente paren worden vermeden om rondjes te doorbreken.
- Getallenlijn-hulp: verschijnt na 8 s zonder invoer (12 s bij tot 1000) of na een fout, **niet** als het tweede getal < 10. Hooguit **2 boogjes**, geen getallen of streepjes op de lijn, alleen de sprong boven de boog: eerst tientallen (incl. honderdtallen), dan eenheden; bij 8 of 9 een tiental te ver en terug (31 + 18 → +20, −2), tenzij dat over de grens gaat. Een terugsprong staat onder de lijn.
- Gouden munt: alleen als de som in één keer goed is vóór de balk leeg is (en zonder lijn). Sterren: ★ uitgespeeld, ★★ 15 munten, ★★★ alle 20.

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
