import time
from time import sleep
print('Contagem Regressiva!(Laço for, in)')
for c in range(10, -1, -1):
    print('''\033[32m...
{}\033'''.format(c))
    time.sleep(1)
print('\033[31mFim!!!\033')
