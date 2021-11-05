''' Funções Lambdas são funções no python que nos permite construir em apenas 
uma linha de código funções como vimos anteriormente. '''

#criando função lambda que soma x com x e atribuindo a f1
f1 = lambda x:x+2

#criando função lambda que eleva x ao quadrado e atribuindo a f2
print(f1(10))


#printando f1 e passando o x
f2 = lambda x,y:x+y

#printando f2 e passando o x
print(f2(10,12))