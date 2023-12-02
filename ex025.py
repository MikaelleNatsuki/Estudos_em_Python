print('Programa de sorteio de alunos')
import random
alunos = ["Aluno1", "Aluno2", "Aluno3", "Aluno4"]
for aluno in alunos:
    print(aluno)
print ('O aluno sorteado foi :')
print (random.choice(alunos))


