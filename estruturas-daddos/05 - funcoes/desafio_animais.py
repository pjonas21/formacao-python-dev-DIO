a = input() 
b = input() 
c = input()

def vertebrado(b,c):
    if b == 'ave':
        if c == 'carnivoro':
            print("aguia")
        elif c == 'onivoro':
            print("pomba")
    elif b == 'mamifero':
        if c == 'onivoro':
            print("homem")
        elif c == 'herbivoro':
            print("vaca")

def invertebrado(b,c):
    if b == 'inseto':
        if c == 'hematofago':
            print("pulga")
        elif c == 'herbivoro':
            print("lagarta")
    elif b == 'anelideo':
        if c == 'hematofago':
            print("sanguessuga")
        elif c == 'onivoro':
            print("minhoca")

if a == 'vertebrado':
    vertebrado(b=b,c=c)
elif a == 'invertebrado':
    invertebrado(b=b,c=c)