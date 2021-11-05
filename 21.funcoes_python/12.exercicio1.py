# 1. Crie uma função que receba o input do cpf e nome do usuário.

def cadastro():
    print('Digite o n° do seu CPF:')
    cpf = input()
    print('Digite o seu nome: ')
    nome = input()
    return cpf, nome

usuario = cadastro()
print(usuario)