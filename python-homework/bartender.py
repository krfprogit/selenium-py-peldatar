# Feladat: Vezérlési szerkezetek gyakorlása
# A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
# Ezen a néven fogadható el a megoldás.
#
# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
# A megoldást egy bartender.py nevű file-ban kell beadnod.
#
# Feladat beadása
# A fent eméített python file-okat és benne a megoldásodat kérlek a saját selenium-py-peldatar
# github repo forkodban egy python-homework nevű mappába helyezd el.

##################################################### MEGOLDAS

while True:
    eletkor = float(input("Kérem adja meg életkorát (nullánál nagyobb szám): "))
    print("Az Ön által megadott életkor:", eletkor)
    if eletkor <= 0:
        print("Kérem egy nullánál nagyobb számot adjon meg!")
    if eletkor > 0:
        break

fogyasztas = "i"
while fogyasztas == "i":
    while True:
        ital = input("Mit szeretne inni? (Kétféle italt ismerünk: sör és kóla) ")
        print("Az Ön által megadott ital:", ital)
        if ital != "sör" and ital != "kóla":
            print("Kérem ezekből adjon meg egyet, csak sört és kólát tudunk adni!")
        if ital == "sör" or ital == "kóla":
            break

    kiskoru_korhatar = 18
    idos_korhatar = 60

    if eletkor < kiskoru_korhatar and ital == "sör":
        print("Sajnos nem adhatok Önnek sört, mert kiskorú!")
    elif eletkor > idos_korhatar and ital == "kóla":
        print("Sajnos a koffein megemelheti a vérnyomását!")
    else:
        if ital == "sör":
            print("Parancsoljon, a söre.")
        else:
            print("Parancsoljon,a kólája.")

    while True:
        fogyasztas = input("Szeretne még egy italt? (i / n)")
        print("Az Ön által megadott válasz:", fogyasztas)
        if fogyasztas != "i" and fogyasztas != "n":
            print("Kérem ezekből adjon meg egyet: 'i' vagy 'n' !")
        if fogyasztas == "n" or fogyasztas == "i":
            break
