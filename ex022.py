print ('Calculando o valor da hipotenusa')
import math
catop = int(input('Digite o valor do cateto oposto :'))
caad = int(input('Digite o valor do cateto adjacente :'))
hi = math.hypot(catop,caad)
print ('O valor da hipotenusa é igual a : {:.2f} '. format(hi))
