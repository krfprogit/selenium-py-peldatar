# 026 Feladat: filekezelés gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Adott az alábbi szöveges állomány: adat.txt
# Ezt mentsd le magadnál. Ezt kell majd beolvasnod a feladat során.
#
# 3. FELADAT
# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként egy másik fájlba!
# A megoldást egy fajl3.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python2-homework nevű mappába helyezd el.
#
######################################################### MEGOLDAS
print("Olvasd be a fájlt, majd írd ki a lista tartalmát egy sorként egy másik fájlba!")
print("------------------------------------------------------------------------------")

with open("adat.txt", "r", encoding="utf-8") as f:
    adat = f.readlines()

text = [""]
for a in adat:
    text[0] += a
print(text)
