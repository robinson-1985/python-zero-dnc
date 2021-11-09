''' List Comprehension é um dos grandes marcos de Python, podemos criar loop dentro de 
uma lista para gerar ela.'''

lista_6 =[a for a in range(10)]
print(lista_6)

lista_7 = [a for a in range(10) if a%2==0]
print(lista_7)