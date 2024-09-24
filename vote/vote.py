from random import randint
tab=(
  {"votants":3273 , "choix":[1,5,4,2,3]},
  {"votants":2182, "choix":[5,1,4,3,2]},
  {"votants":1818 , "choix":[5,2,1,4,3]},
  {"votants":1636 , "choix":[5,4,2,1,3]},
  {"votants":727 , "choix":[5,2,4,3,1]},
  {"votants":364 , "choix":[5,4,2,3,1]}
)



def SystemeDeBorda (tab):
    #chaque candidat a un nombre de point attribues en fonction des votes
    for j in
    t=[]*len(tab[0]["choix"])
    for i in range(len(tab[0]["choix"])):
      if tab[0]['choix'][i] == 1:
        t[i]=5
      elif tab[0]['choix'][i]==2:
        t[i]=4
  
