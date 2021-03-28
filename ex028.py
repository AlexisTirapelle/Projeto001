import time
from random import randint

print('--=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--=' * 20)
numAI = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(1.0)
if numAI == num:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numAI, num))


