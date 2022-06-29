velo = int(input('Qual velocidade do carro? '))
if velo > 80:
    print('MULTADO! Limite de velocidade excedido!!')
    multa = (velo - 80) * 7
    print('Você deve pagar uma multa de R$:{:.2f}'.format(multa))
print('Tenha um com dia dirija com segurança!')
