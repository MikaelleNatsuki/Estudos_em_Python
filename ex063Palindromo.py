print('\033[92m-\033[m'*20)
print('\033[92m-\033[m'*4, '\033[95mPalíndromo\033[m', '\033[92m-\033[m'*4)
print('\033[92m-\033[m'*20)
frase = str(input('Digite a frase e descobriremos se é um \033[92mPalíndromo\033[m: ')).upper().replace(' ', '')
invertido = frase.upper()[::-1].replace(' ', '')
if invertido == frase:
    print('A frase é um palíndromo,pois lida de trás para frente é ''\033[95m{}\033[m'' e lida na ordem é ''\033[92m{}\033[m'' '.format(invertido, frase))
else:
    print('A frase ''\033[92m{}\033[m'' não é um palíndromo, pois ela e diferente lida de trás para frente, ''\033[95m{}\033[m''.'.format(frase, invertido))
