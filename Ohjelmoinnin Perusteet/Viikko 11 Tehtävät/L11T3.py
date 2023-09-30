def kysyLuku():
    # Tarkistetaan käyttäjän syöte merkkijonon varalta
    while True:
        try:
            luku = int(input("Anna tulostuskertojen määrä: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def tulostus(sana, luku):
    if luku != 0:
        tulostus(sana, luku - 1)
        print("Sana on", ("'" + sana + "',"), (str(luku) + "."), "kerta.")
    return None

def paaohjelma():
    # Kysytään käyttäjältä tulostettava merkkijono
    sana = input("Anna tulostettava sana: ")
    # Kysytään käyttäjältä luku
    luku = kysyLuku()
    tulostus(sana, luku)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

