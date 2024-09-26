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