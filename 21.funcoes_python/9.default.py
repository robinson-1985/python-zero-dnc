# criando variável que recebe x e y e atribuindo x e y default

def valores_padrao(x=10, y=3):
    return x + y

# print da função padrão acima sem passar parâmetros

print(valores_padrao())

# print da função padrão acima passando o valor de x

print(valores_padrao(19))

# print da função padrão acima passando o valor de x e y

print(valores_padrao(x=11, y=20))

# print da função padrão acima passando 2 valores

print(valores_padrao(12,20))

# print da função padrão acima passando o valor de y 

print(valores_padrao(y=23))