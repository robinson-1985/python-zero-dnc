#criando uma tupla e percorrendo ela e a lista com zip printando os 2 valores
lista = [1, 2, 3, 4, 5, 6]
tupla = ('oi',5,'tchau',20)
for a,b in zip(lista, tupla): #só vai percorrer o tamanho da tupla.
  print(a,b)