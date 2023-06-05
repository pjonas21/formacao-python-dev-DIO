conjunto_a = {1,2}
conjunto_b = {1,2,4,5}
conjunto_c = {3,4,5}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

print(conjunto_a.issubset(conjunto_b))
print(conjunto_a.issubset(conjunto_c))

print(conjunto_b.issuperset(conjunto_a))
print(conjunto_b.issuperset(conjunto_c))

print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_a.isdisjoint(conjunto_b))

# metodo add - caso o elemnto não exista, ele é adicionado no set (conjunto)
conjunto_a.add(3)
conjunto_a.add(4)
conjunto_a.add(3)
print(conjunto_a)

# metodo clear - utilizado para limpar o conjunto
conjunto_b.clear()
print(conjunto_b)

# metodo copy - gera uma cópia do conjunto
conjunto_b = conjunto_a.copy()
print(conjunto_b)

# metodo discar - usado para eliminar (descartar) um valor presente no conjunto
conjunto_c.discard(3)
conjunto_c.discard(10)
print(conjunto_c)

# metodo pop - retira o primeiro elemento do conjunto
conjunto_c.pop()
print(conjunto_c)

# metodo remove
# se passar um indice que não existe
# é apresentado um erro de key
conjunto_a.remove(1)
print(conjunto_a)
