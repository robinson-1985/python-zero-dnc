#printando cada campo do dicionário em formato de json

dicionario_full = {'usuario':'Peter','lingua':'pt-br','pet':['cachorro_1','cachorro_2']}

print('nome do usuario: ', dicionario_full['usuario'])
print('lingua nativa: ',dicionario_full['lingua'])

#printando len da lista (quantidade de valores)

print('qtd de pet: ', len(dicionario_full['pet']))