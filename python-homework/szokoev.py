# Feladat: Python függvények gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik,
# nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt!
# Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.
# A megoldást egy szokoev.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar
# github repo forkodban egy python-homework nevű mappába helyezd el.

###################################################### MEGOLDAS

def szokoev_eldonto(ev):
    if ev % 4 == 0 and ev % 100 != 0 or ev % 400 == 0:
        return True
    else:
        return False


print("A felhasználótól évszámokat kérek, és mindegyikre kiírom, hogy szökőév-e!")
tovabb = "i"

while tovabb == "i":
    while True:
        try:
            evszam_input = int(input("Kérem adjon meg egy évszámot! "))
            break
        except:
            print("Kérem egész számot adjon meg!")

    evszam_szokoev = szokoev_eldonto(evszam_input)
    if evszam_szokoev:
        print("Az Ön által megadott évszám SZÖKŐÉV!")
    else:
        print("Az Ön által megadott évszám NEM SZÖKŐÉV!")

    while True:
        tovabb = input("Szeretne további évszámokat megadni? (i / n) ")
        if tovabb == "i" or tovabb == "n":
            break
        print("Kérem 'i' vagy 'n' betűt adjon meg!")
