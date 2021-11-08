'''Definição de classes em Python:

Geral:
Classes são usadas como prótotipos para instanciar objetos.

Objetos
Objetos são compostos basicamente de dois atributos:

Estado -> Informações salvas nos atributos dos objetos.
Comportamento -> ações que o objeto pode tomar, representam as funções e métodos dentro do objeto.

Classe
Classes são usadas para instanciar objetos, para ficar menos abstratos vamos aplicar em um exemplo ilustrativo.

Criamos a Classe Carro
Objetos dessa classe poderiam ser Fiat Uno, VW Gol, Corolla
Estado (Atributos) seriam Gasolina, óleo, água...etc.
Comportamentos (Funções e métodos) seriam acelerar, freiar... etc.

Vamos ver como isso funcionaria na prática:  '''

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

#pode dar o nome que quiser desde que não seja numeros nem palavras reservadas do python
uno = Carro(litros=10) 

uno.gasolina()#acessando função gasolina
uno.velocidade=120
uno.acelera()
uno.velocidade=99
uno.acelera()
uno.litros=uno.litros+32
uno.acelera()
