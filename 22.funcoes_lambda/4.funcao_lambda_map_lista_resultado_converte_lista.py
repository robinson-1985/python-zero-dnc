#criando função lambda verifica par dentro do map e passando uma lista e convertendo resultado para lista

#printando o resultado de par

lista=[1,2,3,4,5,3,6,4,3]
pares = list(map(lambda x: 'par' if x %2==0 else 'impar' ,lista))
print(pares)

#list(filter(ver_par_filter,lista))