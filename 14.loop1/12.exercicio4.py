'''4. Crie um for para reproduzir a sequência de Fibonacci.
A regra é a seguinte:
O primeiro número da série é 1
O segundo número da série é 1 também
O próximo número da série é sempre a soma dos dois anteriores'''

x = 0
y = 1
for i in range(10):
    print(x)
    b = x+y
    x = y 
    y = b