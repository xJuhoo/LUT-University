def tiedostoKirjoita(file) :
    tiedosto = open(file, "w")
    while (True) :
        nimi = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if not nimi :
            break
        else :
            tiedosto.write(nimi + '\n')
    tiedosto.close()
    return None

def tiedostoLue(file) :
    print("Tiedostoon", ("'" + file + "'"), "on tallennettu seuraavat nimet:")
    tiedosto = open(file, "r")
    while (True) :
        nimet = tiedosto.read()
        print(nimet, end = "")
        break
    tiedosto.close()
    return None

def paaohjelma() :
    file = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(file)
    tiedostoLue(file)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
