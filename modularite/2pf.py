def applique(f,t):
    tab = t[:]
    for i in range (len(t)):
        tab[i]=f(t[i])
    return tab

def applique2(f,t):
    tab = [f(x)for x in t]
    return tab


def calcule(op,t,f):
    v=f(t[0])
    for i in range(1,len(t)):
        v=op(v,f(t[i]))
    return v

def compose(f,g):
    def h(x):
        return f(g(x))
    return h
