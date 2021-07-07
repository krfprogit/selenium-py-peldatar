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

########################################################## MEGOLDAS
######################################################### DONTOBEN AZ OLASZOK !!! :D :D
# kisbetuk unicode: 97-122

import random

sorok_szama_ossz = random.randint(1, 10)
kisbetuk_elso_unicode = 97
kisbetuk_utolso_unicode = 122
kisbetuk_szama = (kisbetuk_utolso_unicode - kisbetuk_elso_unicode) + 1

if kisbetuk_szama % sorok_szama_ossz == 0:
    oszlopok_szama = kisbetuk_szama // sorok_szama_ossz
    sorok_szama_rovid = 0
else:
    oszlopok_szama = kisbetuk_szama // sorok_szama_ossz + 1
    sorok_szama_rovid = sorok_szama_ossz - kisbetuk_szama % sorok_szama_ossz

sorok_szama_hosszu = sorok_szama_ossz - sorok_szama_rovid
print("Sorok száma:", sorok_szama_ossz)

for i in range(1, sorok_szama_hosszu + 1):
    for j in range((kisbetuk_elso_unicode - 1) + i, (kisbetuk_utolso_unicode + 1), sorok_szama_ossz):
        print(chr(j), j, " ", end="")
    print()

for i in range(1, sorok_szama_rovid + 1):
    for j in range((kisbetuk_elso_unicode - 1) + i + sorok_szama_hosszu, (kisbetuk_utolso_unicode + 1),
                   sorok_szama_ossz):
        print(chr(j), j, " ", end="")
    print()
