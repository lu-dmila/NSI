class Simulateur:
    repartiteurs = {"Un" : "RepartiteurUn", "Alea" : "RepartiteurAlea", "Choix" : "RepartiteurChoix"}

    def __init__(self):
        self._repartiteur=None
        self._tick=0
        self._clientsServis=0
        self.max=0
        self.nbTours=0
        #attributs rajoutés
        self.nbGuichets=0
        self._totalAttente=None
        self.guichets=[]


    def config(self):
        #lorna
        """configure le simulateur selon les inputs des utilisateurs"""
        print("Mode de répartition ?")
        self._repartiteur=self.repartiteurs[input()]
        print("Nombre de guichets ?")
        self.nbGuichets=input()
        print("temps de traitement maximal aux guichets ?")
        self.max = input()
        print("nombres de tours de la simulation ?")
        self.nbTours = input()

    def demarre(self):
        """lance la simulation et retourne le nombre de clients servis et l'attente totale"""
        #boucle qui decremente tick(tt le tps)(actions entre) lance un tour sur tous les guichets et ajoute un client a la file.
        self.config()
        while self._tick != 0:
            for i in range( len(self.guichets)): 
                self.guichets[i].tour()  #num du guichet dans Guichet???
            self.repartiteur.entree_client()
            self._tick-=1
        return ("clients servis : "+str(self._clientsServis), "attente totale : "+str(self._totalAttente))