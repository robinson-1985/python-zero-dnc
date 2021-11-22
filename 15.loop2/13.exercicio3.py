''' 3. crie duas listas e percorra as duas no mesmo for, se elas tiverem tamanhos diferentes 
descreva o que acontece.'''

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [1,2,3,4,5,6,7,8,9,10]

for a, b in zip (lista1, lista2):
        print(a, b) # é percorrido até o último elemento da lista menor. 

