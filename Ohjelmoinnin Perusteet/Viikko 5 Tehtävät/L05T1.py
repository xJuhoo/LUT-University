# Pääohjelma ja aliohjelmat :
def tulostaOhjeet() :
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna nimesi kahdessa osassa.")
    return None

def kysyNimi(kehote) :
    print("Tämä aliohjelma kysyy nimen.")
    nimi = input(kehote)
    return nimi

def tulostaTulokset(etunimi, sukunimi) :
    print("Tämä aliohjelma tulostaa nimesi.")
    print("Hei", etunimi, sukunimi)
    return None

def paaohjelma() :
    tulostaOhjeet()
    etunimi = kysyNimi("Anna etunimi: ")
    sukunimi = kysyNimi("Anna Sukunimi: ")
    tulostaTulokset(etunimi, sukunimi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
