salario = float(input('Qual salario do funcionário? '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$:{:.2f} passa a ganha R$:{:.2f} agora'.format(salario, novo))
