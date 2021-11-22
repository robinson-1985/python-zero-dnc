''' 2. Adicione os valores 10,7,33,22 com uma única linha de código e deixe-os ordenados 
também em uma segunda linha de código.'''

list = [10,6,18,15,2,9,33]
list.extend([10,7,33,22])
list.sort(reverse=True)
print(list)