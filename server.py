import socket               
import _thread

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        print(msg.decode('utf-8'))
        clientsocket.send(msg)
    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Please, connect to",IPAddr)
host = socket.gethostname()
port = 3030

s.bind((host, port))       
s.listen(5)               

while True:
   c, addr = s.accept()    
   _thread.start_new_thread(on_new_client,(c,addr))
s.close()