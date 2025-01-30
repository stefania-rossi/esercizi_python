import os  #import os
from multiprocessing import Process, current_process, Pipe  # Import Process, current_process e Pipe

#stampa ID del processo
def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")


def process_function(conn):
    process_id()  # Stampa infor
    print("Elaboro il dato ricevuto ed invio il risultato")
    data_received = conn.recv()  # Riceve il dato 
    result = data_received * 2  # moltiplica per 2
    conn.send(result)  # Invia il risultato 
    conn.close()  # Chiude la connessione 

if __name__ == "__main__":
    process_id()  # Stampa info
    print("Creo una connessione e un processo figlio")

    parent_conn, child_conn = Pipe()  # Crea una Pipe per com tra processi
    data = 5  # Dato

    p = Process(target=process_function, args=(child_conn,))  # Crea il processo child
    p.start()  # Avvia il processo 

    parent_conn.send(data)  # Invia il dato al processo child
    result = parent_conn.recv()  # Riceve il risultato 
    p.join()  # Attende il termine

    process_id()  # Stampa info
    print("Stampo il risultato ricevuto")  
    print(result)  # Stampa risultato