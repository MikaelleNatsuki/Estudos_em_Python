from datetime import date
print('O ano e bissexto ou não?')
ano = (int(input('''Digite o ano que você deseja saber se é ou não é bissexto.
Se gostaria de saber se o ano atual é bissexto, digite 0 :''')))
resultado = ano % 4
if ano == 0:
    ano = date.today().year
if resultado == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto!'.format(ano))
