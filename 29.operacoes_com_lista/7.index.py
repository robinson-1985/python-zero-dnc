# Index() -> Retorna o endereço do elemento da lista.

lista_1 =[1,2,4,3,5,8,7,9]
print(lista_1)
lista_1.extend([10,30,20,30])
print(lista_1)
lista_1.extend(lista_1)
print(lista_1)
lista_4 = [10,9,8,7,5,6,4,2,3,1,2,3]
lista_4.extend((3,3,3))
print(lista_4)
print(lista_1.index(9))
print(lista_1.index(9,10))
print(lista_1.index(9,2,40))
print(lista_1.index(9,10,20))