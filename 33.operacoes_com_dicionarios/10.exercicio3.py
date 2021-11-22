# 3. Conte a quantidade de nomes e sobrenomes contidos no dicionário.

dic1 = {'user1':{'nome': 'Mioshi', 'sobrenome': 'Kanashiro', 'apelido': 'Japa'},
        'user2':{'nome': 'Sergei', 'sobrenome': 'Ivanov', 'apelido': 'Russo'},
        'user3':{'nome': 'Alfredo', 'sobrenome': 'Constâncio', 'apelido': 'Portuga'}}

n = 0
s = 0
for a, b in dic1.items():
    nome = b.get('nome', 0)
    snome = b.get('sobrenome', 0)
    if nome != 0:
        n+=1
    if snome != 0:
        s+=1
print('Total nomes: ',n,'\nTotal sobrenomes: ',s,'\nTotal de nomes e sobrenomes: ', s+n)