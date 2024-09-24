
tab=(
  {"votants":3273 , "choix":[1,5,4,2,3]},
  {"votants":2182, "choix":[5,1,4,3,2]},
  {"votants":1818 , "choix":[5,2,1,4,3]},
  {"votants":1636 , "choix":[5,4,2,1,3]},
  {"votants":727 , "choix":[5,2,4,3,1]},
  {"votants":364 , "choix":[5,4,2,3,1]}
)

def maxim(t):
    max=0
    for p in range(len(t)):
        if t[p]>max:
            max=t[p]
            imax=p
    return imax


def SystemeDeBorda (tab):
    #chaque candidat a un nombre de point attribues en fonction des votes
    nbCandidat=len(tab[0]["choix"])
    t=[0]*nbCandidat
    for j in range(len(tab)):
        nbVotant=tab[j]["votants"]
        for i in range(nbCandidat):
            if tab[j]['choix'][i] == 1:
                t[i]+=5*nbVotant
            elif tab[j]['choix'][i]==2:
                t[i]+=4*nbVotant
            elif tab[j]['choix'][i]==3:
                t[i]+=3*nbVotant
            elif tab[j]['choix'][i]==4:
                t[i]+=2*nbVotant
            elif tab[j]['choix'][i]==5:
                t[i]+=1*nbVotant
    return "le gagant est le candidat" + str(maxim(t))