def paaohjelma():
    tiedosto = input("Anna tiedoston nimi: ")
    luenta = open(tiedosto, "r", encoding = "utf-8")
    print("Kalastuskilpailun tulokset ovat seuraavat:")
    koko = luenta.readlines()
    for i in range(0, len(koko)):
        rivi = koko[i].replace("\n", "")
        if "Joukkkue" not in rivi: # Skipataan ensimmäinen rivi.
            lista = rivi.split(";")
            print("Joukkue", ("'" + lista[0] + "'"), "sai kalan", lista[1] + ",", "joka oli", lista[2], "cm.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
    
    
