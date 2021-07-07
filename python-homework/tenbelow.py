# Feladat: Python while ciklus gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# rja ki ezek után a beolvasott számok összegét!
# A megoldást egy tenbelow.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar
# github repo forkodban egy python-homework nevű mappába helyezd el.

######################################################## MEGOLDAS

print("Addig olvasok be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.")
szam_osszeg = 0
while True:
    szam_input = input("Kérem adjon meg egy tíznél kisebb számot! ")
    print("Az Ön által megadott szám:", szam_input)
    if float(szam_input) >= 10:
        break
    szam_osszeg += float(szam_input)

print("A beolvasott számok összeg: ", szam_osszeg)
