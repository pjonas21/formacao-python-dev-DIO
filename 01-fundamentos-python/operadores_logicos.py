saldo = 1000
saque = 150
limite = 100

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)
print(not saldo >= saque or saque <= limite)

saldo = 1000
saque = 150
limite = 100
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)