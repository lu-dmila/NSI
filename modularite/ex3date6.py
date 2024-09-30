def cree():
    return [0]*6

def contient(s,x):
    iEntier = x//64
    bit = x%64
    return (s[iEntier]&(1<<bit) != 0)

def ajoute(s,x):
    iEntier = x // 64
    bit = x % 64
    s[iEntier]= s[iEntier] | 1 << bit

def enumere(s):
    tab = []
    for j in range(len(s)):
        for i in range (64):
            if s[j]&2**i ==1:
                tab.append(i+64*j)
    return tab


def tranche(t,i,j):
    tab=[]
    if j>i:
        return[t[k]for k in range(i,j)]
    else:
        return[]

def concatenate(t1,t2):
    t3=[]
    for elm in t1:
        t3.append(elm)
    for elm in t2:
        t3.append(elm)
    return t3