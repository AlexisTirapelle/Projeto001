from time import sleep
from random import randint

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual é sua jogada? '))
if 0 <= opcao <= 2:
    pc = randint(0, 2)
    print('JO...')
    sleep(0.7)
    print('KEN...')
    sleep(1)
    print('PO!!!...')
    sleep(0.5)
    print('-' * 22)
    # if pc == 0:
    #     print('Computador jogou PEDRA')
    # elif pc == 1:
    #     print('Computador jogou PAPEL')
    # else:
    #     print('Computador jogou TESOURA')
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    print('Computador jogou {}'.format(itens[pc]))
    print('Você jogou {}'.format(itens[opcao]))
    print('-' * 22)
    if opcao == 0:
        # print('Você jogou PEDRA')
        # print('-' * 20)
        if pc == 0:
            print('EMPATE!')
        elif pc == 1:
            print('DERROTA!')
        else:
            print('VITÓRIA!')
    elif opcao == 1:
        # print('Você jogou PAPEL')
        print('-' * 20)
        if pc == 0:
            print('VITÓRIA!')
        elif pc == 1:
            print('EMPATE!')
        else:
            print('DERROTA!')
    elif opcao == 2:
        # print('Você jogou TESOURA')
        # print('-' * 20)
        if pc == 0:
            print('DERROTA!')
        elif pc == 1:
            print('VITÓRIA!')
        else:
            print('EMPATE!')
else:
    print('Opção inválida...')
