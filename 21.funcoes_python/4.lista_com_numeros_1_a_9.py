#lista com numeros de 1 a 9
lista=[1,2,3,4,5,6,7,8,9]
#utilizando o map para aplicar a função verifica_par na lista e atribuindo o resultado em x
def verifica_par(x):
    if x % 2 == 0:
        resultado = ' é par'
    else:
        resultado = ' é ímpar'
    return 'O número' +resultado
x = map(verifica_par, lista)
#printando a list de x porque o map retorna um construtor
print(list(x))
