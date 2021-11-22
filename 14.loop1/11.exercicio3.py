# 3. Compare as duas listas.

lista = [1,2,3,4]
lista_b = [2,3,45,6,8]

for a in lista:
    if a in lista_b: print(a, 'Contém na lista')
    else: print(a, 'Não contém na lista')
