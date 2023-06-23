nome = 'Paulo'
idade = 33
profissao = 'Programador'
linguagem = 'Python'

# old style
print("Olá, me chamo %s. Eu tenho %d anos. Trabalho como %s e utilizo a linguagem %s" % (nome, idade, profissao, linguagem))

# métofo format
print("Olá, me chamo {}. Eu tenho {} anos. Trabalho como {} e utilizo a linguagem {}".format(nome, idade, profissao, linguagem))

# f string
print(f"Olá, meu nome é {nome}, tenho {idade} anos. Sou {profissao} e utilizo a linguagem {linguagem}.")

PI = 3.14159
print(f"valor de PI: {PI:.2f}")
print(f"valor de PI: {PI:10.2f}")