######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Juho Rekonen
# Opiskelijanumero:441410
# Päivämäärä: 6.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T3.py

#eof

import datetime

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit")
    print("2) Laske ikä päivinä")
    print("3) Tulosta viikonpäivät")
    print("4) Tulosta kuukaudet")
    print("0) Lopeta")

    valinta = int(input("Anna valintasi: "))
    return valinta

def datanKasittely():
    paiva = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    pvm = datetime.datetime.strptime(paiva, "%d.%m.%Y %H:%M")
    print("Annoit vuoden", int(pvm.strftime("%Y")))
    print("Annoit kuukauden", int(pvm.strftime("%m")))
    print("Annoit päivän", int(pvm.strftime("%d")))
    print("Annoit tunnin", int(pvm.strftime("%H")))
    print("Annoit minuutin", int(pvm.strftime("%M")))
    return None

def laskeIka():
    aika = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ")
    pvm = datetime.datetime.strptime(aika, "%d.%m.%Y")
    vuosi = pvm.strftime("%Y")
    kuukausi = pvm.strftime("%m")
    paiva = pvm.strftime("%d")
    syntyma = datetime.date(int(vuosi), int(kuukausi), int(paiva))
    vertaus = datetime.date(2000, 1, 1)
    erotus = vertaus - syntyma
    print("1.1.2000 henkilö oli", erotus.days, "päivää vanha.")
    return None

def tulostaPaivat():
    pvm = datetime.datetime.strptime("31.10.2022", "%d.%m.%Y")
    for _ in range(1, 8):
        print(pvm.strftime("%A"))
        pvm += datetime.timedelta(days = 1)
    return None

def tulostaKuukaudet():
    pvm = datetime.datetime.strptime("01.01.2022", "%d.%m.%Y")
    for _ in range(1, 13):
        print(pvm.strftime("%b"))
        pvm += datetime.timedelta(days = 31)
    return None

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        valinta = valikko()

        if valinta == 1:
            datanKasittely()
        
        elif valinta == 2:
            laskeIka()

        elif valinta == 3:
            tulostaPaivat()

        elif valinta == 4:
            tulostaKuukaudet()

        elif valinta == 0:
            print("Lopetetaan.")
            break

        else:
            print("Tuntematon valinta, yritä uudelleen.")
        
        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

