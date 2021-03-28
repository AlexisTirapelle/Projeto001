nome = input('Nome completo: ').strip()

print('\nMaiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))

nomeSemEspaco = nome.replace(' ', '')
print('Quantidade de letras: {}'.format(len(nomeSemEspaco)))
nomeSplit = nome.split()
print('Qtd letras 1º nome: {}'.format(len(nomeSplit[0])))
