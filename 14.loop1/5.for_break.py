#é possível parar o comando for assim que encontrar o item desejado utilizando o break

lista=[2,5,10,4,12]
for a in lista:
  if type(a)==int:
    print(a,' = inteiro encontrado')
    break