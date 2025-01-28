from file import *
from random import randint
        
def _creerClient(tick):
    """cree un client à partir de l'horloge et le renvoie"""
    c=Client(tick)
    return c

class Repartiteur:
    #lorna
    def __init__(self,s):
        self.attenteTotale=0
        self.files=[]
        self.simul=s
            
    def entree_client(self):
        """ajoute un entier représentant le tour d'arrivée du client"""
        raise NotImplemented()
    
    def sortie_client(self,num):
        """retire un client de la file et ajoute son temps d'attente au total. 
        num est le numero du guichet."""
        raise NotImplemented()
    
class RepartiteurUn(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        f=File()
        self.files.append(f)

    def entree_client(self):
        c = _creerClient(self.simul._tick)
        self.files[0].ajouter(c)
    
    def sortie_client(self, num=1):
        if not self.files[0].est_vide():
            c=self.files[0].retirer()
            self.simul._totalAttente += (self.simul._tick - c.temps_arrivee)


class RepartiteurAlea(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        for _ in range(len(self.simul.guichets)):
            f=File()
            self.files.append(f)
        
    def entree_client(self):
        c=_creerClient(self.simul._tick)
        ifile = randint(0, len(self.files)-1)
        self.files[ifile].ajouter(c)

    def sortie_client(self, num):
        #soit num le numero identifiant du guichet entre 1 et nbGuichets du simulateur inclus
        if not self.files[num-1].est_vide():
            c = self.files[num-1].retirer()#-1 car passage de numero à indice ds le tableau files
            self.simul._totalAttente += (self.simul._tick - c.temps_arrivee)
        #on peut faire en sorte de renvoyer le client retirer ( pour le guichet.) Souhaitable ?


class RepartiteurChoix(Repartiteur):
    def __init__(self, s):
        super().__init__(s)
        for _ in range(len(self.simul.guichets)):
            f=File()
            self.files.append(f)

    def _lenfiles(self) -> list :
        lenfiles=[]
        for i in range(len(self.files)):
            lenfiles.append(len(self.files[i]))
        return lenfiles

    def _imin_file(self) :
        lenfiles=self._lenfiles()
        lenmin=lenfiles[0]
        imin=0
        for i in range(1, len(lenfiles)):
            if lenfiles[i]<lenmin :
                imin = i
        return imin
                       
    def entree_client(self):
        c=_creerClient(self.simul._tick)
        ifile = self._imin_file()
        self.files[ifile].ajouter(c)

    def sortie_client(self, num):
        if not self.files[num-1].est_vide():
            c = self.files[num-1].retirer()   
            self.simul._totalAttente += (self.simul._tick - c.temps_arrivee)


class Client:
    #lorna
    def __init__(self,tick):
        self.temps_arrivee=tick

    def __str__(self):
        return str(self.temps_arrivee)
            
class Guichet:

    def __init__(self, s, num): 
        self.simul = s
        self.traitement = 0
        self.numero = num #numero du guichet
        self.avecClient = False


    def tour(self):
        """soustrait le temps de tratement restant si le gichet est occupé, sinon prend un nouveau client
     et augmente le nombre de client servis"""
    # Si le guichet est occupé, on continue de réduire le temps de traitement
        if self.traitement > 0:
            self.traitement -= 1
        else:
        # Si le guichet est libre, on retire un client de la file d'attente et on l'enregistre comme traité
            if self.avecClient == True :
                self.simul._repartiteur.sortie_client(self.numero)
                self.avecClient = False
                self.simul._clientsServis += 1
            if self.simul._repartiteur.files[0]._longueur > 0 :  # s'il y a encore des clients dans la file
                self.traitement = randint(1, self.simul.max)
                self.avecClient = True