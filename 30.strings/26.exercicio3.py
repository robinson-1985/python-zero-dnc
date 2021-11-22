# 3. Conte a quantidade de vogais que aparecem na história.

texto = 'O tempo é muito lento para os que esperam\nMuito rápido para os que têm medo\nMuito longo para os que lamentam\nMuito curto para os que festejam\nMas, para os que amam, o tempo é eterno\n(Henry Van Dyke)'
vogais = [a for a in texto if a in ['a','e','i','o','u']]
print('Quantidade de vogais: ',len(vogais))
