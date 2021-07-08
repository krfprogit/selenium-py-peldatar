# 010 Feladat: Python lista gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# . Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
# amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
# majd írja ki a képernyőre a lista elemeit fordított sorrendben!
# A megoldást egy fordito.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar github repo forkodban
# egy python2-homework nevű mappába helyezd el.

######################################################## MEGOLDAS

print("A felhasználótól pozitív számokat kérek be mindaddig, amíg a felhasználó nullát nem ad be!")
szamok = []
while True:
    while True:
        try:
            szam = float(input("Kérem adjon meg egy pozitív számot! "))
            if szam <= 0:
                break
            szamok.append(szam)
        except:
            print("Csak pozitív számot fogadok el!")
            print("Kilépéshez nyomja meg a nullát!")
    if szam == 0:
        break
    print("Csak pozitív számot fogadok el!")
    print("Kilépéshez nyomja meg a nullát!")

szamok.reverse()
print("A lista elemei fordított sorrendben:")
print(szamok)
