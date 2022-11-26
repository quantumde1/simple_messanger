import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Please, enter IP of server")
host = input("> ")
s.connect((host, 3030)) # Подключаемся к нашему серверу.
while True:
    message = input("> ")
    s.sendall(message.encode('utf-8')) # Отправляем фразу.
    data = s.recv(1024) #Получаем данные из сокета.