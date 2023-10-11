import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Piloto: {piloto} || Carro: {trajeto}')
        trajeto += velocidade
        time.sleep(0.5)


t_carro1 = Thread(target=carro, args=[1, 'Joao'])
t_carro2 = Thread(target=carro, args=[2, 'Andre'])

t_carro1.start()
t_carro2.start()
