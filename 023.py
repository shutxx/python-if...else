from random import randint
from time import sleep
itens = ('pedra ', 'papel', 'tesoura')
cpu = randint(0, 2)
# print('O computador escolheu {}'.format(itens[cpu]))
print('-=' * 12)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
player = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!')
print('-=' * 12)
print('CPU jogou {}'.format(itens[cpu]))
print('jogador jogou {}'.format(itens[player]))
print('-=' * 12)
if cpu == 0:  # pedra
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('CPU VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 1:  # papel
    if player == 0:
        print('CPU VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 2:  # tesoura
    if player == 0:
        print('JOGADOR VENCE')
    elif player ==1:
        print('CPU VENCE')
    elif player ==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')