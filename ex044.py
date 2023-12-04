print('Aumento do Salário de um funcionario')
# Para salarios acima de 1250,00 o aumento é de 10% e para valores inferiores o aumento é de 15%
salario = float(input('Qual o seu salário atual? : '))
porcentagem10 = (salario * 10)/100 + salario
porcentagem15 = (salario * 15)/100 + salario
if salario > 1250:
    print('Seu salário atual é de {:.2f} e com o aumento de 10% o seu novo salário é de: {:.2f}'.format(salario, porcentagem10))
elif salario <= 1250:
    print('Seu salário atual é de {:.2f} e com o aumento de 15% o seu novo salário é de: {:.2f}'.format(salario, porcentagem15))

