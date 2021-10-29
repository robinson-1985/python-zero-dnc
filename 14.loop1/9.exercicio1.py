# Crie uma lista contendo os números pares de 0 até 1000.

lista=[]
for lista in range(0, 1000):
  if lista % 2 == 0:
      print(lista, end=' ')
print(lista)