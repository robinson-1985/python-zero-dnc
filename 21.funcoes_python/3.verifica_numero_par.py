# função verifica se é par, atribui em uma variável e retorna resposta "o número é" +variável.

def verifica_par(x):
    if x % 2 == 0:
        resultado = ' é par'
    else:
        resultado = ' é ímpar'
    return 'O número' +resultado
print(verifica_par(10))