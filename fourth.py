def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.[cite: 2]

    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})[cite: 2]
    :param cilova_pozice: N-tice (řádek, sloupec)[cite: 2]
    :param obsazene_pozice: Množina obsazených pozic[cite: 2]
    :return: True, pokud je tah možný, jinak False[cite: 2]
    """
    aktualni_pozice = figurka["pozice"][cite: 2]
    typ = figurka["typ"][cite: 2]

    c_radek, c_sloupec = cilova_pozice
    a_radek, a_sloupec = aktualni_pozice

    if not (1 <= c_radek <= 8 and 1 <= c_sloupec <= 8):
        return False

     if cilova_pozice in obsazene_pozice:
        return False


    rozdil_radku = abs(c_radek - a_radek)
    rozdil_sloupcu = abs(c_sloupec - a_sloupec)

    if typ == "král":
    
        if rozdil_radku <= 1 and rozdil_sloupcu <= 1 and (rozdil_radku > 0 or rozdil_sloupcu > 0):
            return True

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L (např. rozdíl řádků je 2 a sloupců 1, nebo naopak).
        if (rozdil_radku == 2 and rozdil_sloupcu == 1) or (rozdil_radku == 1 and rozdil_sloupcu == 2):
            return True

    return False
