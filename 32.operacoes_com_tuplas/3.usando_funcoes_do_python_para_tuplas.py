''' Por mais que temos um leque de opções limitados para métodos próprios para tuplas, 
podemos utilizar métodos gerais do python que são compatíveis com operações com tupla, 
ou então construir nossos próprios métodos. '''

tupla_1 = (1,2,4,7,5,6,(4,3),1,2,1)
tupla_2 = ("oi","tchau","boa tarde")
tupla_3 = tupla_1 + tupla_2
print(tupla_3)
del tupla_3
print(tupla_3)

tupla_3 = (10,203,40,7)*2
print(tupla_3)
print(id(tupla_3))
lista = list(tupla_3)
lista.sort()
tupla_3= tuple(lista)
print(id(tupla_3))
tupla_3

(valor_1,valor_2,valor_3)=tupla_2
print(valor_1)
print(valor_2)
print(valor_3)