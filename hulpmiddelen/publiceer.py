#!/usr/bin/env python3
"""Zet de site in elkaar voor GitHub Pages: main in de hoofdmap, dev onder /dev/.

Gebruik:  python3 hulpmiddelen/publiceer.py <map-main> <map-dev of -> <uitvoer>

In /dev/ krijgt elke pagina:
- <meta name="robots" content="noindex">, en "[dev]" voor de titel;
- een eigen voorraadje in localStorage (sleutels krijgen "dev:" ervoor), zodat een
  testversie nooit de voortgang van een kind op de echte site kapotmaakt.
robots.txt (uit main) verbiedt /dev/ al voor zoekmachines.
"""
import os
import shutil
import sys

WEGLATEN = {".git", ".github", ".claude", "hulpmiddelen", "CLAUDE.md", "WENSLIJST.md",
            ".gitignore", ".env", ".env.local", "__pycache__"}
ALLEEN_MAIN = {"CNAME", "robots.txt", "sitemap.xml"}

DEV_KOP = ('<meta charset="utf-8">\n'
           '<meta name="robots" content="noindex">\n'
           '<script>(function(){try{var p="dev:",S=Storage.prototype,g=S.getItem,s=S.setItem,r=S.removeItem;'
           'S.getItem=function(k){return g.call(this,p+k)};'
           'S.setItem=function(k,v){return s.call(this,p+k,v)};'
           'S.removeItem=function(k){return r.call(this,p+k)}}catch(e){}})();</script>')


def kopieer(bron, doel, dev):
    def negeer(map_, namen):
        weg = [n for n in namen if n in WEGLATEN]
        if dev and os.path.abspath(map_) == os.path.abspath(bron):
            weg += [n for n in namen if n in ALLEEN_MAIN]
        return weg
    shutil.copytree(bron, doel, ignore=negeer, dirs_exist_ok=True)


def markeer_dev(map_):
    for wortel, _, bestanden in os.walk(map_):
        for naam in bestanden:
            if not naam.endswith(".html"):
                continue
            pad = os.path.join(wortel, naam)
            with open(pad, encoding="utf-8") as f:
                tekst = f.read()
            if '<meta charset="utf-8">' not in tekst:
                sys.exit("Geen <meta charset=\"utf-8\"> in %s" % pad)
            tekst = tekst.replace('<meta charset="utf-8">', DEV_KOP, 1).replace("<title>", "<title>[dev] ", 1)
            with open(pad, "w", encoding="utf-8") as f:
                f.write(tekst)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main_map, dev_map, uit = sys.argv[1:]
    if os.path.exists(uit):
        shutil.rmtree(uit)
    kopieer(main_map, uit, dev=False)
    if dev_map != "-":
        if os.path.exists(os.path.join(uit, "dev")):
            sys.exit("main heeft zelf al een map dev/")
        kopieer(dev_map, os.path.join(uit, "dev"), dev=True)
        markeer_dev(os.path.join(uit, "dev"))
    print("Klaar:", uit)


if __name__ == "__main__":
    main()
