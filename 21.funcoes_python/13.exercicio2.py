''' 2. Agora nessa mesma função coloque o retorno como um dicionário onde a chave é
 o cpf e o valor o nome do usuário. '''

def cadastro():
    print('Digite o n° do seu CPF:')
    cpf = input()
    print('Digite o seu nome: ')
    nome = input()
    return cpf, nome

usuario = cadastro()
print(usuario)

dicionario = {'cpf': 333366142110, 'nome': 'Robinson'}
print(dicionario)