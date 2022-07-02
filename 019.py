from datetime import date
n1 = date.today().year
n2 = int(input('Ano de Nascimento: '))
anos = n1 - n2
print('O atleta tem {} anos.'.format(anos))
if anos <= 9:
    print('Classificação: MIRIM')
elif anos <= 14:
    print('Classificação: INFANTIL')
elif anos <= 19:
    print('Classificação: JÚNIOR')
elif anos <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
