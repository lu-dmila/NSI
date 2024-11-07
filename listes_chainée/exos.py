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