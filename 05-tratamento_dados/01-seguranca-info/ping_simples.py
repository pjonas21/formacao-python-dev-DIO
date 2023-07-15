import os

print("#" * 60)

ip_host = input("Digite o IP ou HOST para verificar: ")

os.system(f'ping -n 6 {ip_host}')

print("#" * 60)
