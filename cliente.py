import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host, port))

print("Conectado ao servidor!")

print("Este é um jogo de pedra, papel ou tesoura! Escolha entre: \n0 - Pedra \n1 - Papel \n2 - Tesoura\n")

mensagem = input()
mensagem = mensagem.encode()
s.send(mensagem)

mensagem = s.recv(1024)
mensagem = mensagem.decode()

print(mensagem)