#importando o modulo reduce da biblioteca functools
#biblioteca é um diretório de modulos 
from functools import reduce

#atribuindo o resultado do reduce a uma nova variável e criando uma função lambda para somar x e y e passando lista range(10)
# irá acumular as soma dos números de 0 a 9 na variável x
#printando o resultado acima
reduce(lambda x,y:x+y, range(11))

# equivalente a criar x = 0, percorrer um for range(10) e somar x com y percorrido no for
y=0
for a in range(11):
  y+=a
print(y)