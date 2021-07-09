# 026 Feladat: filekezelés gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Adott az alábbi szöveges állomány: adat.txt
# Ezt mentsd le magadnál. Ezt kell majd beolvasnod a feladat során.
#
# 1. FELADAT
# Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz!
# A megoldást egy fajl1.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python2-homework nevű mappába helyezd el.
#
######################################################### MEGOLDAS
print("Olvasd be a fájlt, és írd ki a tartalmát egy sorba!")
print("---------------------------------------------------")

with open("adat.txt", "r", encoding="utf-8") as f:
    print(f.readlines(), end="")


