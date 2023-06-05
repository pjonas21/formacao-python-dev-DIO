numeros = [1,2,3,4,5,6,7,8,9]
pares = []

# filtro v1 - adicionando itens em uma lista
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

# adicionando itens com apenas uma linha
pares_filtro_v2 = [num for num in numeros if num % 2 == 0]

# adicionando valores a uma lista com for
lista_potencia = []
for num in numeros:
    if num % 2 == 0:
        lista_potencia.append(num ** 2)

# adicionar items na lista com apenas uma linha
lista_potencia_2 = [num ** 2 for num in numeros]

print(pares)
print(pares_filtro_v2)
print(lista_potencia)
print(lista_potencia_2)