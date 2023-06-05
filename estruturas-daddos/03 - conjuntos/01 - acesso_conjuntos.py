'''
para acessar pelo índice é preciso converter
o conjunto em uma lista primeiro
'''
linguagens = {"python","java","python"}

# podemos percorrer os dados de forma iterável
# da mesma forma que nas listas
for lang in linguagens:
    print(lang)

for ind,lang in enumerate(linguagens):
    print(f'{ind} - {lang}')

lista_linguagens = list(linguagens)

print(lista_linguagens[0])