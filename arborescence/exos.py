import os
import xml.dom.minidom as dom

class Noeud:
    def __init__(self,v,f):
        self.valeur=v
        self.fils=f


def compte_balise(d,n):
    num=0
    if d.nodeName==n:
        num+=1
    for f in d.childNodes:
        num+=compte_balise(f,n)
    return num
    


def stat_xml(d):
    e=compte_balise(d,"e")
    for f in d.childNodes:
        if f.nodeValue!=None:
            a=compte_balise("d,f.nodeValue")
            t=compte_balise(d,"f.nodeValue")

    return (e,a,t)

doc= dom.parse("/home/tnsi-eleve4/Téléchargements/recette.xml")
y=stat_xml(doc)
print (y)

def gen_doc(n):
    pass