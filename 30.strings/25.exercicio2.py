# 2. Conte a quantidade de nomes próprios e de números que aparecem na história.

texto = 'O tempo é muito lento para os que esperam\nMuito rápido para os que têm medo\nMuito longo para os que lamentam\nMuito curto para os que festejam\nMas, para os que amam, o tempo é eterno\n(Henry Van Dyke)'

titles = [a for a in texto.split() if a.istitle()]
numeros = [a for a in texto.split() if a.isnumeric()]
print('Quantidade de nomes ou palavras com letras maiúsculas:  ',len(titles),'\nQuantidade de Num: ',len(numeros))
