from graph import Graphe
from region g 

def parcours_largeur(g, source):
    """parcours en largeur depuis le sommet source"""
    dist = {source: 0}
    courant = {source}
    suivant = set()
    while len(courant) > 0:
        s = courant.pop()
        for v in g.voisins(s):
            if v not in dist:
                suivant.add(v)
                dist[v] = dist[s] + 1
        if len(courant) == 0:
            courant, suivant = suivant, set()
    return dist

def distance(g, u, v):
    """distance de u à v et None si pas de chemin"""
    dist = parcours_largeur(g, u)
    return dist[v] if v in dist else None

assert distance(g,"Normandie","Normandie")==0
assert distance(g,"Normandie","Bretagne")
assert distance(g,"Guyane","Martinique")

#ex7
class Noeud:
    def ___init___(self,g,v,d):
        self.gauche=g
        self.droit=d
        self.valeur=v

def parcours_largeur_arbres(abr):
    """parcours en largeur depuis le sommet source"""
    dist = {abr.valeur: 0}
    courant = {abr.valeur}
    suivant = set()
    while len(courant) > 0:
        s = courant.pop()
        d=s.droit
        g=s.gauche
        if d.valeur not in dist:
                suivant.add(d.valeur)
                dist[d.valeur] = dist[abr.valeur] + 1
        if g.valeur not in dist:
                suivant.add(g.valeur)
                dist[g.valeur] = dist[abr.valeur] + 1
        if len(courant) == 0:
            courant, suivant = suivant, set()
    return dist