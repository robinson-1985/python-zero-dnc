''' 3. crie duas listas e percorra as duas no mesmo for, se elas tiverem tamanhos diferentes 
descreva o que acontece.'''

lista = [1,2,3,4,5,6,7,8,9]
lista_2 = [1,2,3,4,5,6,7,8,9,10]

for a in lista:
    for b in lista_2:
        print(a, b)
if lista > lista_2:
    print('A lista 1 contém mais elementos que a lista 2!')
else:
    print('A lista 2 contém mais elementos que a lista 1!')
