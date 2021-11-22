''' 5.Utilize pelo menos mais 3 métodos próprios pra string que não apareceu em aula mas 
estão na referência.'''

texto = 'O tempo é muito lento para os que esperam\nMuito rápido para os que têm medo\nMuito longo para os que lamentam\nMuito curto para os que festejam\nMas, para os que amam, o tempo é eterno\n(Henry Van Dyke)'

print(texto.encode())

print(texto.count('Muito'))

palavra = [a for a in texto if a.startswith('tempo')]
print(palavra)