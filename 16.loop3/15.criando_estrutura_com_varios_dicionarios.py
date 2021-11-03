#criando estrutura com varios dicionarios
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
#criando for para percorrer os items do dicionario
for a,b in varios_dict.items():
  print(a,b)