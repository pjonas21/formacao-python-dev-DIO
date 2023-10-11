import hashlib

texto = input('Digite um texto: ')

menu = int(input('''
### Escolha o tipo de hash ###
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o numero do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print(f'O hash MD5 da string eh: {resultado.hexdigest()}')
elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print(f'O hash SHA1 da string eh: {resultado.hexdigest()}')
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print(f'O hash SHA256 da string eh: {resultado.hexdigest()}')
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print(f'O hash SHA512 da string eh: {resultado.hexdigest()}')
else:
    print('Opcao invalida! Tente novamente.')
