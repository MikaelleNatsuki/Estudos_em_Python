print('-Calculadora de IMC (Indíce de Massa Corporal)-')
print('')
print('-'*42)
print('''   Abaixo de 17 Muito abaixo do peso
   Entre 17 e 18,49 Abaixo do peso
   Entre 18,5 e 24,99 Peso normal
   Entre 25 e 29,99 Acima do peso
   Entre 30 e 34,99 Obesidade I
   Entre 35 e 39,99 Obesidade II(severa)
   Acima de 40 Obesidade III(mórbida)
''')
print('-'*42)
nome = str(input('Olá usuario(a)!!!, por favor, digite o seu nome: '))
altura = float(input('Digite a sua altura em metros e centimetros (ultilizando "." para separar METROS dos CENTIMETROS.): '))
peso = float(input('Digite o seu peso em kg (ultilizando "." para separar KG das GR: '))
imc = peso / (altura * altura)
print('-'*42)
if imc <= 17:
    print('{} o seu Imc é: {:.2f}, está \033[31mmuito abaixo do peso.\033'.format(nome, imc))
elif imc <= 18.49:
    print('{} o seu Imc é: {:.2f}, \033[31mestá abaixo do peso.\033'.format(nome, imc))
elif imc <= 24.99:
    print('{} o seu Imc é: {:.2f}, \033[32mestá no seu peso normal.\033 '.format(nome, imc))
elif imc <= 29.99:
    print('{} o seu Imc é: {:.2f}, \033[31mestá acima do peso.\033 '.format(nome, imc))
elif imc <= 34.99:
    print('{} o seu Imc é: {:.2f}, \033[32mestá com obesidade grau I\033'.format(nome, imc))
elif imc <= 39.99:
    print('{} o seu Imc é: {:.2f}, \033[32mestá com obesidade grau II (severa)\033 '.format(nome, imc))
elif imc >= 40:
    print('{} o seu Imc é: {:.2f}, \033[32mestá com obesidade grau III (mórbida)\033 '.format(nome, imc))
