########################################### Feladat: Python for ciklus gyakorlása

# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# rj programot, ami kiírja a kisbetűket, és melléjük az karakter kódjukat! A kiírás több oszlopos legyen,
# és legfeljebb 10 soros. Minta:
# a 97 f 102 .....
# b 98 g 103
# c 99 h 104
# d 100 i 105
# e 101 j 106
# A megoldashoz használd a beépített ord() es chr() függvényeket.
#
# A megoldást egy charsandord.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python-homework nevű mappába helyezd el.

########################################################### MEGOLDAS
# kisbetuk unicode: 97-122

sorok_szama = int(input("Kérem adja meg a sorok számát (min. 1, legfeljebb 10): "))
while sorok_szama < 1 or sorok_szama > 10:
    sorok_szama = int(input("Kérem adja meg a sorok számát (legfeljebb 10): "))

kisbetuk_unicode_szamai = []
for i in range(97, 123):
    kisbetuk_unicode_szamai.append(i)

kezdo_ertek = kisbetuk_unicode_szamai[0]
szamlalo = sorok_szama
sor_elemei_unicode = []
sor_elemei = []

while kezdo_ertek < (kisbetuk_unicode_szamai[0] + sorok_szama):
    sor_elemei_unicode.append(kezdo_ertek)
    while (kezdo_ertek + szamlalo) <= kisbetuk_unicode_szamai[len(kisbetuk_unicode_szamai) - 1]:
        sor_elemei_unicode.append((kezdo_ertek + szamlalo))
        szamlalo += sorok_szama
    for i in sor_elemei_unicode:
        sor_elemei.append(chr(i))
        sor_elemei.append(i)
    print(sor_elemei)
    sor_elemei.clear()
    sor_elemei_unicode.clear()
    szamlalo = sorok_szama
    kezdo_ertek += 1
