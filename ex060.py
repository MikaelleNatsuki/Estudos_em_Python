print('\033[32mSoma de números pares\033')
soma = 0
cont = 0
# Programa feito para efetuar a soma de números pares digitados pelo usuario.
for s in range(1, 7):
    nu = int(input('\033[92mDigite o {}° valor a ser somado :\033'.format(s)))
    if nu % 2 == 0:
        soma = soma + nu
print('\033[92mO valor da soma dos números pares é igual a: {}\033'.format(soma))
