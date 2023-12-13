print ('Operadores aritiméticos')
n1 = int(input('Primeiro valor '))
n2 = int(input('Segundo valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print (' A soma é {}, \n o produto é {} \n e a divisão é {:.3f}\n'.format(s,m,d), end =' ')

print('Divisão inteira {} \n e potência {:.3f}'.format(di, e))
