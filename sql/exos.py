import csv
import sqlite3 as sgbd

class Usager:
    def __init__(self,code_barre):
        self.cnx = sgbd.connect('/home/mediatheque.db')
        self.code_barre = self.code_barre

    def __del__(self):
        self.cnx.close()

    def emprunter(self,isbn):
        c = cnx.cursor()
        c.execute( INSERT INTO emprunt VALUES('self.code_barre','self.isbn',) )


    def rendre(self, isb):
        
    def emprunts(self):


        
    cnx=sgbd.connect('/home/')