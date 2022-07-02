peso = float(input('Qual seu peso? (Kg): '))
altura = float(input('Qual sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO.')
elif 18.5 <= imc < 24.9:
    print('Você esta no PESO IDEAL')
elif 25 <= imc < 29.9:
    print('Você esta ACIMA DO PESO')
elif 30 <= imc < 34.9:
    print('CUIDADO!! Você esta com OBESIDADE I')
elif 35 <= imc < 39.9:
    print('CUIDADO!! Você esta com OBESIDADE II')
else:
    print('CUIDADO!! Você esta com OBESIDADE III ')
