n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos a cima nao podem forma um TRIÂNGULO! ')
