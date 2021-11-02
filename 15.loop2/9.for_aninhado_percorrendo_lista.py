#for aninhado percorrendo a lista

texto = 'Eu vou fazer todos os exercícios'
texto_2 = texto.split()
for a in texto_2:
  for b in texto_2:
    print(a,b)