#percorrendo valores do dicionário e verificando se o type de algum deles é list, se for, 
#criando um novo for e percorrendo até range(len(a)) os valores

dicionario_full = {'usuario':'Peter','lingua':'pt-br','pet':['cachorro_1','cachorro_2']}
for a in dicionario_full.values():
  if type(a)==str:
    print(a)
  if type(a)==list:
    for b in range(len(a)):
      print(a[b])