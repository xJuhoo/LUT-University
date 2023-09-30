def kysyLuku():
    # Tarkistetaan käyttäjän antama syöte merkkijonojen varalta
    while True:
        try:
            luku = int(input("Anna luku: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def neliojuuri(luku):
    # Tarkistetaan, onko annettu luku 1
    if luku == 1:
        return luku
    else:
        aloitus = 1
        askel = 0.5
        while aloitus < luku ** 0.5:
            aloitus += askel
    
    return aloitus

def paaohjelma():
    # Kysytään käyttäjältä luku
    luku = kysyLuku()
    nelio = neliojuuri(luku)
    print("Neliöjuuri on", round(nelio))
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

