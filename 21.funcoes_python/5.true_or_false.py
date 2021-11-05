# criando nova função verifica_par e atribuindo T ou F na variável que vai retornar

def verifica_par_bol(x):
    if x % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado
print(verifica_par_bol(10))
