# 2. Refaça o exercício 1 mas dessa vez pulando os espaços.

texto = ('Adeus mundo cruel e doloroso')
for a, b in enumerate(texto):
    if b != " ":
        print(a, b)