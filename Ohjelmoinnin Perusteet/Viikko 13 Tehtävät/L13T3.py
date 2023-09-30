import sys
import datetime

def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta: ")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot viikonpäivittäin")
    print("0) Lopeta")

    while True:
        try:
            valinta = int(input("Valintasi: ").strip())
        except ValueError:
            print("Anna valinta kokonaislukuna.")
        else:
            break
    
    return valinta

def analysoiTiedot(tiedosto):
    paivat = []
    viikonpaivat = {}
    try:
        luenta = open(tiedosto, "r", encoding="utf-8")
        koko = luenta.readlines()
        for i in range(1, len(koko)):
            rivi = koko[i].replace("\n", "").split(";")
            if len(rivi) >= 1:
                paivat.append(rivi)
            else:
                continue
        luenta.close()

        for rivi in paivat:
            for alkio in rivi:
                if len(alkio) > 1:
                    pvm = datetime.datetime.strptime(alkio, "%A, %d %B %Y, %I:%M %p")
                    if pvm.strftime("%A") not in viikonpaivat:
                        viikonpaivat[pvm.strftime("%A")] = 1
                    else:
                        viikonpaivat[pvm.strftime("%A")] += 1
                else:
                    continue
        paivat.clear()

    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(tiedosto))
        sys.exit(0)

    print("Tiedosto luettu.")
    return viikonpaivat

def tulostaTiedot(sanakirja):
    print(";Palautuksia viikonpäivittäin")
    vkp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    summa = 0
    for i in range(0, 7):
        for viikonpaiva in sanakirja:
            if viikonpaiva == vkp[i]:
                print("{};{}".format(viikonpaiva, sanakirja[viikonpaiva]))
                summa += sanakirja[viikonpaiva]
            else:
                continue
    print("Yhteensä;{}".format(summa))
    return None

def paaohjelma():
    viikonpaivat = {}
    while True:

        valinta = valikko()

        if valinta == 1:
            viikonpaivat.clear()
            tiedosto = input("Anna luettavan tiedoston nimi: ")
            viikonpaivat = analysoiTiedot(tiedosto)
        
        elif valinta == 2:
            tulostaTiedot(viikonpaivat)
        
        elif valinta == 0:
            viikonpaivat.clear()
            print("Lopetetaan.")
            break
        
        else:
            print("Tuntematon valinta, yritä uudelleen.")

        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

