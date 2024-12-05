class Noeud:
    def ___init___(self,v,f):
        self.valeur=v
        self.fils=f

def parcours_prefixe(a):
    ch=a.valeur
    for f in a.fils:
        ch+=parcours_prefixe(f)
    return ch


def affiche(a,c):
    ch=a.valeur
    