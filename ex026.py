print ('Sorteio de alunos (detalhado)')
import random
al1 = (input('Primeiro Aluno: '))
al2 = (input('Segundo Aluno: '))
al3 = (input('Terceiro Aluno: '))
al4 = (input('Quarto Aluno: '))
listas = [al1,al2,al3,al4]
for lista in listas:
    print(lista)
print('O aluno sorteado foi: ')
print(random.choice(listas))
