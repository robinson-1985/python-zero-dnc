''' 2. Procure o atributo idade para o usuário 1 e caso não tenha adicione o valor 30 
nesse campo.'''

dic1 = {'user1':{'nome': 'Mioshi', 'sobrenome': 'Kanashiro', 'apelido': 'Japa'},
        'user2':{'nome': 'Sergei', 'sobrenome': 'Ivanov', 'apelido': 'Russo'},
        'user3':{'nome': 'Alfredo', 'sobrenome': 'Constâncio', 'apelido': 'Portuga'}}

for a, b in dic1.items():
    b.setdefault('idade', 30)
print(dic1)