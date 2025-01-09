

def plus_proche(ville, dist,visitees):
    pp=None
    for i in range(len(visitees)):
        if visitees[i]:
            continue
        if pp==None or dist[ville][i]<dist[ville][pp]:
            pp=i
    return pp

def voyageur(villes,dist,depart):
    n=len(villes)
    visitees=[False]*n
    courante=depart
    tab_villes=[None]*n
    total_dist=0
    for i in range(n-1):
        visitees[courante]=True
        suivante= plus_proche(courante,dist,visitees)
        total_dist+=dist[courante][suivante]*100
        tab_villes[i]=villes[courante]
        courante=suivante
    return [tab_villes, total_dist]

euros=[1,2,5,10,20,50,100,200]

def monnaies (s):
    i=len(euros)-1
    p=0
    while s>0:
        if s>=euros[i]:
            s-=euros[i]
            p+=1
        else:
            i-=1
    return p



def bin_packing(n,c,tab):
    p=[0]*(n+1)
    for elm in tab:
        for i in range (n+1):
            val=p[i]+elm
            if val<=c
            p[i]=val
            break
        if p[n]>0:
            return False
    return True