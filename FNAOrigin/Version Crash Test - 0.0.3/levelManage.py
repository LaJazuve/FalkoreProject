
import os
import importlib
import sys

sys.path.append("C:\\Users\\poste\\Archives\\Projets Python\\FNA EXPLORE\\Version Crash Test - 0.0.3\\level")


class niv:

    def __init__(self,nom,hero,room,objet):#+text et pnj 

        self.nom=nom
        self.hero=hero
        self.room=room
        self.objet=objet

def assembleur(lvl):
    
    print(lvl)
    
    LLL=importlib.import_module(lvl)
    dic=LLL.LOBJ
    bloc=niv(dic["Nom"],dic["Hero"],dic["Room"],dic["Objets"])

    return bloc

def listing():

    L=os.listdir("C:\\Users\\poste\\Archives\\Projets Python\\FNA EXPLORE\\Version Crash Test - 0.0.3\\level")
    
    n=0
    
    for i in L:
        n+=1
        if n!=len (L):
            print (n," : ",i)
        
        
            
    Choixnv=input("Quel niveau ? entré numero")
    Choixnv=int(Choixnv)-1
    
    name=L[Choixnv].split(".")
    lvl=assembleur(name[0])
    return lvl





