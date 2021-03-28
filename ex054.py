from datetime import date

maiores = 0
menores = 0
anoAtual = date.today().year
for c in range(1, 8):
    anoNasc = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = anoAtual - anoNasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
