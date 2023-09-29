def valikko() :
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Määritä askel")
    print("3) Tulosta merkkijono")
    print("0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyMerkkijono() :
    jono = input("Anna merkkijono: ")
    return jono

def kysyAskel() :
    askel = int(input("Anna tulostuksessa käytettävä askel: "))
    return askel

def tulostaMerkkijono(jono, askel) :
    if askel != 0 :
        print(jono[::askel])
    else :
        print(jono)
        for i in range(1, len(jono) + 1) :
            print(jono[:-i])
    return None

def paaohjelma() :
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    while (True) :
        valinta = valikko()
        
        if (valinta == 1) :
            jono = kysyMerkkijono()
        elif (valinta == 2) :
            askel = kysyAskel()
        elif (valinta == 3) :
            tulostus = tulostaMerkkijono(jono, askel)
        elif (valinta == 0) :
            print("Lopetetaan.")
            break
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
