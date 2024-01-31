print('\033[33m-\033[m'*30)
print('\033[33m======Maior e menor peso======\033[m')
print('\033[33m-\033[m'*30)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Olá {}° usuário digite o seu peso em kg: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi \033[31m{:.2f}Kg\033[m\nO menor peso foi \033[32m{:.2f}Kg\033[m'.format(maior, menor))
