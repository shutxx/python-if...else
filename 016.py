num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num > num2:
    print('{} e maior que {}'.format(num, num2))
elif num < num2:
    print('{} e maior que {}'.format(num2, num))
else:
    print('Os números são igual')
