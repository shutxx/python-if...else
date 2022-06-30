nome = str(input('Qual é seu nome? '))
if nome == 'Allan':
    print('Que nome bonito {}!!'.format(nome))
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
