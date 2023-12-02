print ('Aluguel de um carro')
km = float(input('Quantos Kilometros o carro andou?:'))
dias = float(input('Quantos dias o carro foi alugado?: '))
vkm = km * 0.15
vdia = dias * 60
totapg = vkm + vdia
print ('O Total de dias alugados foi de: {:.0f} dias resultando no valor de R$ {:.2f}\nO total de kilometros rodados foi de {:.0f}km Resultando no valor de R${:.2f}\nO valor total do aluguel do veiculo é de : R${:.2f}'.format(dias, vdia, km, vkm,totapg))