
tab=(
  {"votants":3273 , "choix":[1,5,4,2,3]},
  {"votants":2182, "choix":[5,1,4,3,2]},
  {"votants":1818 , "choix":[5,2,1,4,3]},
  {"votants":1636 , "choix":[5,4,2,1,3]},
  {"votants":727 , "choix":[5,2,4,3,1]},
  {"votants":364 , "choix":[5,4,2,3,1]}
)

def maxim(t):
    maxi=0
    imax=None
    for p in range(len(t)):
        if t[p]>maxi:
            maxi=t[p]
            imax=p
    return imax

def SystemeDeBorda (tab):
    #chaque candidat a un nombre de point attribues en fonction des votes

    nbCandidat=len(tab[0]["choix"])
    t=[0]*nbCandidat
    for j in range(len(tab)):
          b=0
        nbVotant=tab[j]["votants"]
        for i in range(nbCandidat):
            b+=1
            t[i]+=(nbCandidat-b+1)*nbVotant
    return "le gagnant est le candidat" + str(maxim(t))

def minim(t):
       mini=float('inf')
       imin=None
               for p in range(len(t)):
                      if t[p]<mini:
                               mini=t[p]
                               imin=p
        return imin

def LastManStanding (tab):
    #a chaque tours le candidat ayant le moins de votes est elimine
    t=[]
    for votes in tab:
        for candidats in tab["choix"]:
            if candidats not in t:
                t.append(candidats)
    while len (t) > 1:
        tabvote=[0]*len(t)
        for votes in tab:
            a=0
            for candidats in votes["choix"]:
                if votes["choix"][a]==1:
                    tabvote[a]+=votes[a]
                    a+=1
        tabvote.pop(minim(tabvote))
        t.pop(minim(tabvote))
    return "le gagnant est le candidat" + str(t)    

def unTours(tab):
    #le plus de vote gagne
      gagnant=0
    candidats=[0]*len(tab)
    for i in range( len(tab)):
        candidats[i]=tab[i]["votants"]
    for j in range (tab[maxim(candidats)]["choix"]):
          if tab[maxim(candidats)]["choix"][j]==1:
                         gagnant=j
     return "le gagnant est le candidat" + str(gagnant)
