class Estudante:
    # variavel de classe
    # atributo da classe
    escola = 'DIO'

    def __init__(self, nome, matricula):
        # variaveis de instancia
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

aluno_1 = Estudante("J Silva", '30283619')
aluno_2 = Estudante("Marcelo", '1343171X')

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = 'Python'
aluno_3 = Estudante("Sampaio", '12726414')
mostrar_valores(aluno_1, aluno_2, aluno_3)

