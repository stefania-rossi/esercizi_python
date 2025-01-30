from multiprocessing import Process, Queue  # Import Process e Queue
import os  # Import os
from multiprocessing import current_process  # Import current_process 

"""
Queue: classe che rappresenta una coda condivisa tra processi.
È utilizzata per consentire la comunicazione tra processi,
consentendo loro di scambiarsi dati in modo sicuro.
put(item): Aggiunge un elemento alla coda.
get(): Rimuove e restituisce un elemento dalla coda.
empty(): restituire true se la coda è vuota, altrimenti restituisce false
full():restituisce true se la coda è piena, altrimenti restituisce false.
qsize(): restituisce il numero di elementi  presenti nella coda.
close():chiude la coda.
"""

# stampa ID del processo
def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(data, result_queue):
    process_id()  # Stampa infor sul processo
    print("Elabora: ", data)  # Stampa il dato 
    result = data * 2  # Moltiplica per 
    result_queue.put(result)  # Inserisce il risultato nella coda

if __name__ == "__main__":
    data_list = [1, 2, 3, 4]  # Lista di dati 
    result_queue = Queue()  # coda per  i risultati
    processes = []  # Lista per  i processi


    for data in data_list:
        p = Process(target=process_function, args=(data, result_queue))  # Crea il processo
        processes.append(p)  # Aggiunge il processo alla lista
        p.start()  # Avvia il processo

    # Attende la termina di tutto
    for p in processes:
        p.join()

    print("Il main stampa i risultati") 
    while not result_queue.empty():  # Finché la coda non è vuota
        result = result_queue.get()  # Estrae  risultato 
        print(result)  # Stampa