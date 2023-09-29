PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'

def tulostaOhjeet() :
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään", PITUUS_MIN, "ja korkeintaan", PITUUS_MAX, "merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä", ("'" + EROTIN + "'."))
    return None

def kysyMerkkijono(kehote) : # Muokataan pääohjelmassa ainoastaan kehote osaa, muu print -lause pysyy samana.
    merkkijono = input("Anna " + kehote + "merkkijono 5-15 merkkiä (enter lopettaa): ")
    return merkkijono

def tarkistaMerkkijono(jono) :
    while (True) :
        if EROTIN in jono :
            print("Merkkijonossa on kielletty merkki", ("'" + EROTIN + "'."))
            jono = "hylätty"
            break
        elif len(jono) < PITUUS_MIN :
            print("Liian lyhyt,", len(jono), "merkkiä.")
            jono = "hylätty"
            break
        elif len(jono) > PITUUS_MAX :
            print("Liian pitkä,", len(jono), "merkkiä.")
            jono = "hylätty"
            break
        else : # Jos tässä vaiheessa kaikki edelliset tarkistukset menneet läpi, merkkijono hyväksytään.
            jono = "hyväksytty"
            break
    return jono   # Palauttaa joko arvon 'hylätty' tai 'hyväksytty'.

def tulostaHyvaksytyt(nimet) :
    print("Annoit seuraavat hyväksytyt merkkijonot:")
    nimet = nimet[:len(nimet) - 1] # Tämä komento poistaa viimeisen ';' merkin merkkijono lopusta.
    print(nimet.replace(";", "\n")) # Replace-komennon avulla vaihdetaan kaikki ';' merkit rivinvaihdoksi.
    return None
    
def paaohjelma() :
    tulostaOhjeet()
    print()
    jono = kysyMerkkijono("")
    nimet = "" # Luodaan hyväksyttyjen nimien parametriksi tyhjä merkkijono.
    while (True) :
        if not jono : # Looppi loppuu jos käyttäjä painaa Enter- näppäintä.
            print()
            break
        elif tarkistaMerkkijono(jono) == "hylätty" :
            jono = kysyMerkkijono("uusi ")
        elif tarkistaMerkkijono(jono) == "hyväksytty" :
            nimet = nimet + jono + ";" # Kun luku hyväksytään, se lisätään 'nimet' parametriin.
            jono = kysyMerkkijono("seuraava ")
    if nimet == "" : # Jos nimet parametri pysyy samana kuin alussa, ei käyttäjä antanut yhtään hyväksyttyä nimeä.
        print("Et antanut yhtään hyväksyttyä merkkijonoa.")
    else :
        tulostaHyvaksytyt(nimet) 
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
