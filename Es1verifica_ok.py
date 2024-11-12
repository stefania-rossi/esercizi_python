tupla_competizioni = (
    ("Marco", "Carbonara", 8.5, 5),
    ("Luigi", "Lasagna", 7.2, 4 ),
    ("Fabio", "Parmigiana", 9.0, 6),
    ("Marco", "Amatriciana", 7.8, 5 ),
    ("Luigi", "Risotto", 8.1, 4),
)

def media_punteggio_competizioni(tupla_competizioni):
    n=0
    somma=0
    for nome, piatto, punteggio, giudici in tupla_competizioni:
        somma+=punteggio
        n+=1
    return somma/n




def media_punteggio_chef(tupla_competizioni,chef):
    somma=0
    n=0
    for nome,piatto, punteggio, giudici in tupla_competizioni:
        if chef==nome:
            somma+=punteggio
            n+=1
    return somma/n



def competizione_con_più_giudici(tupla_competizioni):
     max=0
     competizione_maggiore= ()
     for nome,piatto, punteggio, giudici in tupla_competizioni:
         if giudici>max:
            max=giudici
            competizione_maggiore=((nome, piatto, punteggio, giudici))

     return competizione_maggiore



def competizione_con_meno_giudici(tupla_competizioni):
     min=100
     competizione_minore= ()
     for nome,piatto, punteggio, giudici in tupla_competizioni:
         if giudici<min:
            min=giudici
            competizione_minore=((nome, piatto, punteggio, giudici))
     return competizione_minore

while True:
    print("Menù: \n 1. calcola media punteggi \n 2 calcola media punteggio di uno chef \n 3 trova competizione con più giudici \n 4 trova competizione con meno giudici: \n inserisci 0 per terminare")
    scelta= int(input("inserisci quale comando vuoi eseguire: "))
            
    if (scelta==1):
        print (f"la media del punteggio totale è: {media_punteggio_competizioni(tupla_competizioni)} ")
    if(scelta==2):
            chef = str(input("inserisci il nome di uno chef: "))
            print (f"la media del punteggio dello chef richiesto è: {media_punteggio_chef(tupla_competizioni,chef)}")
    if(scelta==3):
            print (f"la competizione col numero maggiore di giudici è: {competizione_con_più_giudici(tupla_competizioni)}")
    if(scelta==4):
        print (f"la competizione col numero minore di giudici è: {competizione_con_meno_giudici(tupla_competizioni)}")
    if(scelta>4 or scelta<1):
        print("il comando selezionato è inesistente/programma terminato")
        break

 






         



 

