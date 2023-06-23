def exibir_mensagem():
    print("Ola, mundo")

def exibir_mensagem_2(nome):
    print(f"Ola, eu sou {nome}")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Ola, {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Jonas")
exibir_mensagem_2("Jonas")
exibir_mensagem_3()
exibir_mensagem_3(nome="Paulo")