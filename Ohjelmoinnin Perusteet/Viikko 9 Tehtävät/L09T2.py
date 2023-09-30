def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")

    while True:
        try:
            valinta = input("Valintasi: ")
            return int(valinta)
        except ValueError:
            print("Anna Valinta kokonaislukuna.")
            continue

def testaaIndex(i):
    lista = [11, 22, 33, 44, 55]
    try:
        print("Listan arvo on", str(lista[i]), "indeksillä", str(i) + ".")
    except IndexError:
        print("Tuli IndexError, indeksi", str(i) + ".")
    return None

def testaaZeroDivision(jakaja):
    try:
        print("4/" + str(jakaja), "on", "{0:.2f}".format(4 / jakaja) + ".")
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja 0.")
    return None

def testaaType(luku):
    try:
        luku * luku
    except TypeError:
        print("Tuli TypeError,", (str(luku) + "*" + str(luku)), "merkkijonoilla ei onnistunut.")
    return None


def paaohjelma():
    while True:
        valinta = valikko()

        if valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.")

        elif valinta == 2:
            indeksi = int(input("Anna indeksi 0-4: "))
            testaaIndex(indeksi)

        elif valinta == 3:
            jakaja = int(input("Anna jakaja: "))
            testaaZeroDivision(jakaja)
        
        elif valinta == 4:
            numero = input("Anna numero: ")
            testaaType(numero)

        elif valinta == 0:
            print("Lopetetaan")
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")

        print()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

