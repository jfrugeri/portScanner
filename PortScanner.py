'''
Autor: Juan
* Escaner Básico de Portas *
Desenvolvido durante o curso da Solyd Treinamentos

'''

import socket

ip = str(input("Digite o IP: "))

ports = []
count = 0

while count < 5: # --------------> Colocar número de portas que queira escanear
    port = int(input("Digite a porta: "))
    ports.append(port)
    count += 1

print ("-----------------------------")

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print ("{}{} ->Porta Aberta{}".format('\033[1;32m', port, '\033[m'))
    else:
        print ("{}{} -> Porta fechada{}".format('\033[1;31m', port, '\033[m'))

print ("\nScan Finalizado")