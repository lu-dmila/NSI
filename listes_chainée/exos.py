class Cellule:

    def __init__(self,v,s):
        self.valeur=v
        self.suivante=s

def niem_element(n,lst):
    i=n
    c=lst
    while i !=0:
        if c is None:
            raise IndexError
        else:
            i=-1
            c=c.suivante
    return c.valeur

def occurence(x,lst):
    if lst is None:
        return 0
    elif lst.valeur ==x:
        o=occurence(x,lst.suivante)
        return o+1
    else:
        return o
    
def w_occurence(x,lst):
    l=lst
    nb=0
    while l is not None:
        if l.valeur ==x:
            nb=+1
        l=l.suivantes
    return nb

def trouve(x,lst):
    if lst is None:
        raise ValueError
    elif lst.valeur!=x:
        o= trouve(x,lst.suivante)
    else:
        return lst.valeur

def identique(l1,l2):
    if l1 is None:
        if l2 is None:
            return True
        else:
            return False
    elif l2 is None:
        return False
    elif l1.valeur == l2.valeur:
        return identique(l1.suivante,l2.suivante)
    else:
        return False
    
def inserer(x,lst):
    if lst is None:
        return Cellule(x,None)
    elif lst.valeur>=x:
        return Cellule(x,lst)
    else:
        return Cellule(lst.valeur,inserer(x,lst.suivante))



