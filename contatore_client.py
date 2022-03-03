import socket
import json

HOST="127.0.0.1"
PORT=22007

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #AF_INEF: tipo indirizzo/protocollo usato; la famiglia dell'indirizzo
    #STREAM: TCP. Indica la connessione, per l'appunto
    s.connect((HOST, PORT))
    while True:
        print("Inserisci KO per uscire ")
        messaggio=input("Inserisci una frase ")
        if messaggio=="KO":
            print("connessione terminata")
            break
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode())