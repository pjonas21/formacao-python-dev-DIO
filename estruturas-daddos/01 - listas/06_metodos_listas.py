lista = list(range(6))
print(lista)

lista.append(6)
print(lista)

#metodo copy - copia uma lista
# o que fizer em lista_2 não reflete na lista original
lista_2 = lista.copy()
print(lista_2)

print(id(lista), id(lista_2))

# metodo count - contar quantas vezes um valor ocorre em uma lista
lista_cores = ['vermelho', 'azul', 'azul', 'verde']
print(lista_cores.count('azul'))

# metodo extend - unir listas
# sem alterar o conteúdo
lista_linguagens = ['python','java']
lista_linguagens.extend(['javascript','c-sharp','c++','java'])
print(lista_linguagens)

# metodo index - resgatar o indice de um valor presente na lista
# trazendo o indice da primeira ocorrencia do valor na lista
print(lista_linguagens.index('java'))

# metodo pop - retirar itens de uma lista
lista_linguagens.pop() # retira o ultimo item da lista
lista_linguagens.pop(2) # retira o item com indice 1 da lista
print(lista_linguagens)

# metodo remove - passa o valor a ser retirado da lista
lista_linguagens.remove('c++')
print(lista_linguagens)

# metodo reverse - espelhamento de lista
lista_linguagens.reverse()
print(lista_linguagens)

# metodo sort - ordenar os valores da lista
linguagens = ['python','c','js','java','kotlin','swift']
linguagens.sort()
print(linguagens)
linguagens.sort(reverse=True)
print(linguagens)
# ordena por tamanho de cada palavra
# passando uma função anônima - lambda
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# metodo len
print(len(linguagens))

# função já inclusa na linguagem - builtin
# sorted
linguagens_2 = ["python", "c", "js", "java", "csharp"]
print(sorted(linguagens_2, key=lambda x: len(x)))
print(sorted(linguagens_2, key=lambda x: len(x), reverse=True))
print(sorted(linguagens_2))

lista_numero = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lista_numero)


