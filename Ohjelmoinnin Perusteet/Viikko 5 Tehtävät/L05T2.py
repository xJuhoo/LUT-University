# Funktio parametreillä :
def tulostaOhjeet() :
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi")
    print("lukujen lukumäärän.")
    return None

def kysyLuku(kehote) :
    luku = int(input(kehote))
    return luku

def vertaileLukuja(x, y) :
    while (True) :
        if x < y :
            pienempi = x
            print("Annetuista luvuista pienempi oli", str(x) + ".")
            break
        elif y == x :
            pienempi = x
            print("Annetuista luvuista pienempi oli", str(x) + ".")
            break
        elif x > y :
            pienempi = y
            print("Annetuista luvuista pienempi oli", str(y) + ".")
            break
    return pienempi

def tulostaTiedot(pienin, lkm) :
    if lkm == 1 :
        print("Annoit yhden luvun, joka oli", str(pienin) + ".")
    else :
        print("Annoit", lkm, "lukua.")
        print("Annetuista luvuista pienin oli", str(pienin) + ".")
    return None

def paaohjelma() :
    tulostaOhjeet()
    print()
    x = kysyLuku("Anna positiivinen kokonaisluku: ")
    lkm = 1
    y = int(input("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): "))
    while (True) :
        if y == 0:
            pienin = pienin
            break
        else :
            lkm += 1
            pienin = vertaileLukuja(x, y)
            if x > y :
                x = int(y)
            else :
                x = int(x)
            y = int(input("Anna uusi positiivinen kokonaisluku (0 lopettaa): "))
    print()
    tulostaTiedot(pienin, lkm)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
