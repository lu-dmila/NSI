class Chrono:
    heure_max=24

    def __init__(self,h,m,s):
        self._temps=3600*h+60*m+s

    def avance(self,s):
        self._temps +=s

    def _coversion(self):
        s=self._temps
        return (s//60)