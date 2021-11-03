#printando dicionario e verificando se o type é diferente de string (lista) para printar o len desse paramêtro 
#caso não printando qtd = 1

lista_dicionario_full =[{'usuario':'Peter','lingua':'pt-br','pet':['cachorro_1','cachorro_2']},
                        {'usuario':'Peter2','lingua':'pt-br','pet':['cachorro_1','cachorro_2']},
                        {'usuario':'Peter3','lingua':'es-ar','pet':'cachorro_2'}]

for a in lista_dicionario_full:
  print('nome do usuario: ', a['usuario'])
  print('lingua nativa: ',a['lingua'])
  if type(a['pet'])!= str:
    print('qtd de pet: ',  len(a['pet']))
  else:
    print('qtd de pet: ',1)