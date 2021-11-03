#percorrendo os items do dicionario com enumerate

varios_dict = {
  "aluno" : {
    "name" : "fulano",
    "year" : 1985
  },
  "aluno2" : {
    "name" : "ciclano",
    "year" : 1999
  },
  "aluno3" : {
    "name" : "Linus",
    "year" : 2021
  }
}

for a,b in enumerate(varios_dict.items()):
  print(a,b)