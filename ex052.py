num = int(input('Digite um número: '))
primo = False
for c in range(2, num):
    if num % c == 0:
        primo = True
        break
if primo or num in (0, 1):
    print('{} não é primo!'.format(num))
else:
    print('{} é primo!'.format(num))
