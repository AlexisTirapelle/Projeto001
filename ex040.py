nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Média {}: REPROVADO'.format(media))
# elif media >= 5 and media <= 6.9:
elif 5 <= media <= 6.9:
    print('Média {}: RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('Média {}: APROVADO'.format(media))
else:
    print('Erro inesperado...')
