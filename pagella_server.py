import socket
import json

HOST='127.0.0.1'
PORT=65435

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))#tupla: array non modificabile
    s.listen()
    print("[*] In ascolto su %s:%d "%(HOST, PORT))
    #conversione del client
    clientsocket, address=s.accept()#accetta la conversione
    con=1
    while True:
        data=cs.recv(1024)
        print("Connessione da ", address)
        while True:
            data=data.decode()
            data=data.strip()
            print("[*] Received: %s" % data)
            if not data:
                break
            data=data.decode()
            stringa= data
            print("Stringa ricevuta"+stringa)
            if stringa!="KO":
                ris=stringa+""+str(con)
                con+=1
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))

            if data=="#list":
            elif data.find('#get') != -1:
            elif data.find('#put') != -1:
            elif data.find('#set') != -1:
            elif data=="#close" != -1:
            print(cs.getpeername())
            pp=pprint.PrettyPrinter(indent=4)
            pp.pprint(students)
        cs.close()
        
        
        print ("stringa ricevuta"+ stringa)
            if stringa!="KO":
                ris=stringa+" "+str(contatore)
                contatore+=1
            ris=str(ris)
            cs.sendall(ris.encode("UTF-8"))  

        
        

          