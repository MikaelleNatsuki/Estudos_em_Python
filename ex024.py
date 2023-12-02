print('Calculadora seno, cosseno e tangente')
import math
ang = float(input('Digite o angulo desejado: '))
se = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O valor de Seno é: {:.2f}\nO valor do Cosseno é: {:.2f}\nO valor do Tangente é {:.2f}'.format(se,cos,tg))
