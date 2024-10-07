class Fration:
    
    def __init__(self, num, denom):
        if denom<0:
            raise ValueError
        self.num=num
        self.denom=denom
        
    def __str__(self,num ,denom):
        if denom==1:
            return num
        else:
            return str(num) + "/" + str(denom)
        
    def __eq__(self,v):
        return self.num*v.denom==v.num*self.denom
    
    def __lt__(self, u):
        return self.num/self.denom<u.num/u.denom
    
    def __add__(self, o):
        pass