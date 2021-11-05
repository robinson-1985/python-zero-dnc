#utilizando o map para executar a função verifica par em uma lista e atribuindo a variavel par
#convertendo o map para lista
#criando funcao de verificar par com lambda
ver_par_filter = lambda x: True if x %2==0 else False
#chamando função verifica par
print(ver_par_filter(11))
#printando variavel par
lista=[1,2,3,4,5,3,6,4,3]
pares = list(filter(lambda x: True if x %2==0 else False,lista))
print(pares)