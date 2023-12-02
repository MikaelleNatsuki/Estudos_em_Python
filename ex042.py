print('O ano e bissexto ou não?')
ano = (int(input('Digite o ano que você deseja saber se é ou nao é bissexto: ')))
resultado = ano % 4
if resultado == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano Bissexto!'.format(ano))
