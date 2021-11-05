#printando list d ex porque o filter retorna um construtor

lista = [3,2,1,6,9,5,10]
def verifica_par_bol(x):
    if x % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado
print(lista)
pares = list(filter(verifica_par_bol, lista))
print(pares)