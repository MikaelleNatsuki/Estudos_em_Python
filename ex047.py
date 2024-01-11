print('\33[31mEmprestimo bancário para financimento de um casa\33[m')
# Lembrando que o valor da mensalidade nao pode passar de 30% do salario do usuario.
nome = str(input('\033[37mOlá, qual o seu nome? :\033[m'))
valcasa = float(input('Digite o valor da casa: '))
anos = int(input('Em quantos anos você pretende pagar?: '))
salario = float(input('Qual é o seu salário?: '))
prestacao = (anos * 12)
mensa = (valcasa / prestacao)
if mensa > (salario * 30)/100:
    print('Infelizmente não podemos efetuar o emprestimo, poís o valor da mensalidade é de {:.2f} que é acima de 30% do seu salário'.format(mensa))
elif mensa <= (salario * 30)/100:
    print('''O valor da mensalidade será de: R${:.2f}.
Que será pago em: {} anos.
\033[32mParábens, {} por comprar sua casa!!!
'''.format(mensa, anos, nome))
