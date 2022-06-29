from random import randint
from time import sleep

cpu = randint(0, 5)  # imprime um número aleatória entre 0 e 5
print('-=-' * 20)
print('Pensando em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)  # espera 3 segundos para continuar o código
if jogador == cpu:
    print('PARABENS!! Você me venceu')
else:
    print('GANHEI! Eu pensei no número {} não no {}'.format(cpu, jogador))
