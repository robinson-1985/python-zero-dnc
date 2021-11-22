''' 4. Crie uma classe chamada Calculadora com os atributos Digito 1 e Digito 2, crie 
os métodos de adição e de subtração. '''

class Calculadora():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subtrai(self, x, y):
        return x - y

    def subtrai(self, x, y):
        return x + y

soma = Calculadora()
soma.add(10, 20)