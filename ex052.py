print('\033[34m---Triângulo Equilátero, Isóceles e Escaleno.---\033')
l1 = float(input('\033[37mDigite o Primeiro segmento: \033'))
l2 = float(input('\033[37mDigite o segundo segmento: \033'))
l3 = float(input('\033[37mDigite o terceiro segmento: \033'))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('\033[31mNão e possivel formar um triângulo, pois um dos seus lados e maior que a soma dos outros dois.\033')
elif l1 == l2 == l3:
    print('O Triângulo possui todos os lados iguais,ou seja, é um \033[33mEQUILÁTERO.\033')
elif l1 == l2 or l2 == l3 or l3 == l1:
    print('O Triângulo possui dois lados iguais, ou seja, é um \033[33mISÓCELES.\033')
elif l1 != l2 != l3:
    print('O Triângulo possui todos os seus lados diferentes, ou seja, é um \033[33mESCALENO.\033')
