import numpy

def paaohjelma():
    print("Tämä ohjelma testaa numpy-matriisin käyttöä.")
    # Merkitään matematiikasta tutulla tyylillä matriisia isolla kirjaimella
    A = numpy.zeros((4, 4), int)
    for rivi in range(4):
        for sarake in range(4):
            A[rivi][sarake] = (rivi + 1) * (sarake + 1)

    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(A)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in range(4):
        for sarake in range(4):
            print(A[rivi][sarake], end = ";")
        print()
    print()
    A = numpy.delete(A, numpy.s_[:], None)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

