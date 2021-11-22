# 3. Utilize a função reduce e retorne a soma da lista anterior.

from functools import reduce

r = reduce(lambda x,y: x+y, [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12])
print(r)