import sys

def paaohjelma():
    luvut = []
    for parametri in sys.argv[1:]:
        try:
            if int(parametri) % 2 == 0:
                luvut.append(int(parametri))
            else:
                continue

        except ValueError:
            pass

    print("Syötteen parilliset luvut ovat seuraavat:")
    for luku in luvut:
        print("{} ".format(luku), end="")

    print()
    try:
        keskiarvo = round(sum(luvut) / len(luvut), 2)
        print("Lukujen keskiarvo on {0:.2f}.".format(keskiarvo))
    except ZeroDivisionError:
        print("Nollalla jako, anna parametreiksi kokonaislukuja.")
    print("Kiitos ohjelman käytöstä.")
    luvut.clear()
    return None

paaohjelma()

