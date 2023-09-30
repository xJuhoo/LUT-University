def kysyLuku():
    # Tarkistetaan käyttäjän syöte merkkijonojen varalta
    while True:
        try:
            luku = int(input("Anna kuukausien lukumäärä: ").strip())
        except ValueError:
            print("Anna kokonaisluku.")
        else:
            break
    
    return luku

def Fibonacci(luku, dict):
    if luku in dict:
        return dict[luku]
    if (luku <= 2):
        return 1
    dict[luku] = Fibonacci(luku - 1, dict) + Fibonacci(luku - 2, dict)
    return dict[luku]
    

def paaohjelma():
    dict = {}
    # Kysytään käyttäjältä kuukausien määrä
    kuukaudet = kysyLuku()
    # Tarkistetaan, jos käyttäjän antama luku on ei-positiivinen  
    lukumaara = Fibonacci(kuukaudet, dict)
    print("Kanipariskuntia on", kuukaudet, "kuukauden kuluttua", lukumaara)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
