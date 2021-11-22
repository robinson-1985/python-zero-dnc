''' 3. Crie uma função que busque um determinado valor em uma tupla e retorne a 
quantidade de vezes que esse valor aparece. '''

tupla = (2,31,3,1,4,8,3,9,6,1,20,9)
def conta (x,y):
    return x.count(y)
print(conta(tupla,3))