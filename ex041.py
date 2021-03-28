import datetime

anoNasc = int(input('Ano de nascimento: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('O atleta tem {} anos. \nClassificação: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos. \nClassificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos. \nClassificação: JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos. \nClassificação: SÊNIOR'.format(idade))
elif idade > 120:
    print('O atleta tem {} anos? \nPor favor valide se o ano de nascimento foi informado corretamente...'.format(idade))
else:
    print('O atleta tem {} anos. \nClassificação: MASTER'.format(idade))
