import os
import csv
from math import sqrt

def readCSV (dossier, fichier):
    fichier=os.path.join(dossier,fichier)
    with open(fichier,mode="r", newline="",encoding="utf-8")as csvFile:
        reader=list(csv.DictReader(csvFile))
        lignes=[valide(ligne) for ligne in reader]
    return lignes

def valide(l):
    dict={}
    for clef in l:
        dict[clef]=float(l[clef])
    return dict

def distance(x1,y1,x2,y2):
    d=sqrt((x1-x2)**2 +(y1-y2)**2)
    return d

def aj_distance(new_x,new_y,data):
    
    distance(x1,y1,new_x,new_y)
    return None
readCSV("/home/tnsi-eleve4/Documents/NSI/algorithmes/","iris.csv")