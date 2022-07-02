n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
nota = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, nota))
if 7 > nota >= 5:
    print('O aluno esta RECUPERAÇÃO.')
elif nota < 5:
    print('O aluno esta de REPROVADO.')
elif nota >= 7:
    print('O aluno APROVADO.')
