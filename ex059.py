print('Tabuada ultilizando laço for')
n = int(input('Digite o número que você deseja saber a tabuada: '))
for t in range(1, 11):
    re = (t * n)
    print('\033[35m{} x {} = {}\033 '.format(n, t, re))
print('Fim!')
