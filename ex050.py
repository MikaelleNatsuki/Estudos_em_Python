print('-'*30)
print('        Média do aluno')
print('-'*30)
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('\033[36mSua média é {} e está abaixo de\033 5.0,\033[36mentão está\033 \033[31mREPROVADO\033'.format(media))
elif media >= 7.0:
    print('\033[36mSua média é {}, ou seja, você foi \033[32mAPROVADO\033'.format(media))
else:
    print('\033[36mSua média é {}, e esta abaixo de 7.0, ou seja, está de \033[92mRECUPERAÇÃO\033'.format(media))
