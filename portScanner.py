'''
Autor: Juan
* Escaner Básico de Portas *
Desenvolvido durante o curso da Solyd Treinamentos
'''

import socket

def get_ip():
    return input("Digite o IP: ")

def get_ports():
    ports = []
    num_ports = int(input("Quantas portas você quer escanear? "))
    for _ in range(num_ports):
        port = int(input("Digite a porta: "))
        ports.append(port)
    return ports

def scan_ports(ip, ports):
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        code = client.connect_ex((ip, port))
        if code == 0:
            print(f"\033[1;32m{port} -> Porta Aberta\033[m")
        else:
            print(f"\033[1;31m{port} -> Porta Fechada\033[m")

def main():
    ip = get_ip()
    ports = get_ports()
    print("-----------------------------")
    scan_ports(ip, ports)
    print("\nScan Finalizado")

if __name__ == "__main__":
    main()
