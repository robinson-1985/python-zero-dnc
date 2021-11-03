#criando um terceiro dicionario

dicionario_3={}
#criando uma lista de cores e outra de adjetivos
cor = ['azul','verde','cinza']
adj = ['legal','top','top']

#percorrendo a lista e atribuindo ao dicionário chave e valor pelo zip das listas cores e adjetivos

for a,b in zip(cor, adj):
  dicionario_3[a]=b
print(dicionario_3)