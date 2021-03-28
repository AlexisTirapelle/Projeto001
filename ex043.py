print('\n---- IMC ----')
peso = float(input('Informe seu peso (kg): '))
alt = float(input('Informe sua altura (m): '))
imc = peso / (alt * alt)
print('\nSeu IMC é {:.2f}'.format(imc))
print('Situação: ', end='')
if imc < 18.5:
    print('Abaixo do peso...')
elif 18.5 <= imc < 25:
    print('Peso normal!')
elif 25 <= imc < 30:
    print('Sobrepeso...')
elif 30 <= imc < 40:
    print('Obesidade...')
else:
    print('Obesidade Mórbida, CUIDADO!')
