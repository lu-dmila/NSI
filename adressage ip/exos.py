#matrice
class Graphe:
    def __init__(self,n):
        self.n=n
        self.adj=[[False]*n for _ in range (n)]

    def ajouter_arc(self,s1,s2):
        self.adj[s1][s2]=True

    def arc(self,s1,s2):
        return self.adj[s1][s2]
    
    def voisins(self,s):
        v=[]
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v
    
    def degre(self,s):
        d=0
        for v in self.adj[s]:
            if v==True:
                d+=1
        return d
    
    def nb_arc(self):
        nb=0
        for i in range(len(self.adj)):
            for v in len(self.adj[i]):
                if v==True:
                    nb+=1
        return nb
    
    def supprimer(self,s1,s2):
        if self.adj[s1][s2]==True:
            self.adj[s1][s2]=False

#dictionnaire
class Graphe2 :
    def __init__(self):
        self.adj={}
    
    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s]= set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self,s1,s2):
        return list(self.adj)
    
    def voisins(self,s):
        return self.adj[s]
    
    def nb_sommets(self):
        nb=0
        for clef in self.adj:
            nb+=1
        return nb
    
    def degre(self,s):
        nb=len(self.adj[s]) 
        return nb
    
    def nb_arcs(self):
        pass


#ex3
def parcours_largeur(g,source):
    dist={source:0}
    courant={source}
    suivant=set()
    while len(courant)>0:
        s=courant.pop()
        for v not in dist:
            suivant.add(v)
            dist[v]=dist[s]+1
        if len(courant)==0:
            courant,suivant=suivant,set()
    return dist

def distance(g,u,v):
    dist= parcours_largeur(g,u)
    return dist[v] if v in dist else None

assert distance(g,occitanie,ocitanie)==0
assert distance (g, bretagne, occitanie)
assert distance (g,guadeloupe,martinique)

