#criando duas listas
lista_1=[1,2,3,4,5]
lista_2=[5,4,3,2,1]

#convertendo o zip das 2 listas em dict e atribuindo a um segundo dicionário
dicionario_2 = dict(zip(lista_1,lista_2))
print(dicionario_2)