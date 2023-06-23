tipo_conta = int(input("Informe o tipo da conta: \n[1] conta normal \n[2] conta universitária\n"))
saldo = 500
cheque_especial = 200

if tipo_conta == 1:
    saque = float(input("Informe o valor do saque: "))
    if saque <= saldo:
        print("Sauqe realizado")
    elif saque <= saldo + cheque_especial:
        print("Sauqe com cheque especial")
    else:
        print("Não foi possível realizar a operação")
elif tipo_conta == 2:
    saque = float(input("Informe o valor do saque: "))
    if saque <= saldo:
        print("Sauqe realizado")
    else:
        print("Saldo insuficiente")
else:
    print("opção inválida")