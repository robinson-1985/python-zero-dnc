''' 2. Agora nessa mesma função coloque o retorno como um dicionário onde a chave é
 o cpf e o valor o nome do usuário. '''

def cadastro():
    print('Digite o seu nome: ')
    nome = input()
    print('Digite o n° do seu CPF:')
    cpf = input()
    dicio = dict({cpf:nome})
    print(dicio)
    return dicio

usuario = cadastro()
print(usuario)
