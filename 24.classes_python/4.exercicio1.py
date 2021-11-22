# 1. Recrie a classe Carro e adicione um novo atributo e um novo método (função).

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
            

