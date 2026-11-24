---
name: spelideeen
description: Zoek op internet inspiratie voor nieuwe oefenspellen voor groep 3 t/m 8 en werk WENSLIJST.md bij. Gebruik bij "/spelideeen", "zoek spelideeën", "vul de wenslijst aan" of wanneer de wekelijkse workflow draait.
---

# Spelideeën zoeken voor Ik oefen

Je vult `WENSLIJST.md` in de hoofdmap aan met **5 tot 8 nieuwe, goed uitgewerkte ideeën** voor oefenspellen. De dagelijkse workflow kiest daar willekeurig een open idee uit en laat het bouwen (skill `nieuw-spel`), dus elk idee moet zonder verdere vragen te bouwen zijn.

## 1. Wat is er al

1. Lees `CLAUDE.md` helemaal: de structuurtabel (bestaande spellen), de harde regels en "Lessen uit de spellen". Een idee dat daartegen ingaat, is geen goed idee.
2. Lees `WENSLIJST.md` (als die er is). Elk idee, open (`[ ]`), gebouwd (`[x]`) of mislukt (`[!]`), telt als bestaand: niet opnieuw voorstellen, ook niet in andere woorden.

## 2. Zoeken (groep 3 t/m 8)

Zoek per run breed, en verdeel de ideeën over de groepen. **Groep 6, 7 en 8 krijgen voorrang**: daar heeft de site nog bijna niets. Goede bronnen:

- Leerdoelen: SLO (kerndoelen en tussendoelen rekenen-wiskunde, taal, spelling, oriëntatie op jezelf en de wereld), Cito/doorstroomtoets-domeinen (groep 8), referentieniveaus 1F/1S.
- Leerstof per groep: oefensites en methodes (Squla, Rekenweb, Wereld in getallen, Pluspunt, Taal actief, Staal, Taal in beeld, Snappet-leerlijnen, Junior Einstein, Topografie-sites), juf-en-meester-blogs, leerkrachtfora.
- Spelvormen: onderzoek naar wat werkt (retrieval practice, spaced repetition, directe feedback), en hoe goede educatieve spellen oefenen zonder veel tekst.

Gebruik bronnen **alleen voor leerstof en spelvormen**. Bedenk een eigen spel: nooit een bestaand spel, merk, figuur of uiterlijk namaken.

Onderwerpen om aan te denken (niet beperkend): breuken, kommagetallen, procenten, verhoudingen, grote getallen en afronden, schattend rekenen, cijferend optellen/aftrekken/vermenigvuldigen/delen, metriek stelsel en omrekenen, oppervlakte/omtrek, tijd en tijdsduur, roosters en kalender, grafieken en tabellen, coördinaten en kompas, symmetrie, werkwoordspelling (pv, voltooid deelwoord, verleden tijd), zinsontleding en woordsoorten, leestekens, hoofdletters, meervoud/verkleinwoord, synoniemen en spreekwoorden, Engelse woordjes (groep 7–8), topografie van Europa en de wereld, hoofdsteden, landen en vlaggen (eigen tekeningen), tijdvakken van de geschiedenis, Nederlandse rivieren en wateren.

## 3. Wat een goed idee is

- **Eén leerdoel**, duidelijk passend bij een groep. Te oefenen in korte rondes (10–12 vragen) met directe feedback.
- **Weinig tekst, geen uitleg** in beeld. Groep 3–4 kan nog niet vlot lezen; groep 6–8 wel, maar ook dan geen lappen tekst.
- **Eigen wereld en thema** dat nog niet gebruikt is (zie de bestaande spellen: tuin, sterrenwacht, beren, trein, klokkentoren, winkel, ballonnen, kippenhok, kikkervijver). **Beloning past bij het thema** en heet niet zoals het onderwerp. Een blijvende verzameling die over dagen groeit.
- **4 of 5 niveaus** met korte namen.
- **Te bouwen als één statische HTML-pagina**: geen geluid, geen afbeeldingen van internet, geen verzoeken naar derden; tekeningen in eigen SVG/CSS. Werkt met toetsenbord én aanraking, ook op 390px breed.
- Bij voorkeur een **handeling** (slepen, tikken, zetten) in plaats van alleen een meerkeuzevraag, als het onderwerp dat toelaat.

## 4. Vorm in WENSLIJST.md

Bestaat het bestand nog niet, begin dan met:

```markdown
# Wenslijst

Spelideeën voor Ik oefen. De skill `spelideeen` vult aan, de dagelijkse workflow bouwt een willekeurig open idee (`[ ]`) met de skill `nieuw-spel` en zet het dan op `[x]`. `[!]` = bouwen lukte niet (reden eronder). Wil je een idee niet: haal het weg of zet het op `[-]`.
```

Voeg elk idee onderaan toe, precies in deze vorm (de workflow zoekt op de kopregel):

```markdown
## [ ] <slug> — <Spelnaam> (groep <n>–<m>, <vak>)
- Leerdoel: <wat het kind oefent, concreet, met getalbereik of woordsoort>
- Spel: <wat je ziet en doet, in 3–5 zinnen; de handeling, wat goed/fout doet>
- Niveaus: <4 of 5 korte namen, met wat elk niveau vraagt>
- Beloning: <wat er verdiend wordt en waar het blijft staan>
- Bronnen: <1–3 URL's van leerstof of inspiratie>
```

- `<slug>`: kleine letters, cijfers en streepjes, wordt de mapnaam (bijv. `breuken`, `werkwoorden`, `europa`). Moet nog niet bestaan als map of in de lijst.
- Spelnaam in de stijl van de site: "De …" of "Het …" plus een plek of ding ("De Bakkerij", "Het Observatorium").

Pas bestaande ideeën niet aan en verander geen andere bestanden. Eindig met een korte samenvatting: welke ideeën erbij kwamen en voor welke groepen.
