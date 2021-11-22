# 2. Percorra cada pet no dicionário e imprima e pet com maior quantidade de dislikes.

itemData = [
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

pet = ''
len1 = 0
for a in itemData:
    print(len(a['foods']['dislikes']),a['name'])
    if len1 < len(a['foods']['dislikes']):
        len1 += len(a['foods']['dislikes'])
        pet = a['name']
    print(pet)
