import os
class Noeud:
    def __init__(self,v,f):
        self.valeur=v
        self.fils=f

def fonction_repertoires(r):
    abr=Noeud(r,[])
    if os.path.isdir(r)==True:
        t=os.listdir(r)
        for elt in t:
            abr.fils.append(fonction_repertoires(os.path.join(r,elt)))
    return abr

fonction_repertoires("/home/tnsi-eleve4/Documents/NSI/arbre/")