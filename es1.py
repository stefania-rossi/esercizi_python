
dati = (
    
    ("Milano", [("gennaio",6 ),("febbraio", 12),("Giugno", 2)]),
    ("Como", [("gennaio",3 ),("febbraio", 4),("Giugno", 1)]),
    ("Monza", [("gennaio",4 ),("febbraio", 6),("Giugno", 2)]),
    ("Mantova", [("gennaio",7 ),("febbraio", 9),("Giugno", 3)])

)


def datiPrecipitazioni(nome):
    for città , *rilevazione in dati:
        if (nome==città):
            print(rilevazione)
            somma=0
            max=0
            min=500
            mesiMax=[]
            mesiMin=[]
            for mese, valore in rilevazione:
                somma += valore
                if(valore>max):
                    max=valore
                if(valore<min):
                    min=valore
            for mese, valore in rilevazione:
                if(max==valore):
                    mesiMax.append(mese)
                if(min==valore):
                    mesiMin.append(mese)
            



            #print(somma/len(rilevazione))
            #print("max", max)
            #print("min", min)
            #print("Mese Max", mesiMax)
            #print("Mesi min", mesiMin)
        if(somma==0):
         return print("La tupla non esiste")
        else:
         return (somma/len(rilevazione),(max, mesiMax),(min,mesiMin))
    
        

nome=input("inserisci il nome di una città:   ")
datiPrecipitazioni(nome)