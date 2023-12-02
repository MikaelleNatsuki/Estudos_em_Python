print('Limite de velocidade')
vel = (float(input('Qual a velocidade do veiculo em km ? ')))
if vel <= 80:
    print('Está dentro do limite de velocidade de 80km por hora.')
elif vel > 80:
    ac = (vel - 80) * 7.00
    print('Você esta acima do limite de velocidade, o valor da multa é de : R$ {:.2f}'.format(ac))
