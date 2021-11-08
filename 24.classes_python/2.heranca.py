'''Herança
As classes podem herdar comportamentos e estados de outra classe, seguindo o exemplo acima, poderiamos ter a Classe Automóvel e a classe carro herdar os estados e comportamentos acima, se tornando uma sub classe de Automóveis.'''

class Carro():
  def __init__(self, litros, velocidade=0):
      self.litros = litros
      self.velocidade = velocidade

  def gasolina(self,litros=20):
    print("Tem ",self.litros," de gasolina")

  def acelera(self,velocidade=0):
    velocidade=self.velocidade
    if self.velocidade < 120:
      self.litros = self.litros-2
      print("Velocidade: ",self.velocidade,"\nQuantidade de litros de gasolina: ",self.litros)
    else:
      self.litros = self.litros-5
      print("Velocidade: ",self.velocidade,"\nQuantidade de litros de gasolina: ",self.litros)

class fiat_uno(Carro):
    def __init__(self):  # o construtor da subclasse chama o construtor da superclasse
                         # com parametros desejados
        Carro.__init__(self,litros=9,velocidade = 50)
    
    def escada(self):
        print("Nova velocidade ",self.velocidade*10," KM/h")

tunado = fiat_uno()
tunado.acelera()
tunado.escada()

tunado.litros=17
tunado.acelera()
