opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] sair"))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema")