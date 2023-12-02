import random
print('Programa que escolha um número de 0 a 5')
num = (str(input('Digite um número de 0 a 5: '))).strip().upper()
lista = ['0', '1', '2', '3', '4', '5']
resultado = (random.choice(lista))
print('-'*20)
print('Escolhendo número....')
print('-'*20)
print('O número escolhido foi: {}'.format(resultado))
if resultado != num:
    print('Você errou o número sorteado!!!')
else:
    print('Você acertou o número sorteado!')
