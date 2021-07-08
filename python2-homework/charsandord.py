# 017 Feladat: Python dictionary gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Szavak előfordulási gyakorisága
# Állapítsuk meg, hogy az alábbi szövegben (TEXT) melyik szó hányszor fordul elő s írassuk ki az eredményt
# a következő formában: szó_1 előfordulások_száma_1 szó_2 előfordulások_száma_2 ...
#
# Az eredményt úgy írassuk ki, hogy a lista szavak szerint rendezve legyen. Minden szó kisbetűsen szerepeljen,
# vagyis pl. a 'The' és 'the' szavak azonos szónak számítanak.
#
# Használjuk az str.split() függvényt (paraméter nélkül) a whitespace karakterek eltávolítására.
#
# Az egyes szavakhoz kapcsolódó írásjelekkel (pont, vessző, idézőjel, stb.) nem kell most foglalkozni.
#
# Ezt a szöveget használd a ruttatáshoz: (TEXT.txt)
#
# A megoldást egy charsandord.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python2-homework nevű mappába helyezd el.

########################################################## MEGOLDAS
print("Ez a progi kiírja, hogy a szövegben (TEXT.txt) melyik szó hányszor fordul elő, a következő formában: \n"
      "szó_1 előfordulások_száma_1 szó_2 előfordulások_száma_2")
print("-------------------------------------------------------")

with open("TEXT.txt", "r", encoding="utf-8") as f:
    szoveg_input_sorok = f.readlines()

szoveg_sorok_nincsvegjel = szoveg_input_sorok.copy()
for szamlalo in range(len(szoveg_sorok_nincsvegjel)):
    if szoveg_sorok_nincsvegjel[szamlalo].endswith("\n"):
        szoveg_sorok_nincsvegjel[szamlalo] = szoveg_sorok_nincsvegjel[szamlalo].replace("\n", "")

szoveg_sorok_nincsureselem = []
for szamlalo in szoveg_sorok_nincsvegjel:
    if szamlalo != "":
        szoveg_sorok_nincsureselem.append(szamlalo)

szoveg_szavak_split = []
for szamlalo in szoveg_sorok_nincsureselem:
    szoveg_sor_split = szamlalo.split()
    for szo in szoveg_sor_split:
        szoveg_szavak_split.append(szo)

szoveg_szavak_piszkok = ['"""', ".", ",", ":", '"', "!", ";", "?", ""]
for p in szoveg_szavak_piszkok:
    for szo in szoveg_szavak_split:
        for b in szo:
            if p == b:
                szoveg_szavak_split.remove(szo)
                szo = szo.replace(p, "")
                szoveg_szavak_split.append(szo)
                break

szoveg_szavak_mindkisbetu = []
for szo in szoveg_szavak_split:
    szoveg_szavak_mindkisbetu.append(szo.lower())

szoveg_szavak_rendezve = szoveg_szavak_mindkisbetu.copy()
szoveg_szavak_rendezve.sort()

szoveg_szavak_set = set(szoveg_szavak_rendezve)

szoveg_szavak_set_rendezve = list(szoveg_szavak_set)
szoveg_szavak_set_rendezve.sort()

szoveg_szavak_darabszam = dict
szoveg_szavak_darabszam = szoveg_szavak_darabszam.fromkeys(szoveg_szavak_set_rendezve)
for k in szoveg_szavak_darabszam.keys():
    szoveg_szavak_darabszam[k] = 0
for szo in szoveg_szavak_rendezve:
    for k in szoveg_szavak_darabszam.keys():
        if szo == k:
            szoveg_szavak_darabszam[k] += 1

szoveg_szavak_kiir = []
for k, v in szoveg_szavak_darabszam.items():
    szoveg_szavak_kiir.append(k)
    szoveg_szavak_kiir.append(v)
for k in szoveg_szavak_kiir:
    print(k, "", end="")
print()

# for i in szoveg_szavak_darabszam.items():
#     print(i)

# szamlalo = 1
# for i in szoveg_szavak_darabszam.items():
#     print(i, "", end="")
#     if szamlalo == 6:
#         szamlalo = 0
#         print()
#     szamlalo += 1
