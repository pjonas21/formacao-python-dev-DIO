class Bicicleta:
    # o metodo __init__ define o construtor da classe
    # mesmo que inicializador da classe
    def __init__(self, cor, modelo, ano, valor, aro=18):
        # atributos da classe
        # o self representa a referencia a propria classe
        # essa referencia em Python eh feita de forma explicita
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def __del__(self):
        print("Removendo a instancia da classe...")

    def buzinar(self):
        print('Plim')

    def correr(self):
        print('Vrummmm....')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')

    def __str__(self) -> str:
        # return f"Bicicleta: {self.modelo} | {self.cor} | {self.ano} | R$ {self.valor:.2f}"
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('azul','caloi',2023,800)

b1.correr()
b1.buzinar()
b1.parar()

print(b1.cor, b1.ano, b1.modelo, b1.valor)

b2 = Bicicleta('preta','monark',2023,700)

print(b2)