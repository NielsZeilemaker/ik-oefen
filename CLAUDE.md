# Ik oefen

Kleine oefenspelletjes voor kinderen (basisschoolleeftijd), live op https://ik-oefen.nl via GitHub Pages (`CNAME`). Geen build, geen dependencies: elke pagina is één zelfstandig HTML-bestand met inline CSS en JS.

## Structuur

| Pad | Spel |
|---|---|
| `index.html` | Startpagina: een kaart per spel, beloftes, link naar GitHub-issues |
| `typen/` | De Letterhof — blind leren typen |
| `tafels/` | De Sterrenwacht — tafels oefenen |
| `provincies/` | De Berenkaart — provincies en hun hoofdsteden oefenen |
| `rekenen/` | De Rekentrein — plussen en minnen tot 20/50/100/1000 |
| `klok/` | De Klokkentoren — klokkijken, van hele uren tot digitaal |
| `geld/` | De Winkel — betalen en wisselgeld, tot €10/€20/€100 en met centen |
| `spelling/` | Het Ballonnenfeest — spelling: ei/ij, au/ou, d/t, g/ch |
| `splitsen/` | Het Kippenhok — splitsen tot 10: hoeveel eieren liggen onder de kip? |
| `verdelen/` | De Kikkervijver — aanvullen tot N: hoeveel kikkers moeten er nog op het blad? |
| `zinsdelen/` | De Haven — zinsdelen: persoonsvorm, onderwerp, knippen, gezegde, lijdend voorwerp |
| `kommagetallen/` | Het Atletiekveld — kommagetallen op de meetlat: halven, tienden, honderdsten, aflezen, afronden |
| `maten/` | De Mijnlift — maten omrekenen met de trap: lengte, gewicht, inhoud, met komma |
| `fonts/` | Zelf gehoste Fredoka (`fredoka.css` + woff2 + `OFL-fredoka.txt`) |
| `robots.txt`, `sitemap.xml` | Vindbaarheid (`/dev/` staat in robots.txt op Disallow) |
| `WENSLIJST.md` | Spelideeën (alleen op de dev-branch), bijgehouden door de pijplijn |
| `.github/workflows/`, `.claude/skills/` | De pijplijn: publiceren, ideeën zoeken, dagelijks een spel bouwen |
| `hulpmiddelen/` | Scripts die niet op de site komen (`publiceer.py`, `klokstem.py`) |
| `favicon.svg`, `apple-touch-icon.png` | Icoon van de site |

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
- Favicon op elke pagina, vóór `<title>`: `<link rel="icon" href="/favicon.svg" type="image/svg+xml">` en `<link rel="apple-touch-icon" href="/apple-touch-icon.png">` (oranje vlak met witte ster; de PNG is 180×180 zonder ronde hoeken, iOS rondt zelf af).
- `hidden` werkt niet op `<svg>`; verberg een omhullende `<div>`.

## Nieuw spel toevoegen

1. Nieuwe map met `index.html` volgens bovenstaande opbouw.
2. Kaart op de startpagina (`index.html`) met eigen kleuren en inline SVG-tekeningetje, en de groepen: `data-groep="3-6"` op de `<a class="spel">` en `<span class="groep"> · groep 3–6</span>` in `.wat` (de groepkiezer bovenaan zet passende spellen voorop en maakt de rest lichter, onthouden in `localStorage` `ikoefen-groep`).
3. URL toevoegen aan `sitemap.xml`.
4. Het onderwerp toevoegen aan de opsomming in `description` én `og:description` van de startpagina ("rekenen, splitsen, tafels, …").

## Het Kippenhok (splitsregels)

- Op het bordje van het hok staat het totaal N (2–10); naast de kip liggen k eieren (k ≥ 1, rijen van 5), de rest ligt onder de kip. Het antwoord N − k is altijd één cijfer: toetsen 0–4 / 5–9 (bij Tot 5 alleen 0–4, want het antwoord is hooguit 4), één tik = antwoord, geen OK of ⌫.
- Niveaus: Tot 5 → Tot 10 (~3 op 4 met N 6–10) → Samen 10 (N altijd 10, hartje op het bordje) → Alles. Elk paar even vaak, nooit twee keer hetzelfde antwoord achter elkaar, geen paar uit de laatste 5; antwoord 0 hooguit één keer per ronde; eerste vraag antwoord 1–3.
- Goed: de kip staat op en je ziet de eieren eronder. Fout: de kip tilt zich even op om te tellen, het goede cijfer licht groen op en het kind tikt het aan. Geen uitleg, alleen een "?"-wolkje bij de kip.
- Beloning: een **kuiken** dat blijvend in de ren loopt (hooguit 40 zichtbaar, totaal ernaast), op tijd (8 s, Alles 10 s) en in één keer goed. 12 eieren per ronde; ★ uitgespeeld, ★★ 9 kuikens, ★★★ alle 12. Einde ronde: elk ei als splitshuisje op de plek van het toetsenbord.
- De poten van de kip staan achter de eieren, anders dekken ze de verstopte eieren af.

## De Kikkervijver (verdeelregels)

- Aanvullen tot N: een bordje op de oever toont N. Het linkerblad heeft k kikkers die blijven zitten; het rechterblad begint leeg. Op de oever staan altijd precies 5 kikkers op een rij: pak je er een, dan springt er een nieuwe op dat plekje (de voorraad is eindeloos, dus te veel kan altijd).
- Sleep of tik een kikker van de oever op het rechterblad, of terug (geen fout). Toetsen: → erop, ← terug. Elke kikker houdt zijn plekje op de oever (er schuift niets op); een kikker die terugkomt neemt de plek van de nieuwste kikker op de oever, zodat het er 5 blijven.
- Precies N telt pas na 0,9 s rust; opnieuw pakken breekt dat af. Te veel: het rechterblad wiebelt, de laatste kikker springt terug en het telt als fout (geen lelie). Nergens een lopende telling: tellen is de oefening. Geen huisje of tekst in het speelveld (het splitshuisje en "kan het anders?" waren zonder uitleg niet te snappen, en zonder fout was het te makkelijk).
- Niveaus: Tot 5 (2–5), Tot 10 (4–10), Duiken (de kikkers links duiken na 2 s onder, de balk start dan; na een fout komen ze even boven), Eerlijk (even 4–10, beide bladen beginnen leeg; goed = N in de vijver en gelijk verdeeld, N maar ongelijk = beide bladen wiebelen = fout, te veel = de laatste springt terug).
- Layout: bij `(max-height:901px) and (min-width:600px)` wordt de tekening 500×330 (`kiesIndeling()`, via `matchMedia`, ook bij draaien/verkleinen): de oever is dan een staande strook rechts van de vijver (bordje boven, de 5 kikkers onder elkaar met stap 50), en de tijdbalk staat staand daarnaast (lof weer rechts daarvan). Anders 380×420 met de oever en een liggende balk eronder. Het script zet `--vul` op de vulling, de CSS kiest breedte of hoogte. Grijpvlak 50×50, zodat de staande rij niet overlapt.
- Waterlelie als het in één keer goed is binnen 12 s (+1 s per te verplaatsen kikker boven 4); blijft in de vijver (nieuwste 5 + teller). ★★ 7, ★★★ 10. Einde ronde: sterren op het bordje, de lelies van de ronde op de bladen.

## De Berenkaart

- Twee keuzes: **wat** (Provincies | Hoofdsteden, `data.onderwerp`) en **hoe** (Op de kaart | Kies de naam, `data.modus`). Intern draait alles op provincienaam; `noem()` geeft wat het kind ziet (provincie of hoofdstad). Eén gedeelde berenplank.
- Hoofdsteden: een stip per stad (`STEDEN`, omgerekend uit RD-coördinaten en gecontroleerd met `isPointInFill`: elke stip ligt in zijn provincie). Op de kaart: tik de stip aan (grijpvlak r=24; Groningen–Assen liggen 54 uit elkaar). Kies de naam: de stip knippert en de provincie licht op. Het naamlabel wijst dan naar de stip. Amsterdam en Rotterdam staan bewust niet op de kaart.

- De kaart is zo groot als in de hoogte past (X=590). Op een liggend scherm tot 1000px hoog en vanaf 700px breed: kaart links, de rest rechts, zonder plakken en zonder `haalInBeeld`-scroll. De lege marges van de kaart zijn voor de namen met lijntjes: niet wegknippen.
- De Letterhof en De Sterrenwacht hebben geen niveauknoppen: de lestitel blijft staan. Alles past ook op 1366×650; alleen de kop schaalt mee.

## De Rekentrein (rekenregels)

- Ketting: elke som gebruikt de laatste twee getallen (`a op b`), het antwoord rijdt mee naar de volgende som.
- **Nooit onder 0**: bij min staat het grootste getal voorop. Wordt de som groter dan de grens, dan wordt het een min; anders ~1 op 3 toch een min. Antwoord 0 wordt vermeden.
- Om de 4–6 sommen stapt een vers getal in (bordje "nieuw!"), en recente paren worden vermeden om rondjes te doorbreken.
- Getallenlijn-hulp: verschijnt na 8 s zonder invoer (12 s bij tot 1000) of na een fout, **niet** als het tweede getal < 10. Hooguit **2 boogjes**, geen getallen of streepjes op de lijn, alleen de sprong boven de boog: eerst tientallen (incl. honderdtallen), dan eenheden; bij 8 of 9 een tiental te ver en terug (31 + 18 → +20, −2), tenzij dat over de grens gaat. Een terugsprong staat onder de lijn.
- Gouden munt: alleen als de som in één keer goed is vóór de balk leeg is (en zonder lijn). Sterren: ★ uitgespeeld, ★★ 15 munten, ★★★ alle 20.
- Layout: de toetsen schalen met de hoogte (44–64px via `--toets`), de trein niet. Lager dan 760px en minstens 800px breed: trein en getallenlijn links, toetsen rechts (trein krimpt mee via `cqw`).

## De Klokkentoren (klokregels)

- Niveaus volgen de school: heel en half (hele en halve uren) → kwartieren → per 5 minuten → per minuut → digitaal (24 uur). Op een niveau gaat ~3 op 4 vragen over wat nieuw is.
- Vraagsoorten: wijzers zelf slepen (de kern), "hoe laat is het?" (keuze), "over een kwartier" (vanaf kwartieren), en bij digitaal: 15:30 zetten, digitale tijd kiezen, en digitaal → woorden.
- Grote wijzer blauw, kleine wijzer rood. Alleen de grote wijzer is te draaien (overal op de wijzerplaat te pakken), de kleine loopt mee zoals bij het knopje van een echte klok. Tijdens slepen volgt hij soepel je vinger; bij loslaten glijdt hij naar de dichtstbijzijnde stap van het niveau. De klok start 1 à 2 uur van het antwoord (ervoor of erna); bij "over een kwartier" op de gegeven tijd. De grote wijzer pulseert geel tot je hem pakt.
- Tijden in woorden zoals op school: "tien voor half vijf", "één over half één". Afleiders doen echte vergissingen na (uur ernaast, over/voor omgedraaid, wijzers verwisseld).
- **Geen hulp en geen uitlegzinnen** (groep 3 leest nog niet vlot, en het kind moet het zelf doen). Wel een 🔊-knop naast de keuzes: leest ze op verzoek één voor één voor (Web Speech, alleen met een Nederlandse stem op het apparaat; anders geen knop), het knopje dat aan de beurt is licht geel op, en de gouden balk wacht zolang. Geen Klaar-knop: staat de klok goed bij het loslaten (of na een pijltjestoets), dan telt het meteen. Fout bij kiezen: het goede antwoord licht groen op en het kind tikt het aan.
- De klok is zo groot als in de hoogte past (tot 460px), zodat de antwoordknoppen eronder in beeld blijven; groot op een staande tablet, minstens 300px. Past dat niet in de hoogte (lager dan ~900px) en is het scherm minstens 600px breed, dan staat de klok links (gouden balk eronder) en vraag + antwoorden rechts in één kolom. De keuze hangt alleen af van de beschikbare hoogte, niet van het apparaat.
- Slepen op een tablet: alleen de eerste vinger telt (een hand op het scherm stoort niet), en `touchstart`/`touchmove` worden zelf geblokkeerd (Safari negeert `touch-action` op een `<svg>`).
- Geen niveautitel boven de klok (de actieve niveauknop zegt het al); munten en "vraag 1 van 12" staan rechts in de rij van de niveauknoppen. De ondertitel staat onder de titel; alleen bij een lage schermhoogte (klok naast de antwoorden) ernaast.
- 12 vragen per ronde, elk een raampje in de toren (goud = munt). Sterren: ★ uitgespeeld, ★★ 9 munten, ★★★ alle 12.

## De Winkel (geldregels)

- Bedragen intern in centen. Niveaus: tot €10 (munten 1, 2 en briefjes 5, 10), tot €20, tot €100, met centen (10, 20, 50 cent).
- Twee soorten: **Betaal** (gepast betalen) en **Geef terug** (wisselgeld: klant betaalt met het eerstvolgende briefje boven de prijs). Niveau 1 alleen betalen; daarna 6 betaal + 4 terug per ronde van 10.
- Tik geld uit de beurs op de toonbank, tik op de toonbank om terug te pakken. Klopt het precies, dan gaat het vanzelf verder (geen knop). Te veel: de toonbank wiebelt en het laatste geld springt terug (telt als fout). Geen lopend totaal tonen: tellen is de oefening.
- Beloning heet hier **blije klant 😊** (niet "munt", want munten zijn het onderwerp): op tijd en in één keer goed. Elke blije klant zet het gekochte ding (emoji) blijvend in het schap. Sterren: ★ uitgespeeld, ★★ 7 blij, ★★★ alle 10.
- Einde ronde (geen "dicht"-bordje): grote sterren, en op de toonbank elke klant van de ronde als kaartje met wat hij kocht en 😊 (blij) of 🙂. De beurs verdwijnt.
- Munten en briefjes zijn eigen CSS-tekeningen, geen afbeeldingen van echte euro's. Weinig tekst: alleen "Betaal" / "Geef terug" en prijskaartjes.
- Layout: schaal `--e` (1px, tot 1.3px op hoge schermen vanaf 600px breed); geld, toonbank en ding rekenen met `calc(N * var(--e))`. Lager dan 760px en minstens 800px breed: winkel links, toonbank met beurs rechts. Beurs en toonbank altijd samen in beeld.

## Het Ballonnenfeest (spellingregels)

- Niveaus: ei / ij → au / ou → d / t (aan het eind) → g / ch → Alles. Vanaf niveau 2: 9 woorden van het niveau + 3 herhaling, de eerste altijd van het niveau. Per soort ongeveer half/half verdeeld over de twee antwoorden.
- Een woord = plaatje (emoji) + het woord met een gat (`"🐐 g[ei]t"`); de letters eromheen maken duidelijk welk woord het is. Kies uit twee grote knoppen, altijd in dezelfde volgorde. Toetsenbord: de eerste letter (e/i, a/o, d/t, g/c).
- Kies woorden waarbij het andere antwoord geen bestaand woord is (dus geen "licht/ligt"), en emoji die maar één ding betekenen.
- Fout: het gat wiebelt, de goede knop licht groen op en het kind tikt die aan. Geen uitleg.
- Geen geluid of voorlezen: voegt weinig toe.
- Beloning: een **ballon** die opstijgt in de lucht (eigen SVG, blijvend, zweeft zachtjes), op tijd (10 s) en in één keer goed. 12 woorden per ronde; ★ uitgespeeld, ★★ 9 ballonnen, ★★★ alle 12. Einde ronde: sterren en alle woorden van de ronde als kaartjes (met ballon als verdiend).
- Layout: het speelveld is klein en blijft altijd onder elkaar; op hoge schermen (≥600px breed) groeien plaatje, woord en knoppen mee via `--extra = clamp(0px, 100svh - 860px, 300px)`, met vaste min-heights tegen verspringen.

## De Haven (zinsdelen)

- Een zin ligt op de kade als rij containers (één woord per container); een zinsdeel = containers die aan elkaar zitten, in één kleur. Het bordje aan de kraan zegt wat je zoekt: pv, ow, wg (alle werkwoorden: pv + de `w`-delen, ook een scheidbaar deel) of lv, met de volle naam klein eronder; bij Knippen "knip".
- Zinnen in `ZINNEN` als `"o De kat|p heeft|l een muis|w gevangen"` (o/p/w/l/b). Alleen korte zinnen zonder bijzin, meewerkend voorwerp, voorzetselvoorwerp of naamwoordelijk gezegde, zodat elk antwoord eenduidig is.
- Niveaus: Persoonsvorm (losse woorden, geen zinsdelen) → Onderwerp → Knippen (tik tussen de woorden waar een nieuw zinsdeel begint) → Gezegde (~4 op 5 een zin met meer werkwoorden) → Lijdend voorwerp. Geen herhaling van eerdere niveaus: alle 12 vragen gaan over het gekozen niveau (een pv-vraag midden in Onderwerp viel niet op en verwarde).
- Geen Klaar-knop: een goed zinsdeel gaat omhoog (de kraan pakt het), een goede knip wordt een oranje streep; zijn ze allemaal gevonden, dan telt het. Fout: wiebelen, de goede zinsdelen/knipplekken lichten groen op en het kind tikt ze aan. Toetsen: ← → kiezen, Enter tikt aan.
- Beloning: een **vrachtschip** (geladen met een container per zinsdeel) vaart uit en blijft aan de horizon liggen (nieuwste 14 + totaal), op tijd (pv 10 s, ow/lv 12 s, wg 14 s, knip 16 s) en in één keer goed. 12 zinnen; ★★ 9 schepen, ★★★ alle 12. Einde ronde: sterren op het bordje en elke zin als regel met het antwoord vet (bij knippen strepen).
- De haven is één SVG (600×170, `overflow:visible` zodat de kade doorloopt), hoogte `min(breedte, clamp(96px, 100svh - 480px, 240px))`; lucht en water zijn de achtergrond van `.haven` (horizon op 58,8%).

## Het Atletiekveld (kommagetallen)

- Alle getallen intern in honderdsten (430 = 4,3); `komma()` toont zo kort mogelijk (4 / 4,3 / 4,37). Eén SVG (600×280): scorebord met de sprong en prijzenbord met lintjes bovenaan, daaronder aanloop, zandbak en meetlat (x 50–570).
- Niveaus: Halven (lat van 4 m, streepjes per 0,5, antwoord x,5) → Tienden (lat van 2 m) → Honderdsten (dunne overzichtslat met een geel vergroot stukje van 0,2, de loep, naar de grote lat in honderdsten; vaak ook 4,0x) → Aflezen (de afdruk en de vlag staan er al, kies uit drie: tiende/honderdste ernaast en 4,03 ↔ 4,3) → Afronden (op hele meters: lat van 3 m, dunne tiendestreepjes, de vlag kan alleen op hele meters; op tienden: vergroot stukje van 0,5, de vlag kan alleen op tienden; nooit precies op de helft). Vanaf niveau 2: 9 van het niveau + 3 herhaling, de eerste altijd van het niveau.
- Sleep de vlag of tik op de lat (ook in de zandbak, behalve bij een vergroot stukje); bij loslaten glijdt hij naar het dichtstbijzijnde streepje en telt het meteen. Loslaten op de beginplek telt niet. Toetsen: ← → schuiven, Enter telt; 1–3 bij kiezen.
- Fout: de vlag wiebelt, de goede plek licht groen op en het kind zet de vlag daar. Bij kiezen: de goede knop licht groen op. Goed: de springer springt vanaf de balk en landt met een afdruk in het zand.
- De opdracht bij Afronden ("Rond af op hele meters / tienden") en de lof staan in de vaste ruimte onder het veld (waar bij Aflezen de knoppen staan), omdat kleine tekst in de SVG op een telefoon onleesbaar wordt.
- Beloning: een **lintje met rozet** (kleur per niveau) aan het prijzenbord, op tijd (8/10/12/10/12 s) en in één keer goed; nieuwste 12 + totaal. ★★ 9, ★★★ 12. Einde ronde: sterren op het scorebord en elke sprong als kaartje op het veld ("4,46 ≈ 4" bij afronden).
- Breedte van het veld: `clamp(300px, (100svh - 320px) * 600/280, 100%)`, zodat alles op 1366×650 zonder scrollen past.

## De Mijnlift (maten)

- Een mijnschacht met een verdieping per maat (de trap: km hm dam m dm cm mm, kg hg dag g, l dl cl ml); hm, dam en dag zijn lichtere tussenverdiepingen die nooit gevraagd worden. Getallen intern als heel getal in de kleinste maat (`N`), `toon(N, e)` geeft de kortste schrijfwijze.
- De toetsen zijn altijd aan. De lift is een hulp die je erbij mag gebruiken (▲▼ naast de mijn, op een verdieping tikken of ↑↓; het bordje van de doelverdieping licht geel op). Per verdieping verschijnt naast de schacht ×10 (omlaag) of :10 (omhoog). Bij OK met een goed antwoord rijdt de lift naar de goede verdieping (het bordje laat de verschuivende komma zien) en dan pas telt het; de tijd telt tot OK. Bij het overtypen zit de lift vast.
- Typen op het schermtoetsenbord (5×3: 0–9, komma, ⌫, OK) of het toetsenbord (`,` en `.` zijn de komma). OK is nodig omdat de lengte van het antwoord niets mag verraden; "0,450" of "0350" telt ook goed (`netjes()`).
- Fout: de lift gaat terug naar de begin-verdieping en zakt/stijgt langzaam, verdieping voor verdieping, terwijl het bordje op het karretje de verschuivende komma laat zien (3,5 m → 35 dm → 350 cm). Daarna staat het goede antwoord groen onder de som en typt het kind het over (telt vanzelf).
- Niveaus: Meter en cm (alleen m/dm/cm, heel) → Hele trap (km t/m mm, heel, hooguit 3 verdiepingen) → Gewicht (kg/g, hg/g, kg/hg) → Inhoud (l/dl/cl/ml) → Met komma (de grote maat heeft 1 of 2 cijfers achter de komma: 2,75 km → m, 450 g → kg). Vanaf niveau 2: 9 van het niveau + 3 herhaling, de eerste altijd van het niveau; nooit twee keer hetzelfde paar maten achter elkaar.
- Beloning: een **edelsteen** (kleur per niveau) in de kist rechtsonder in de mijn (nieuwste 24 + totaal), op tijd (10/12/10/12/14 s, tot OK) en in één keer goed. ★★ 9, ★★★ 12. Einde ronde: sterren op een bord in de lege schacht, de som en toetsen verdwijnen en elke lading staat als kaartje naast (of onder) de mijn.
- Layout: de mijn (SVG 400×440) is `clamp(230px, 100svh - 596px, 440px)` hoog met de liftknoppen ernaast; bij `(max-height:900px) and (min-width:700px)` staat de mijn links en som + toetsen rechts.

## Lessen uit de spellen (ontwerp)

- **Weinig tekst, geen uitleg.** Een kind in groep 3 leest nog niet vlot: geen uitlegzinnen of hulptekst in beeld, alleen korte labels ("Betaal") en lof ("Goed zo!"). Liever een hulpmiddel weglaten dan het uitleggen; hulp alleen als erom gevraagd wordt.
- **Geen Klaar/OK-knop als het antwoord een toestand is** (klok gezet, geld neergelegd): controleer vanzelf zodra het klopt (bij loslaten / na elke tik). Een fout telt pas bij een echte vergissing (te veel geld, verkeerde keuze).
- **Slepen**: één ding tegelijk sleepbaar, geen overlappende grijpvlakken. Pointer events met `setPointerCapture`, `touch-action:none` op het sleepvlak. Tijdens slepen soepel de vinger volgen, pas bij loslaten naar een stap laten glijden (niet tussen stappen laten verspringen). Draaien met een "uitgerolde" hoek in `style.transform`, zodat iets altijd de korte kant op draait.
- **Beloning past bij het thema** en heet niet zoals het onderwerp (in De Winkel "blije klant", geen "munt"). Elk spel een eigen wereld: geen thema hergebruiken (De Letterhof is al de tuin). Een blijvende verzameling (het schap) motiveert over dagen heen.
- **Einde ronde**: laat in het speelveld iets zien dat terugblikt (sterren, wat je deze ronde deed), geen leeg vak of bordje als "dicht". Verberg dan de bediening die niets meer doet (beurs, "Begin opnieuw").
- **Niveaus en records**: 4 of 5 niveaus zodat de recordkaarten mooi uitlijnen; houd niveaunamen kort zodat ze niet afbreken ("Heel en half").

## Lessen uit de spellen (techniek)

- `hidden` verliest van een `display:flex/grid` in de CSS: zet er `.x[hidden]{display:none}` bij.
- **Schalen met de schermhoogte, niet met het apparaat.** Het hoofdbeeld (klok, kaart) of de bediening (toetsen, geld) schaalt met `clamp(min, (100svh - X) * …, max)`, met X gemeten, zodat de bediening zonder scrollen in beeld blijft. Is het scherm te laag om alles onder elkaar te laten passen (en breed genoeg), dan komt het beeld links en de bediening rechts. Telefoon (smal) blijft onder elkaar. Grenzen per spel staan bij het spel.
- **Kop in elk spel**: `.koptekst` om h1 + ondertitel; terugknop midden op de titelregel (`margin-top:calc(clamp(28px,6vw,40px) * .75 - 20px)`); ondertitel naast de titel bij `(max-height:901px) and (min-width:600px)`, anders eronder.
- **Spellen met niveauknoppen**: geen niveautitel (de actieve knop zegt het al); teller en voortgang staan rechts in de rij van de knoppen (`#niveaus` in `.leskop` met `display:contents`, rechterkant `margin-left:auto`).
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

## Pijplijn (main, dev en de workflows)

- **Publiceren** (`publiceer.yml`, GitHub Pages via Actions): bij elke push naar `main` of `dev` zet `hulpmiddelen/publiceer.py` main op https://ik-oefen.nl/ en dev op https://ik-oefen.nl/dev/. In `/dev/` krijgt elke pagina `noindex`, `[dev]` voor de titel en `localStorage`-sleutels met `dev:` ervoor (de voortgang op de echte site blijft heel). `CLAUDE.md`, `WENSLIJST.md`, `.github`, `.claude` en `hulpmiddelen` komen niet op de site. Links met `/` vooraan (favicon) wijzen in /dev/ naar main: gebruik in een spel verder alleen relatieve links.
- **Spelideeën** (`spelideeen.yml`, maandag, skill `spelideeen`): zoekt op internet naar leerstof en spelvormen voor groep 3–8 en zet 5–8 nieuwe ideeën in `WENSLIJST.md` op dev. Mag alleen lezen en schrijven (geen Bash), alleen dat bestand mag veranderen.
- **Dagelijks een spel** (`dagelijks-spel.yml`, 00:00 Nederlandse tijd, skill `nieuw-spel`): haalt main in dev, kiest een willekeurig `## [ ]`-idee (of de slug die je bij handmatig starten opgeeft), laat Claude het bouwen en testen, en zet het idee op `[x]` of `[!]` (mislukt, met reden). Claude draait zonder schrijfrechten; een aparte job controleert dat alleen `<slug>/`, `index.html`, `sitemap.xml`, `CLAUDE.md` en `WENSLIJST.md` veranderden, pusht naar dev en start Publiceren.
- Naar de echte site gaat een spel alleen met de hand: `dev` in `main` mergen (of één commit cherry-picken). Geheim nodig: `CLAUDE_CODE_OAUTH_TOKEN` (van `claude setup-token`).

## Werkwijze

- Commit en push alleen als daarom gevraagd wordt.
- Commitberichten in het Nederlands, met het spel als voorvoegsel: `Rekentrein: …`, `Sterrenwacht: …`.
