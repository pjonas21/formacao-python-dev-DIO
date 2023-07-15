import os

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f"Verificando o ip: {ip}")
        os.system(f'ping -n 6 {ip}')
