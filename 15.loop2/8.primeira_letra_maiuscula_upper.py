#deixando a primeira letra de cada palavra maiúscula

texto = 'Justo eterno santo unico salvador'
texto_2 = texto.split()
for a in texto_2:
  print(a[0].upper()+a[1:])