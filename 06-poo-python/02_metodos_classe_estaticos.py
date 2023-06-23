class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # convertido em metodo de classe
    # quando preciso acessar o contexto da classe
    @classmethod
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2023 - ano
        return cls(nome, idade)
    
    # quando nao eh preciso acessar o contexto da classe
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


pessoa_1 = Pessoa('Jonas', 33)
print(pessoa_1.nome, pessoa_1.idade)

pessoa_2 = Pessoa.criar_apartir_data_nasc(1989,12,14,'Paulo Jonas')
print(pessoa_2.nome, pessoa_2.idade)

print(Pessoa.e_maior_de_idade(18))
print(Pessoa.e_maior_de_idade(8))