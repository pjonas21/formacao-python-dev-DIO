import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as err:
        print('A conexão falhou.')
        print(f'Erro: {err}')
        sys.exit()

    print('Socket criado com sucesso!')

    host_alvo = input('Digite o host ou IP para conectar: ')
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))

        print('Cliente TCP conectado com sucesso.')
        print(f'Host: {host_alvo} || Porta: {porta_alvo}')
        s.shutdown(2)
    except socket.error as err:
        print('A conexão falhou.')
        print(f'Não foi possível conectar no {host_alvo}:{porta_alvo}')
        print(f'Erro: {err}')
        sys.exit()

if __name__ == "__main__":
    main()
