#entrada
inverteCor = '\033[40m'
fechaCor = '\033[m'
num = int(input('Digite um número qualquer: '))
print('[1] Converter para {}BINÁRIO{}.'.format(inverteCor, fechaCor))
print('[2] Converter para {}OCTAL{}.'.format(inverteCor, fechaCor))
print('[3] Converter para {}HEXADECIMAL{}.'.format(inverteCor, fechaCor))
opcao = int(input('Escolha uma opção acima: '))

#processamento
if opcao == 1:
    saida = '{} convertido para BINÁRIO é: {:08b}'.format(num, num)
elif opcao == 2:
    saida = '{} convertido para OCTAL é: {}'.format(num, oct(num)[2:])
elif opcao == 3:
    saida = '{} convertido para HEXADECIMAL é: '.format(num) + hex(num)[2:]
else:
    saida = "Digite uma opção válida..."

#saida
print(inverteCor + saida + fechaCor)
