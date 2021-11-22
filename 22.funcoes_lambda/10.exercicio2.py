# 2. Utilize uma função filter para retornar somente os números pares da lista abaixo.

par = list(filter(lambda x: x %2==0, [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12]))
print(par)