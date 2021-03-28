print('=' * 10, 'TABUADA', '=' * 10)
num = int(input('Informe um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
