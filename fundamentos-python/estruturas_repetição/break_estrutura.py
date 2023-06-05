""" while True:
    opcao = int(input("Informe um número: "))

    if opcao % 2 != 0:
        print("número ímpar")
        break

    print(opcao) """

for num in range(100):
    if num % 2 == 0:
        continue
    print(num, end=" ")