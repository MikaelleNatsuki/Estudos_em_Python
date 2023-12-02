print("Preço da passagem de uma viagem")
distancia = float(input('Quantos Kms vamos percorrer na viagem?: '))
mais = distancia * 0.45
menos = distancia * 0.50
if distancia <= 200:
    print('O valor a ser pago será de: {:.2f} ,poís esta dentro dos 200km '.format(menos))
else:
    print('O valor a ser pago será de: {:.2f} ,viagens acima de 200km ganham 10% de desconto! '.format(mais))
