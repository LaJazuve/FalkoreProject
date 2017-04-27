###Liste Niveau

import BibliOBJ as Bobj


####niveau test

 


STI=Bobj.Salle("Salle Test interaction","une Salle toute blanche, carré.",False)

ZTPG=Bobj.Salle("Zone test position geographique","une autre salle carré...",True)

SE=Bobj.Salle("Salle équipement","des étagére",True)

SSoc=Bobj.Salle("SAlle Sociale","Une piece ou des gens attendent, tourne en rond",True)



#-----------------------OBJETS----------------------------

##STI
P1=Bobj.Porte("porte en acier",STI,ZTPG,False)#porte en 1er sinon les clef sont pas configurable



##ZTPG

P2=Bobj.Porte("pbnoir",ZTPG,SE,False)

##SE
P3=Bobj.Porte("porte en bois",SE,SSoc,True)
clefc=Bobj.Clef("clef en cuivre",P3,SE,False,True)

##SSoc



##########
lampe=Bobj.Lampe("lampe",False,False,"inventaire",True)

H=Bobj.Hero("Richard",SE)



LOBJ={}
LOBJ["Nom"] = ("Niveau Test")
LOBJ["Hero"]=H
LOBJ["Room"]=STI,ZTPG,SE,SSoc
LOBJ["Objets"]=P1,P2,P3,clefc,lampe








        
####Algorithme structure niveau

#description salle
#while :impression hero(feedback)
#commande
#feedback (fin boucle)


