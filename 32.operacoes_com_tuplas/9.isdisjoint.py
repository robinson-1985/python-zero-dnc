# tb retorna valores booleanos

set_1 = {1,2,3,4,5,6,7}
set_2 = {0,3,4,5,6,7,8,9}
set_3={1,2,3,4,7,0,9}
print(set_1)
print(set_2)
print(set_3)
set_4={77,33}
print(set_4)
print(set_2.isdisjoint(set_3))
print(set_3.isdisjoint(set_1))
print(set_3.isdisjoint(set_4))