print("Tämä ohjelma laskee risteilyhintoja.")
hyttiA = round(float(79 * 1.60))
hyttiB = round(float(79 * 1.10))
hyttiC = round(float(79))
valinta = input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
if valinta == "A" or valinta == "a" :
    sesonki = input("Onko sesonkiaika (k/e): ")
    if sesonki == "K" or sesonki == "k" :
        hyttiA = hyttiA * 2.75
    else :
        hyttiA = hyttiA
    kanta = input("Onko kanta-asiakas (k/e): ")
    if kanta == "K" or kanta == "k" :
        hyttiA = hyttiA * 0.90
    else :
        hyttiA = hyttiA
    print("A-hytti maksaa", round(float(hyttiA), 2), "euroa.")
elif valinta == "B" or valinta == "b" :
    sesonki = input("Onko sesonkiaika (k/e): ")
    if sesonki == "K" or sesonki == "k" :
        hyttiB = hyttiB * 1.75
    else :
        hyttiB = hyttiB
    kanta = input("Onko kanta-asiakas (k/e): ")
    if kanta == "K" or kanta == "k" :
        hyttiB = hyttiB * 0.90
    else :
        hyttiB = hyttiB
    print("B-hytti maksaa", round(float(hyttiB), 2), "euroa.")
elif valinta == "C" or valinta == "c" :
    sesonki = input("Onko sesonkiaika (k/e): ")
    if sesonki == "K" or sesonki == "k" :
        hyttiC = hyttiC * 1.50
    else :
        hyttiC = hyttiC
    kanta = input("Onko kanta-asiakas (k/e): ")
    if kanta == "K" or kanta == "k" :
        hyttiC = hyttiC * 0.90
    else :
        hyttiC = hyttiC
    print("C-hytti maksaa", round(float(hyttiC), 2), "euroa.")
else :
    print("Tuntematon valinta.")
print("Kiitos ohjelman käytöstä.")
