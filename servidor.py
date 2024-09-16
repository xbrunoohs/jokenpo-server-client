import socket
import threading
import random
import jokenpo
import time

def gerir_cliente(conn, addr):

    #receber mensagem
    jogada_cliente = conn.recv(1024)
    jogada_cliente = int(jogada_cliente.decode())

    jogada_servidor = jogada_aleatoria()

    resultado = jokenpo.jokenpo_logica(jogada_cliente, jogada_servidor)

    resultado_final = mensagem_resultado(resultado, jogada_servidor)

    #sleep só para simular um tempo maior de processamento
    time.sleep(2)

    resultado_final = resultado_final.encode()

    #mandar mensagem
    conn.send(resultado_final)
    
    #fechar a conexão
    conn.close()

def jogada_aleatoria():
    return random.randint(0, 2)

def mensagem_resultado(resultado, jogada_servidor):
    return "Jogada do servidor: " + jokenpo.JOKENPO_DICTIONARY[jogada_servidor] + "\nResultado: " + resultado

#-------conexão com o socket-------#

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((host, port))
s.listen(5)

all_threads = []

try:
    while True:
        print("Esperando jogada")
        conn, addr = s.accept()
        
        t = threading.Thread(target=gerir_cliente, args=(conn, addr))
        t.start()
    
        all_threads.append(t)
except KeyboardInterrupt:
    print("Interrompido com Ctrl+C")
finally:
    if s:
        s.close()
    for t in all_threads:
        t.join()
