import socket
import json
from threading import Thread

SERVER_ADDRESS='127.0.0.1'   # indirizzo del server 
SERVER_PORT=22224 # porta del server 
class Server():
    def ricevi_comandi(sock_service, addr_client):
        print("avviato")
        while True:
            data=sock_service.recv(1024)
            if not data: #se data è un vettore vuoto usciamo dal ciclo 
                break
            data=data.decode()
            data=json.loads(data) # viene ritrasformato in dizionario se non non può essere ricevuto 
            numero1=data['numero1'] #inserisce il numero 1
            operazione=data['operazione']
            numero2=data['numero2'] # inserisce il numero 2
            ris=""
            if operazione=="+": # se l'operazione da fare è +
                ris=numero1+numero2
            elif operazione=="-": # se l'operazione da fare è -
                ris=numero1-numero2
            elif operazione=="*": # se l'operazione da fare è *
                ris=numero1*numero2
            elif operazione=="/": # se l'operazione da fare è /
                if numero2==0:
                    ris="Impossibile dividere per 0"
                else:
                    ris=numero1/numero2
            elif operazione=="%":
                ris=numero1%numero2
            else:
                ris="Operazione non riuscita"
            ris=str(ris)
            sock_service.sendall(ris.encode("UTF-8"))  # manda il vettore in risposta al client 

        sock_service.close()

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client=sock_listen.accept()
        print("\nConnessione ricevuta da "+str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("il thread non si avvia ")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((indirizzo, porta))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((indirizzo, porta)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)