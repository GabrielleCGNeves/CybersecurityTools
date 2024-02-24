#Objetivo do Código: Usar a biblioteca socket para escanear portas abertas no endereço

import socket

def scan_ports(host, ports_to_scan):
    print(f"Escaneando {host}")
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Porta {port}: ABERTA")
        s.close()

host = "fateczonasul.edu.br"
ports_to_scan = range(20, 1024)
scan_ports(host, ports_to_scan)

#Identifique função no Framework de Cibersegurança do NIST
# > Plan e ACT
# > ID.RA ID.RM e DE.CM