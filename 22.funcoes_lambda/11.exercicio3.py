# 3. Utilize a função reduce e retorne a soma da lista anterior.

from functools import reduce

print(reduce(lambda a,b,c,d: a + b + c + d, range(100)))

a = 0
for t in range(100):
    a+=t
print(a)