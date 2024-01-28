from datetime import date
print('-'*38)
print('\033[35m-Grupo de maiores e menores de idade-\033[m')
print('-'*38)
mai = 0
me = 0
anoatual = date.today().year
for c in range(1, 8):
    pessoa = (int(input('Digite o ano de nascimento da {}° pessoa: '.format(c))))
    idade = anoatual - pessoa
    if idade >= 18:
        mai += 1
    elif idade < 18:
        me += 1
print('No grupo possuímos \033[33m{}\033[m maiores de idade.\nE \033[34m{}\033[m menores de idade'.format(mai, me))
