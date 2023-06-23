class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f'{"Sim," if self.carregado else "Nao"} estou carregado.')


moto = Motocicleta('preta', 'ABC1234', 2)
print('Moto: ', end='')
moto.ligar_motor()

carro = Carro('vermelha', 'ABD2345', 4)
print('Carro: ', end='')
carro.ligar_motor()

caminhao = Caminhao('verde', 'JKL7890', 6, False)
print('Caminhao: ', end='')
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
