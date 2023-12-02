print('teste de if,else')
nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Natsuki':
    print('Então e a futura programadora!')
else:
    print('Sai do meu pc intruso.')
print('Olá {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(me))
if me >= 6.0:
    print('Parabéns Zé, não pegou dp!')
else:
    print('Vai ter que estudar nas feriás, se lascou')



