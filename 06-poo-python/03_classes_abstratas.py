from abc import ABC, abstractmethod, abstractproperty

# classe abstrata nao pode ser instanciada
# seus metodos precisam ser declarados dentro das classes filhas
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        print('Ligando...')

    @abstractmethod
    def desligar(self):
        print('Desligando...')

    # podemos declarar propriedades dentro das classes abstratas
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligar...')

    def desligar(self):
        print('desligar...')

    @property
    def marca(self):
        return 'LG'


class ControleAr(ControleRemoto):
    def ligar(self):
        print('ligando ar...')
        print('ligado')

    def desligar(self):
        print('desligando ar...')
        print('desligado')

    @property
    def marca(self):
        return 'Samsung'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleAr()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
