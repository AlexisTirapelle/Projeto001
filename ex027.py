nomeCompleto = input('Nome completo: ')

nomeSplit = nomeCompleto.split()
print('1º nome: {}'.format(nomeSplit[0]))
print('Último nome: {}'.format(nomeSplit[len(nomeSplit)-1]))
