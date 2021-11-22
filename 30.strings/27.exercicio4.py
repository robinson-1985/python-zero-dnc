# 4. Conte a quantidade de linhas que aparece na string.

texto = 'O tempo é muito lento para os que esperam\nMuito rápido para os que têm medo\nMuito longo para os que lamentam\nMuito curto para os que festejam\nMas, para os que amam, o tempo é eterno\n(Henry Van Dyke)'
linhas = [a for a in texto.splitlines()]
print('Quantidade de linhas: ',len(linhas))