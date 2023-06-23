class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # convenção para deixar uma variável privada
        # iniciar variavel com underline "_"
        self._saldo = saldo 
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        # maneira correta de acessar uma variável privada
        # ... verificações para exibir o valor da vareiável
        return self._saldo


conta = Conta('1302', 100)
print(conta.mostrar_saldo())
conta.depositar(150)
print(conta.mostrar_saldo())

