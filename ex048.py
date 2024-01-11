print('\033[35mComparando números com estrutura if, elif, else\033[m')
print('-'*50)
pv = int(input('Digite o primeiro número: '))
sv = int(input('Digite o segundo número: '))
if pv > sv:
    print('\033[30mO primeiro valor\033[m \033[32m{}\033[m \033[30me maior que o segundo valor\033[m \033[32m{}\033[m'.format(pv, sv))
elif pv == sv:
    print('\033[30mOs valores\033[m \033[32m{}\033[m \033[30me\033[m \033[32m{}\033[m \033[30msão iguais, então não possui valor maior.\033[m'.format(pv, sv))
else:
    print('\033[30mO segundo valor\033[m \033[32m{}\033[m \033[30me maior que o primeiro valor\033[m \033[32m{}\033[m'.format(sv, pv))
