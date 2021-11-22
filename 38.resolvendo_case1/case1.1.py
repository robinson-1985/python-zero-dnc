'''Uma empresa te enviou 3 listas, uma representa a largura, outra representa a 
altura e a terceira representa a área em m2 de determinado terreno, todas estão 
ordenadas entretanto tem alguns valores faltantes que precisam ser preenchidos, 
preencha os valores faltantes:

Todos os terrenos dessa empresa são retangulares e você pode utilizar a fórmula 

abaixo:

a = b. h (área = largura * altura)

Utilize as listas abaixo:

area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
altura = ['null',30,40,30,10,25,33,'null',12,20]
largura = [20,20,'null',50,100,'null',30,100,200,10]'''

area = [200,'null',720,1500,1000,275,'null',1200,2400,'null']
altura = ['null',30,40,30,10,25,33,'null',12,20]
largura = [20,20,'null',50,100,'null',30,100,200,10]
print(len(area),len(altura),len(largura))

def preenche (a,b,h):
    area_full = []
    largura_full = []
    altura_full = []
    for area, largura, altura in zip(a, b, h):
        if type(area) != int:
            area_full.append(int(largura*altura))
        else:
            area_full.append(area)
        if type(largura)!=int:
            largura_full.append(int(area/altura))
        else:
            largura_full.append(largura)
        if type(altura)!=int:
            altura_full.append(int(area/largura))
        else:
            altura_full.append(altura)
    return (area_full, largura_full, altura_full)

(area, largura, altura)= preenche(area, largura, altura)
print(area)
print(largura)
print(altura)
