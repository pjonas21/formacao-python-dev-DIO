import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server socket criado com sucesso')

host = 'localhost'
porta = 5434

s.bind((host, porta))
msg = '\nServidor: Tudo ok!'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (msg.encode()), end)