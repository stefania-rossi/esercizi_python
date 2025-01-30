from multiprocessing import Process

"""
multiprocessing è una libreria per la creazione, la comunicazione e la sincronizzazione
tra processi nella programmazione parallela e concorrente.
Process è una classe per creare processi eseguendo una funzione (o metodo) specificata come target.
"""

# Definisce una funzione 
def process_function(data):
    result = data * 2  # Moltiplica il valore per 2
    print(result)  # Stampa il risultato

if __name__ == "__main__":
    data_list = [1, 2, 3, 4]  # Lista di numeri 
    processes = []  # Lista per memorizzare i vari processi

    # Crea e avvia un processo per ogni elemento nella lista
    for data in data_list:
        p = Process(target=process_function, args=(data,))  # nuovo processo
        processes.append(p)  #aggiunta del processo alla lista
        p.start() # Avvio del processo inseriti

    # Attende che tutti i processi terminino
    for p in processes:
        p.join()  # Blocca l'esecuzione del programma principale fino al termine del processo