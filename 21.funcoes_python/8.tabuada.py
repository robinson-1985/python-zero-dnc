''' criando função tabuada que recebe um número e percorre o for com print da 
multiplicação desse número até o range definido. '''

def tabuada (x):
    for a in range(10):
        print(x, 'x', a, '=', a*x)
print(tabuada(3))