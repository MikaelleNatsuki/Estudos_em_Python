print('Quantos litros de tinta por m²')
altura = float(input('Digite a altura: '))
base = float(input('Digite a largura(base): '))
mq = base * altura
tinta = mq / 2
print('A dimensão da parede é de : {} x {} \nA área é : {} m²\nE a quantidade de tinta ultilizada para pintar a área é de :{:.3f}L'.format(altura,base,mq, tinta))
