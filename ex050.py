soma = 0
for c in range(1, 7):
    valor = int(input('Informe o {}º valor: '.format(c)))
    if valor % 2 == 0:
        soma += valor
print('A soma dos valores pares é: {}'.format(soma))
