n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('PARABÉNS')
    print('Sua media foi {:.1f} Aluno aprovado!'.format(m))
else:
    print('ESTUDE MAIS')
    print('Sua media foi {:.1f} Aluno reprovado!'.format(m))
