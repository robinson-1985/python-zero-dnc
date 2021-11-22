#  2. Transforme cada valor da lista anterior em um string.
lista = []
for a in range(0,1000,2):
  lista.append(a)
lista_2=[]
for a in lista:
  lista_2.append(str(a))
print(lista_2)
    