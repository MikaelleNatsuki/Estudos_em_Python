print('\033[1;31;46mAprendendo a usar cores! (padrão ANSI)\033[m')
print('\033[1;97;45mOlá Usuario(a)!\033[m')
print('''Fontes:
\033[1mNegrito\033[m
\033[4mSublinhado\033[m''')
('\033[7mInverte a cor do fundo com a cor da letra\033[m')
print('''Cores da Fonte:
\033[30mPreto\033[m
\033[31mVermelho\033[m
\033[32mVerde\033[m
\033[33mLaranja\033[m
\033[34mAzul\033[m
\033[35mRoxa\033[m
\033[36mCiano\033[m
\033[37mCinza Claro\033[m
\033[90mCinza Escuro\033[m
\033[91mVermelho Claro\033[m
\033[92mVerde Claro\033[m
\033[93Amarelo\033[m
\033[94mAzul Claro\033[m
\033[95mPink\033[m
\033[96mCiano Claro\033[m
''')
print('''Cores do Fundo:
\033[40mPreto\033[m
\033[41mVermelho\033[m
\033[42mVerde\033[m
\033[43mAmarelo\033[m
\033[44mAzul\033[m
\033[45mMangenta\033[m
\033[46mCiano\033[m
''')
# inserindo cores em variavéis \033[m \033[m
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
resultado = n1 + n2
print('A soma entre \033[1;34m{}\033[m e \033[1;34m {}\033[m é : \033[1;36m{}\033[m'.format(n1, n2, resultado))
