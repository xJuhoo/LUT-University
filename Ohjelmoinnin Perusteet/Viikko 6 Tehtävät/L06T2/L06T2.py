def laskuri(tiedosto) :
    nimet = len(tiedosto.readlines())
    tiedosto.seek(0)
    merkit = len(tiedosto.read())
    tiedosto.seek(0)
    nimimerkit = len(tiedosto.read().replace("\n", ""))
    return nimet, merkit, nimimerkit

def paaohjelma() :
    file = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(file, "r", encoding="utf-8")
    arvot = laskuri(tiedosto)
    keskiarvo = round((arvot[2] / arvot[0]),0)
    print("Tiedostossa oli", arvot[0], "nimeä ja", arvot[1], "merkkiä.")
    print("Keskimäärin nimen pituus oli", "{0:.0f}".format(keskiarvo), "merkkiä.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

    
