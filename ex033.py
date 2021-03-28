a = int(input('\033[32mDigite o 1º valor: '))
b = int(input('\033[32mDigite o 2º valor: '))
c = int(input('\033[32mDigite o 3º valor: \033[m'))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print('\033[1;7mMaior: {}\033[m'.format(maior))
print('\033[1;7mMenor: {}\033[m'.format(menor))
