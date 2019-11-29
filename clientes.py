import socket

client_socket = socket.socket() 
client_socket.connect(('10.39.2.2', 5000))

digite= input()  # recebe um valor

while True:
    client_socket.send(digite.encode())
    resposta = client_socket.recv(2000).decode() 

    print(resposta ) 

    digite= input()

client_socket.close()