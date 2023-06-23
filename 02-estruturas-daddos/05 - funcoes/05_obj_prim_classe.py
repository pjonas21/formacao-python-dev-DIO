def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operacao {a} + {b} = {resultado}")


exibir_resultado(34,56,somar)

# objetos de primeira classe nos permitem lhes atribuir a variaveis
op = somar

print(op(23,45))