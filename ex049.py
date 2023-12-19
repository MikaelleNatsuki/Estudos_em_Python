from datetime import date
print('\033[34m-\033'*32)
print('\033[34mAlistamento ao serviço militar\033')
print('-'*32)
se = str(input('Você é do sexo (Masculino/Feminino?:) ')).capitalize()
anonasc = int(input('Qual o seu ano de nascimento?: '))
anoatual = date.today().year
idade = (anoatual - anonasc)
fal = 18 - idade
sob = idade - 18
if se == 'Feminino'.capitalize():
    print('Infelizmente pessoas do sexo feminino não podem se alistar.')
elif idade <= 17:
    print('''\033[90mSua idade atual é de : {} anos.
Faltam {} anos para o seu alistamento.\033'''.format(idade, fal))
elif idade == 17:
    print('''\033[34mSua idade atual é de : {} anos.
Está na hora de se alistar!\033'''.format(idade))
else:
    print('''\033[31mSua idade atual é de : {} anos.'
Já passou {} anos do ano em que voce deveria se alistar\033'''.format(idade, sob))
