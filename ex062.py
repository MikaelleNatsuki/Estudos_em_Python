print('\033[32m-=-\033[m'*10)
print('       -Números Primos-       ')
print('\033[32m-=-\033[m'*10)
nu = int(input('Digite um Número: '))
tot = 0
for c in range(1, nu + 1):
    if nu % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisivel {} vezes'.format(nu, tot))
if tot == 2:
    print('Por isso ele é um número primo!')
else:
    print('Por isso ele não é um número primo!')
