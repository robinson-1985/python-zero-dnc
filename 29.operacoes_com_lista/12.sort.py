# Sort() -> Ordena a lista por algum chave especificada.

lista_4 = [10,9,8,7,5,6,4,2,3,1,2,3]
print(lista_4)
lista_4.sort()
print(lista_4)
lista_4.reverse()
print(lista_4)
print(sorted(lista_4))
print(lista_4)
lista_4.sort(reverse=True)
print(lista_4)
print(5*"--")
lista_5=['Peter','Fulano','Ciclano','Pet']
print(lista_5)
lista_5.sort(key=len)
print(lista_5)
lista_5.sort(key=len,reverse=True)
print(lista_5)