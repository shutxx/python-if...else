distancia = float(input('Qual é a distância da sua viagem? '))
print('Você estápreste a começar sua viagem de {}KM.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R$:{:.2f}'.format(preço))
