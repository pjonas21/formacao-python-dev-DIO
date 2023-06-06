C = int(input())

def verificar_humano(num):
  if num > 8000:
    print("Mais de 8000!")
  else:
    print("Inseto!")


for i in range(C):
  num = int(input())
  verificar_humano(num)