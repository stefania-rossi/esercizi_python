tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("febbraio", ("mais", 950)),
        ("marzo", ("grano", 1500)),
        ("marzo", ("mais", 700)),
        ("aprile", ("grano", 1600)),
        ("aprile", ("mais", 920)),
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("febbraio", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("marzo", ("grano", 1800)),
        ("marzo", ("mais", 900)),
        ("aprile", ("grano", 1700)),
        ("aprile", ("mais", 820)),
    ]),
     ("Calabria", [
        ("gennaio", ("grano", 1100)),
        ("gennaio", ("mais", 650)),
        ("febbraio", ("grano", 1220)),
        ("febbraio", ("mais", 820)),
        ("marzo", ("grano", 1600)),
        ("marzo", ("mais", 900)),
        ("aprile", ("grano", 1600)),
        ("aprile", ("mais", 720)),
    ]),

)

def analizza_produzione_agricola(nomeRegione, nomeColtura):
    somma=0
    n=0
    max=0
    media=0
    q=0
    mese_max=" "
    mese_maggiore=()
    produzione_agricola=()
    for regione, dati in tupla_produzione_agricola:
        nomeRegione=regione
        for (mese, (coltura, quantità)) in dati:
                if nomeColtura==coltura:
                    somma=somma+quantità
                    n=n+1
                if quantità>max:
                    max=quantità
                    mese_max=mese
    
        media=somma/n
        produzione_agricola=(media,(max, mese_max))
        return produzione_agricola
    
risultato = analizza_produzione_agricola(nomeRegione="Toscana", nomeColtura="grano")
print("Risultato per 'Toscana' e 'grano':", risultato)
