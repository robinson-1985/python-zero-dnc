# criando função cadastro com input de nome e sobrenome e retornando nome e sobrenome do input

def cadastro():
    print('Nome: ')
    nome = input()
    print('Sobrenome: ')
    snome = input()
    return nome, snome

# criando variável usuário e chamando função cadastro

usuario = cadastro()

# printando variável usuário

print(usuario)