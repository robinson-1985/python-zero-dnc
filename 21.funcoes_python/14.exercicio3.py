# 3. Crie uma função para retornar a quantidade de CPF cadastrados

def cadastro ():
    cpfs = []
    continuar = ''
    while continuar != 'não' or 'Não' or 'n' or 'N':
        print('Digite o seu nome: ')
        nome = input()
        print('Digite o seu cpf: ')
        cpf = input()
        cpfs.append(cpf)
        print('Quer continuar?')
        continuar = input()
    return len(cpfs)
qtd = cadastro()
print(qtd)