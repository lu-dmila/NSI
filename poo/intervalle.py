class Intervalle :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def est_vide(self):
        return self.b<=self.a
        
    def __len__(self):
        if self.b<=self.a:
            return 0
        else:
            return self.b-self.a
        
    def __contains__(self,x):
        if x<= self.b and x>= self.a:
            return True
        
    def __eq__(self,inter):
        if self.b>self.a:
            return inter.a== self.a and inter.b== self.b
        else:
            return inter.b<=inter.a
        
    def __le__(self,inter):
        if inter.b<=inter.a:
            return True
        else:
            return inter.a>= self.a and inter.b<= self.b
        
    def intersection (self, inter):
        if self==inter:
            pass