#percorrendo a lista e printando o type de cada váriavel se estiverem nas condicionais

lista=[5,12,35.5, 'oi']

for a in lista:
    if type(a)==int:
        print(a, '= inteiro')
    else:
        print('Não é do tipo inteiro')
  