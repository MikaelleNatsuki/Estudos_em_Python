from random import randint
import time
print('\033[33m=\033'*10, 'JO-KEN-PÔ', '\033[33m=\033'*10)
print('''\033[32mOlá Jogador(a)!
Faça a sua escolha!
DIGITE [0] Pedra
DIGITE [1] Papel
DIGITE [2] Tesoura\033''')
user = (int(input('Sua escolha: ')))
op = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Minha vez!!!
JO''')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
print('Eu (Computador) escolhi : {}'.format(op[pc]))
print('\033[33m=\033'*31)
if user == 0 and pc == 0:
    print('\033[34mPedra e Pedra, parece que temos um empate aqui!\033')
elif user == 1 and pc == 1:
    print('\033[34mPapel e Papel, parece que temos um empate aqui!\033')
elif user == 2 and pc == 2:
    print('\033[34mTesora e Tesoura, parece que temos um empate aqui!\033')
elif user == 0 and pc == 1:
    print('\033[31mVôce escolheu Pedra, e eu Papel, puxa parece que eu te venci!\033')
elif user == 0 and pc == 2:
    print('\033[32mVôce escolheu Pedra, e eu Tesoura, puxa parece que perdi para um humano!\033')
elif user == 1 and pc == 0:
    print('\033[32mVôce escolheu Papel, e eu Pedra, puxa parece que perdi para um humano!\033')
elif user == 1 and pc == 2:
    print('\033[31mVôce escolheu Papel, e eu Tesoura, puxa parece que eu te venci!\033')
elif user == 2 and pc == 0:
    print('\033[31mVôce escolheu Tesoura, e eu Pedra, puxa parece que eu te venci!\033')
elif user == 2 and pc == 1:
    print('\033[32mVôce escolheu Tesoura, e eu Papel, puxa parece que perdi para um humano!\033')
