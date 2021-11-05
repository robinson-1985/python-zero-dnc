# 2. Utilize uma função filter para retornar somente os números pares da lista abaixo.
lista = [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12]
pares = list(filter(lambda x: True if x %2==0 else False,lista))
print(pares)