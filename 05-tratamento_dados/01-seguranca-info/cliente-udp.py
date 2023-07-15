import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso')

host = 'localhost'
porta = 5433
msg = 'Olá servidor. Tudo ok?'

try:
    print(f'Cliente: {msg}')
    s.sendto(msg.encode(), (host, 5434))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()

    print(f'Cliente: {dados}')
finally:
    print(f'Cliente: Fechando conexão.')
    s.close()
