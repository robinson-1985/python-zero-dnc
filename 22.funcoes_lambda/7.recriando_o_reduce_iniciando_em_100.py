#recriando o reduce acima porém com x iniciando em 100
# irá acumular as soma dos números de 0 a 9 na variável x, 
# porém, a variável x é inicializada como 100
from functools import reduce

print(reduce(lambda x,y:x+y, range(100)))

# equivalente a criar x = 0, percorrer um for range(10) e somar x com y percorrido no for
y=0
for a in range(100):
  y+=a
print(y)
# equivalent to