frase = input('Frase: ').strip()

print('Qtd letras "A": {}'.format(frase.upper().count('A')))
print('1º "A": {}'.format(frase.upper().find('A') + 1))
print('Último "A": {}'.format(frase.upper().rfind('A') + 1))
