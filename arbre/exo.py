from random import randint

class Noeud:
    def ___init___(self,g,v,d):
        self.gauche=g
        self.droit=d
        self.valeur=v
def ajoute(x,a):
    if a is None:
        return Noeud(None,x,None)
    elif x<a.valeur:
        return Noeud(ajoute(x,a.gauche), a.valeur, a.droit)
    else:
        return Noeud(a.gauche, a.valeur, ajoute(x,a.droit))
    
def ajoute2(x,a):
    if appartient(x,a)==True:
        return a
    else:
        return ajoute(x,a)
    
def remplir(a,t):
    if a is None:
        return None
    remplir(a.gauche,t)
    t.append(a.valeur)
    remplir(a.droit,t)    
    
def appartient(x,a):
    if a is None:
        return False
    elif x<a.valeur:
        return appartient(x,a.gauche)
    elif x>a.valeur:
        return appartient(x,a.droit)
    else:
        return True
    
def supprime_minimum(a):
    assert a is not None
    if a.gauche is None:
        return a.droit
    else:
        return Noeud(supprime_minimum(a.gauche),a.valeur,a.droit)
    
def supprime(x, a):
    if a is None:
        return None
    elif x<a.valeur:
        return Noeud(supprime(x,a.gauche,a.valeur, a.droit))
    elif x>a.valeur:
        return Noeud(a.gauche, a.valeur,supprime(x,a.droit))
    elif a.droit is None:
        return a.gauche
    else:
        return Noeud(a.gauche, minimum(a.droit),supprime_minimum(a.droit))
    
class ABR:
    def ___init___(self):
        self.racine=None

    def ___contains___(self,x):
        return appartient(x,self.racine)
    
    def ajouter(self,x):
        self.racine=ajoute(x,self.racine)

    def supp(self,x):
        return supprime(x,self)
    
    def lister(self):
        t=[]
        remplir(self.racine,t)
        return t
        
def trier(t):
    a=ABR()
    for i in t:
        a.ajouter(i)
    return a.lister()

def melange(t):
    for i in range(len(t)):
        j=randint(0,i)
        t[i],t[j]==t[j],t[i]


def minimum(a):
    if a is None:
        return None
    else:
        while a.gauche != None:
            a=a.gauche
        return a.valeur

def minimum2(a):
    if a is None:
        return None
    elif a.gauche is None:
        return a.valeur
    else:
        return minimum2(a.gauche)