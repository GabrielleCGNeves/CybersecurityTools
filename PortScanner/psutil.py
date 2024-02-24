import psutil
import socket

print("\n>Coletando informações do TCP e UDP")
connectall = psutil.net_connections(kind='inet')
only_udp = [conn for conn in psutil.net_connections(kind='inet') if conn.type == socket.SOCK_DGRAM]

print("\n>Separando informações sobre portas TCP")
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN]

print("\n>Separando informações do portas UDP")
only_udp_listening_ports = [conn.laddr.port for conn in only_udp]

print("\n>Removendo portas repetidas")
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_tcp_listening_ports))

print("\n>Ordenando as portas de forma crescente")
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

print("\n>Mostrando as portas TCP")
for port in only_tcp_listening_ports:
    print(f"Porta TCP = {port} aberta")

print("\n>Mostrando as portas UDP")
for port in only_udp_listening_ports:
    print(f"Porta UDP = {port} aberta.")