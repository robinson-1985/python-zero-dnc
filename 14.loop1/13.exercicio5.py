# 5. Crie um for que execute até aparecer a palavra "parar".

palavras = ['continue','ok','segue','opa,','quase','parar',':)']
a = 0
for a in palavras:
  if a == 'parar':
    print(a,' = palavra encontrada')
    break
