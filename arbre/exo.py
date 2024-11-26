class Noeud:
    def ___init___(self,g,v,d):
        self.gauche=g
        self.droit=d
        self.valeur=v


def str_arbre(a):
    c=""
    if a!=None:
        while a.gauche!=None:
            c+="("+str(a.gauche)
            a.gauche= a.gauche.gauche
        c+=")"

        
        
        
        
        print("("+c+"(")