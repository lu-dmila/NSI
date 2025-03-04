
#ex 3
def fusion(t,g,m,d):
    n1=m-g+1
    n2=d-m
    for i in range(n1-1):
        lg[i]=t[g+i]
    for j in range(n2-1):
        ld[j]t[m+1+j]
        if lg[-1]>ld[-1]:
            lg[n1]=lg[-1]+1
            ld[n1]=lg[-1]+1
        else:
            lg[n1]=ld[-1]+1
            ld[n1]=ld[-1]+1
        i=0
        j=0
        for k in range(g,d):
            if lg[i]<=ld[j]:
                t[k]=lg[i]
                i+=1
            else:
                t[k]=ld[j]
                j+=1

#ex4
def fusion(l1,l2):
    v1=l1.valeur
    v2=l2.valeur
    lst=(None)
    if l1==None and l2!=None:
        lst=(lst,(l2,(None)))
        return lst
    elif l2==None and l1!=None:
        lst=(lst,(l1,(None)))
        return lst
    elif v1>v2:
        lst=(lst,(v1,(None)))
        v1=l1.suivante
        fusion(l1,l2)
    else:
        lst=(lst,(v2,(None)))
        v2=l2.suivante
        fusion(l1,l2)

def fusion(l1,l2):
    v1=l1.valeur
    v2=l2.valeur
    lst=None
    while l1!=None or l2!=None:
        if v1>v2:
            lst=(lst,(v1,(None)))
            v1=l1.suivante
        else:
            lst=(lst,(v2,(None)))
            v2=l2.suivante
    if l1==None:
        lst=(lst,(l2,(None)))
    else:
        lst=(lst,(l1,(None)))
    return lst

#ex5
def divise(lst):
    l1,l2=None,None
    while lst is not None:
        l1,l2=Cellule(lst.valeur,l2),l1
        lst=lst.suivante
    return l1,l2

divise((8,(1,(3,(0,(1,(2,(5,(None)))))))))  


#ex7


class Cellule:
    def __init__(self,v,s):
        self.valeur=v
        self.suivante=s

class Pile:
    def __init__(self):
        self._contenu=None

    def est_vide(self):
        return self._contenu is None
    
    def empiler(self, e):
        self._contenu=Cellule(e,self._contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("depile une pile vide")
        v=self._contenu.valeur
        self._contenu=self._contenu.suivante
        return v
    
#ex9
def hannoi (k):
    a=Pile()
    b=Pile()
    c=Pile()
    for i in range (k-1):
        a.empiler(i)
    deplacement_bis(a,b,c,k)

def deplacement_bis(a,b,c,k):
    if k==1:
        d=a.depiler()
        b.empiler(d)
    else:
        deplacement_bis(a,c,b,k-1)
        deplacement_bis(a,b,c,1)
        deplacement_bis(c,b,a,k-1)

