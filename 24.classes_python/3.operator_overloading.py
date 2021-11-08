'''Sobrecarga de operador (Operator Overloading) Classes podem interceptar operadores especiais e sobrescrevê-los. Esses métodos são definidos por um duplo underscore antes e depois da escrita. Exemplos de operadores especiais são:

__init__ construtor do objeto
__repr__ método que gera uma representação da classe
__add__ método que define a operação de soma +
__lt__, __gt__, para comparações X < Y, X > Y
e outras...'''

class pessoa():
    def __init__(self,nome = '', sobrenome = '', idade = 0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def __lt__(self,p):  # operador '<'
        return(self.idade < p.idade)  # retorna True se a idade da instancia da classe for menor
    
    def __gt__(self,p):  # operador '>'
        return(self.idade > p.idade)

p1 = pessoa(nome='Peter',sobrenome='Almeida',idade=50)    # instancia um objeto 'pessoa'
p2 = pessoa(nome='Daniel',sobrenome='Soria',idade=52) # instancia outro objeto 'pessoa'

if p1 < p2:
    print(p1.nome, ' eh mais novo que ',p2.nome)
else:
    print(p1.nome, ' nao eh mais novo que ',p2.nome)