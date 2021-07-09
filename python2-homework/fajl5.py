# 026 Feladat: filekezelés gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Adott az alábbi szöveges állomány: adat.txt
# Ezt mentsd le magadnál. Ezt kell majd beolvasnod a feladat során.
#
# 5. FELADAT
# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget,
# hanem minden sort azonnal kiírsz!
# A megoldást egy fajl5.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python2-homework nevű mappába helyezd el.
#
######################################################### MEGOLDAS
print("Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el a szöveget,\n"
      "hanem minden sort azonnal kiírsz!")
print("-------------------------------------------------------------------------------------------------")

with open("adat.txt", "r", encoding="utf-8") as f:
    adat = f.readlines()

text = adat.copy()
print(text)
