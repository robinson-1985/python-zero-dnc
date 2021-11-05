# utilizando o filter para aplicar a nova função verifica_par em uma lista e atribuir a x

def verifica_par_filtro(x):
    if x % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado
x = filter(verifica_par_filtro, [1,2,3,4,5,6,7,8,9])
#printando list de x porque o filter retorna um construtor
print(list(x))