class Noeud:
    def ___init___(self,g,v,d):
        self.gauche=g
        self.droit=d
        self.valeur=v

def parfait(h):
    if h==0:
        return None
    else:
       return Noeud(parfait(h-1), h, parfait(h-1))