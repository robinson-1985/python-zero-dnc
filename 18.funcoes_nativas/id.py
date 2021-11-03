# retorna o endereço da lista

lista = [1,2,3,4,5,6,7,8,9]
print(id(lista))

#endereço da lista após add mais um elemento

lista = [1,2,3,4,5,6,7,8,9]
lista.append(10)
print(id(lista))

#copiando a lista com copy

lista = [1,2,3,4,5,6,7,8,9]
lista2 = lista
print(id(lista2))

#verificando o endereço da lista original

lista = [1,2,3,4,5,6,7,8,9]
lista2 = lista.copy()
print(id(lista))

#verificando o endereço da copia da lista

lista = [1,2,3,4,5,6,7,8,9]
lista2 = lista.copy()
print(id(lista2))

