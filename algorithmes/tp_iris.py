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
    for i in range(len(data)):
        data[i]['distance']=distance(data[i]['petal_lenth'],data[i]['petal_width'],new_x,new_y)
    return None

def trier(data,clef):
    data.sort(key= lambda f:f[clef])
    return None
 
trier([{'distance':5},{'distance':1}],'distance')

def knn (new_x,new_y,data,k):
    o=0
    i=0
    z=0
    aj_distance(new_x,new_y,data)
    trier(data,'distance')
    for i in range(k-1):
        if data[i]['espece']==0:
            o+=1
        

readCSV("/home/tnsi-eleve4/Documents/NSI/algorithmes/","iris.csv")