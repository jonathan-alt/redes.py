import socket

server_socket = socket.socket()
server_socket.bind(('10.39.0.3', 5000)) 

server_socket.listen(2)
conn, address = server_socket.accept() 

lista_inteiros = []
while True:

    resposta = conn.recv(2000).decode()

    if resposta .isdigit():
        inteiro = int(resposta )
        lista_inteiros.append(inteiro)
        if len(lista_inteiros) < 2:
            print(lista_inteiros)
            data = 'Digite novamente'
            conn.send(data.encode()) 
        else:
            soma = 0
            for i in lista_inteiros:
                soma += i
            data = 'a soma dos dois digitos foi: ' + str(soma)
            conn.send(data.encode()) 
            lista_inteiros = []
    else:
        data = 'Você não digitou um valor inteiro'
        conn.send(data.encode())

conn.close()
