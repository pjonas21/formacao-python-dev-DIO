carros = {
    'carro_1': {'marca':'vw', 'modelo':'gol', 'ano_fab': 2008, 'cor':'preta'}, 
    'carro_2': {'marca':'fiat', 'modelo':'palio', 'ano_fab': 2009, 'cor':'cinza'}, 
    'carro_3': {'marca':'gm', 'modelo':'celta', 'ano_fab': 2007, 'cor':'branca'}, 
}

copia_carros = carros.copy()
print(copia_carros['carro_1'])

pessoa = {'nome':'Paulo Jonas', 'idade':33}
pessoa.fromkeys(['telefone','endereco'],'vazio')

print(pessoa.get("telefone", {}))
print(carros.get("carro_2"))
print(carros.get("carro_1", {}))

print(carros.keys())

resultado = carros.pop('carro_4', 'nao encontrado')
print(resultado)

resultado_2 = carros.popitem()
print(resultado_2)
print(carros)

# metodo setdefault atribui uma valor padrao para um atributo
# porem caso esse valor ja exista
# retorna o existente
result_set = pessoa.setdefault('nome', 'Jonas')
print(result_set)

pessoa.setdefault('telefone', '85900009999')
print(pessoa)

copia_carros.update({'carro_1':{'marca':'vw', 'modelo':'fox', 'ano_fab': 2015, 'cor':'branca'}} )
print(copia_carros)

print(carros.values())

has_marca = 'marca' in carros['carro_1']
print(has_marca)

# metodo del para apagar uma chave do dicionario
del copia_carros['carro_1']['marca']
print(copia_carros['carro_1'])