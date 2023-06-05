nome = "PAULO JONAS ALVES DA SILVA"
nome_inverso = nome[::-1].strip()

print(nome[0])
print(nome[-1])
print(nome[:11])
print(nome[11:])
print(nome[11:20])
print(nome[8:16:2])
print(nome[:])
print(nome[::-1])

if nome_inverso == nome.strip():
    print("palíndromo")
else:
    print("não palíndromo")