def point(x,y):
    return(x,y)

def deplacer(p,dx,dy):
    return point(p[0]+dx,p[1]+dy)

def triangle(p1,p2,p3):
    return (p1,p2,p3)


class Point:
    def __init__(self,x,y):