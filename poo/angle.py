from math import cos, sin, pi

class Angle:
    def __init__(self,a):
        if  0<=a<=360:
            self.angle=a
        else:
            raise ValueError
    
    def __str__(self):
        return str(self.a)+"degrés"
    
    def ajoute(self,ang2):
        if self.angle+ang2.angle<=360:
            self.angle+=ang2.angle
        else:
            self.angle+=ang2.angle - 360
        
    def cos(self):
        return cos(self.angle *pi//180)
    
    def sin(self):
        return sin(self.angle *pi//180)
    
    