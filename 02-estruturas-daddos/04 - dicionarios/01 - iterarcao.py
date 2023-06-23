carros = {
    'carro_1': {'marca':'vw', 'modelo':'gol', 'ano_fab': 2008, 'cor':'preta'}, 
    'carro_2': {'marca':'fiat', 'modelo':'palio', 'ano_fab': 2009, 'cor':'cinza'}, 
    'carro_3': {'marca':'gm', 'modelo':'celta', 'ano_fab': 2007, 'cor':'branca'}, 
}

for carro in carros:
    print(carro, carros[carro])

print(10 * '=')

for chave,valor in carros.items():
    print(chave,valor)

