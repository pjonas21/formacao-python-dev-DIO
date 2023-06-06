def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("Fox",2015,"PMA8B01",marca="VW",motor="1.6",combustivel="FLEX")
# criar_carro(modelo="Fox",ano=2015,placa="PMA8B01",marca="VW",motor=1.6,combustivel="FLEX")

def criar_carro_nomeado(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro_nomeado(modelo="Gol",ano=2020,placa="QWE&Y&&",marca="VW",motor="1.0",combustivel="FLEX")