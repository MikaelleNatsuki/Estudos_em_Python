print('Condições da existencia de um Triângulo')
print('-'*40)
l1 = int(input('Digite o primeiro lado do triângulo: '))
l2 = int(input('Digite o segundo lado do triângulo: '))
l3 = int(input('Digite o terceiro lado do triângulo: '))
print('-'*40)
if (l1+l2) > l3 and (l1+l3) > l2 and (l3+l2) > l1:
    print('''É possivel formar um triângulo, pois os lados são menores que a soma dos outros dois lados:
    -Lado 1: {}
    -Lado 2: {}
    -Lado 3: {}
    '''.format(l1, l2, l3))
else:
    print('''Impossivel formar um triângulo, pois um dos lados e maior que a soma de dois lados:
    -Lado 1: {} 
    -Lado 2: {}
    -Lado 3: {}
    '''.format(l1, l2, l3))
