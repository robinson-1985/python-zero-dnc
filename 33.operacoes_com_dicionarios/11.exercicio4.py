# 4. Verifique se há dois nomes repetidos.

dic1 = {'user1':{'nome': 'Mioshi', 'sobrenome': 'Kanashiro', 'apelido': 'Japa'},
        'user2':{'nome': 'Sergei', 'sobrenome': 'Ivanov', 'apelido': 'Russo'},
        'user3':{'nome': 'Alfredo', 'sobrenome': 'Constâncio', 'apelido': 'Portuga'}}

nomes = []
for a, b in dic1.items():
    nome = b.get('nome', 0)
    nomes.append(nome)

for a, b in dic1.items():
    nome = b.get('nome', 0)
    print(nomes.count(nome),nome)
