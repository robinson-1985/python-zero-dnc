# 3.Sobreescreva um dos operadores dentro de uma nova classe.

class Carro():
    def __init__(self, litros, velocidade = 0, buzina = 'BIBI!!'):
        self.litros = litros
        self.velocidade = velocidade
        self.buzina = buzina

    def aciona_buzina(self, litros = 20):
        print(self.buzina)

    def gasolina(self, litros = 20):
        print('Tem', self.litros, ' de gasolina')

    def acelera(self, velocidade = 0):
        velocidade = self.velocidade
        if self.velocidade < 120:
            self.litros = self.litros - 2
            print('Velocidade: ', self.velocidade, '\nQuantidade de litros de gasolina: ', self.litros)
        else:
            self.litros = self.litros-5
            print('Velocidade: ', self.velocidade, '\nQuantidade de litros de gasolina: ', self.litros)

class gol_bolinha(Carro):
    def __init__(self):

        Carro.__init__(self, litros = 9, velocidade = 50)

    def __lt__(self, p):
        return (self.idade < p.idade)