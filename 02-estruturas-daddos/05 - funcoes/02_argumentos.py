def salvar_carro(marca,modelo,ano,placa):
    print(f"Carro inserido com sucesso! {marca}|{modelo}|{ano}|{placa}")

salvar_carro("Fiat","Palio",2008,"LVW-5063")
salvar_carro(marca="Fiat",modelo="Palio",ano=2008,placa="LVW-5063")

# os asteriscos indicam a passagem de um dicionario como parametro da funcao
salvar_carro(**{'marca':'Fiat','modelo':'Argo','ano':2019,'placa':'SSS2D33'})