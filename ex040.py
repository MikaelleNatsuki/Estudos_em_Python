print('Número par ou impar?')
numero = int(input('Digite o número desejado: '))
print('O Número escolhido foi: {}'.format(numero))
par = (numero % 2)
if par == 0:
    print('{} é um Número Par!'.format(numero))
else:
    print('{} é um Número impar!'.format(numero))
