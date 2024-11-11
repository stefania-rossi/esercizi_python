datiMensili = [
    ("Milano", [("Gennaio", 10), ("Febbraio", 14), ("Marzo", 12), ("Aprile", 4),
                ("Maggio", 5), ("Giugno", 9), ("Luglio", "none"), ("Agosto", 12),
                ("Settembre", 22), ("Ottobre", 20), ("Novembre", 20), ("Dicembre", 24)]),
    ("Bergamo", [("Gennaio", 3), ("Febbraio", 7), ("Marzo", 1), ("Aprile", 6),
                 ("Maggio", 10), ("Giugno", 10), ("Luglio", "none"), ("Agosto", "none"),
                 ("Settembre", "none"), ("Ottobre", 13), ("Novembre", 19), ("Dicembre", 2)]),
    ("Como", [("Gennaio", 11), ("Febbraio", 15), ("Marzo", 15), ("Aprile", 16),
              ("Maggio", 1), ("Giugno", "none"), ("Luglio", "none"), ("Agosto", "none"),
              ("Settembre", 9), ("Ottobre", 10), ("Novembre", 24), ("Dicembre", "none")])
]

def analisiDati(nomeCitta, datiMensili):
    meseMax = ""
    meseMin = ""
    valoreMax = 0
    valoreMin = 1000
    media = 0
    somma = 0
    i = 0

    # Media
    for citta, dati in datiMensili:
        if(nomeCitta == citta):
            for mese, valore in dati:
                if (valore != "none"):
                    somma += valore
                    i+=1
                    # Min
                    if(valore<valoreMin):
                        meseMin = mese
                        valoreMin = valore
                    # Max
                    if(valore>valoreMax):
                        meseMax = mese
                        valoreMax = valore
    media = somma/i

    return (media, (valoreMax, meseMax), (valoreMin, meseMin))

while True:
    nomeCitta = str(input("Inserisci il nome di una città da analizzare: "))
    ciclo = False
    for citta, dati in datiMensili:
        if(citta==nomeCitta):
            ciclo = True
            break
    if (ciclo==True):
        break
    else:
        print("Nome città inserito non valido.")

print(analisiDati(nomeCitta, datiMensili))



