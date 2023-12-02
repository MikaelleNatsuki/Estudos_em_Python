print('Qual o maior e o menor número?')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if (n1 > n2) and (n1 > n3) and (n2 < n3):
    print('O maior número é {} e o menor número é {}'.format(n1, n2))
elif (n1 > n2) and (n1 > n3) and (n3 < n2):
    print('O maior número é {} e o menor número é {}'.format(n1, n3))
elif (n2 > n1) and (n2 > n3) and (n1 < n3):
    print('O maior número é {} e o menor número é {}'.format(n2, n1))
elif (n2 > n1) and (n2 > n3) and (n3 < n1):
    print('O maior número é {} e o menor número é {}'.format(n2, n3))
elif (n3 > n1) and (n3 > n2) and (n1 < n2):
    print('O maior número é {} e o menor número é {}'.format(n3, n1))
elif (n3 > n1) and (n3 > n2) and (n2 < n1):
    print('O maior número é {} e o menor número é {}'.format(n2, n2))
elif n1 == n2 != n3:
    print('O primeiro e o segundo valor são iguais!')
elif n1 == n3 != n2:
    print('O primeiro e o terceiro valor são iguais!')
elif n2 == n3 != n1:
    print('O segundo e o terceiro valor são iguais!')
