pessoa = {'nome':'Paulo Jonas', 'idade':33}

print(pessoa)
print(pessoa['idade'])

pessoa['telefone'] = '85991232589'
print(pessoa)

pessoa['endreco_comercial'] = {'rua_av':'Av Luciano Magalhaes', 'numero':'1251'}
print(pessoa)

print(pessoa['endreco_comercial']['rua_av'])

pessoa_2 = dict(nome='Joao',idade=23,telefone='85990909090')
print(pessoa_2)