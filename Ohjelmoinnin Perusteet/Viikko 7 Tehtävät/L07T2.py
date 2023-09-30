class TILI:
    Nimi = ""
    Saldo = 0


def kysyTiedot(hlo):
    hlo.Nimi = input("Anna pankkitilin nimi: ")
    hlo.Saldo = round(float(input("Anna pankkitilin saldo: ")), 2)
    return hlo.Nimi, hlo.Saldo

def tallennaTiedot(nimi, saldo):
    print("Pankkitilillä", ("'" + nimi + "'"), "on nyt rahaa", str(saldo) + "e.")
    return None

def paaohjelma():
    hlo = TILI()
    tilitiedot = kysyTiedot(hlo)
    tallennaTiedot(tilitiedot[0], tilitiedot[1])
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

    
    
