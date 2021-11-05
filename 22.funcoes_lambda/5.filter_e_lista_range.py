#criando função lambda dentro do filter e passando como lista range(10)
#convertendo os valores para lista e atribuindo a variavel par
ver_par_filter = lambda x: True if x %2==0 else False
par = list(filter(ver_par_filter,range(10)))

#printando a variavel par
print(par)