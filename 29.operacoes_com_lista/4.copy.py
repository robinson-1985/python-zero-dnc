# Copy() -> Faz uma cópia da lista.

lista_1 =[1,2,4,3,5,8,7,9]
lista_2 = lista_1.copy()
print(lista_1)
print(lista_2)
lista_2.append(9)
print(lista_1)
print(lista_2)
lista_3 = lista_2
print(lista_2)
print(lista_3)
lista_3.append(333)
print(lista_1)
print(lista_2)
print(lista_3)
print(id(lista_1))
print(id(lista_2))
print(id(lista_3))