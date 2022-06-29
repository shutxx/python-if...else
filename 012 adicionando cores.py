cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarela': '\033[33m',
    'pretoEbranco': '\033[7;30m'}
print('\033[4;31;40mOlá, mundo!\033[m')
print('{}Olá, Mundo!{}'.format(cores['amarela'], cores['limpa']))
print('{}Olá, Mundo!{}'.format('\033[4;31;40m', '\033[m'))
