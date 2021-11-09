chaves=["id_1","id_2","id_3"]
valores=[12,123,1234]
dicionario_3 = dict.fromkeys(chaves,valores)
print(dicionario_3.get("id_1"))
print(dicionario_3.get("id_4","Não tem"))