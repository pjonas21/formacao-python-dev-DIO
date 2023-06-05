'''
tuplas são parecidas com as listas,
porém são imutáveis, não permitindo sua alteração

utiliza-se a classe tuple ou colocando os valores
separados por vírgulas e parênteses

boa prática adicionar uma vírgula no final da
declaração de uma tupla, que contenha apenas
um valor, para que o Python não se perca ao
identificar como uma precedência
'''

frutas = ('laranja','maçã','uva',)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ('Brasil',)

print(frutas[0])

# tuplas aninhadas
matriz = (
    (1,'a',2),
    ('b',3,4),
    (6,5,'c'),
)

print(matriz[0])
print(matriz[-1])
print(matriz[0][-2])
print(matriz[-1][-1])

# as formas de acesso são as mesmas da lista
