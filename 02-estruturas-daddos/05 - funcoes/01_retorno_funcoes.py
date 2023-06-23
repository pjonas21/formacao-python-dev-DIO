def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

resultado_1 = calcular_total([1,3,6,9,12])
resultado_2 = retorna_antecessor_sucessor(56)

print(resultado_1)
print(resultado_2)