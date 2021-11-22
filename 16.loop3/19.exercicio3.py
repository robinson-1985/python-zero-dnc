 # 3. Conte o total de comidas citadas no dicionário e quantas se repetem.

lista = []
valor = []
itemData =  [
              {
                "name": "Meowsy",
                "species" : "cat",
                "foods": {
                  "likes": ["tuna", "catnip"],
                  "dislikes": ["ham", "zucchini"]
                }
              },
              {
                "name": "Barky",
                "species" : "dog",
                "foods": {
                  "likes": ["bones", "carrots"],
                  "dislikes": ["tuna"]
                }
              },
              {
                "name": "Purrpaws",
                "species" : "cat",
                "foods": {
                  "likes": ["mice"],
                  "dislikes": ["cookies"]
                }
              }
            ]

comidas = []
for a in itemData:
    for b in a ['foods']['dislikes']:
        comidas.append(b)
    for c in a ['foods']['likes']:
        comidas.append(c)
print(comidas)

lista.count(valor)
for a in comidas:
    print(comidas.count(a), a)