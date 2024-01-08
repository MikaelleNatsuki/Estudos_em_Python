print('Soma dos Multiplos de 3 (Impares)')
s = 0
con = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        s += c
        con = con + 1
        print('\033[33m',c ,'\033')
print('\033[31mA soma de todos os {} números é igual a : {}\033'.format(con, s))
