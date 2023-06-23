'''
quando sao definidos *args e **kwargs o metodo recebe valores
como tuplas e dicionarios respectivamente
'''
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Terça-feira, 06 de Junho de 2023.","Zen of Python", "Beautiful is better than ugly.", autor="Tim Petters", ano=1999)