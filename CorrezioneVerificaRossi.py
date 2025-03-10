import random

concorso = {
  "Rossi Mario": [("Antipasti",(8,7,9),"Junior Chef"), ("Primi",(7,8,8),"Junior Chef"), ("Secondi",(9,9,8),"Junior Chef"),("Dessert",(8,8,9),"Junior Chef")],
  "Bianchi Luigi": [("Antipasti",(7,7,8),"Senior Chef"), ("Primi",(8,9,7),"Senior Chef"), ("Secondi",(7,8,7),"Senior Chef"),("Dessert",(9,8,8),"Junior Chef")],
  "Verdi Giulia": [("Antipasti",(9,8,8),"Junior Chef"), ("Primi",(8,7,9),"Junior Chef"), ("Secondi",(8,8,8),"Junior Chef"),("Dessert",(7,9,8),"Junior Chef")]
}

concorso["Rossi Stefania"]=[("Antipasti",(8,8,8),"Junior Chef"), ("Primi",(7,10,8),"Junior Chef"), ("Secondi",(9,9,9),"Junior Chef"),("Dessert",(7,8,9),"Junior Chef")]



def aggiungi_piatti_unici():
    for chef in concorso.keys():
         concorso[chef] += [("Piatti Unici",((random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10))),"Junior Chef")]

def stampa_dati_di_uno_chef():
    chef=str(input("Inserisci il cognome e nome dello chef che desideri visualizzare:"))
    while chef not in concorso.keys():
        chef=str(input("chef inserito non presente! , reinserisci:"))
    valori=concorso[chef]
    print("chef: " ,chef)
    print("categoria dello chef:" ,valori[0][2])
    for valore in valori:
         print
         print("-Categoria piatto: ", valore[0])
         print("-Punteggi: ")
         print(valore[1])
         print("-Creatività: ")
         print(valore[1][0])
         print("-Gusto: ")
         print(valore[1][1])
         print("-Presentazione: ")
         print(valore[1][2])

def stampa_un_piatto(concorso):
   categoria=int(input("inserisci la categoria dei piatti che vuoi visualizzare: [1] antipasti, [2] primi, [3]secondi,[4] dessert"))
   while categoria < 1 or categoria > 4:
      concorso = int(input("categoria inserita non valida, reinserisci!"))
   for chef in concorso.keys():
      valori=concorso[chef]
      if categoria == 1:
        print(f"piatto di {chef}: {valori[0]}")
      if categoria == 2:
         print(f"piatto di {chef}: {valori[1]}")
      if categoria == 3:
         print(f"piatto di {chef}: {valori[2]}")
      if categoria == 4:
         print(f"piatto di {chef}: {valori[3]}")
   


""" 

richiesta 1: popolamento statico corretto
richiesta 2: aggiunta statica di un nuovo chef
richiesta 3: aggiunta nuova categoria piatto funzionante, categoria dello chef non differenziata.
richiesta 4: stampa di uno chef funzionante
richiesta 5: stampa di un piatto funzionante
richiesta 6 A: mancante
richiesta 6 B: mancante
richiesta 7: mancante

"""