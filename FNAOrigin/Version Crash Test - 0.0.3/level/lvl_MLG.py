#####Level test - Maison de Lady Gatling et vague d'ennemi

import BibliOBJ as Bobj


### Liste Event et leur declencheur


### les differentes Salle

Ch=Bobj.Salle("Chambre de Lady Gatling"," Petite Chambre d'hotel Sobre et luxueuse, le papier peint est sombre, une grande baie vitrée donne sur un jardin les meuble son gris", True)

Jard = Bobj.Salle("Jardin de residence","un carré d'herbe avec une fontaine au centre, et un banc dos au la baies vitrées", True)

Coul=Bobj.Salle("Le Couloir"," un couloir reliant les differente piéce de l'appartement avec à l'une des extremité le salon et l'aautre l'entrée",True)

Sal = Bobj.Salle("Salon", "Simple salon donant sur la cuisine, avec une baie vitrée donnant sur le jardin", True)

Cuis = Bobj.Salle("Cuisine", "Trés petite Cuisine avec tout le nécéssaire, une lucarne avec des barreau donnant sur la rue", True)

####OBJETS

#Ch
P1=Bobj.Porte("Baie vitrée de la chambre",Ch,Jard,False)
P2=Bobj.Porte("Porte peint en gris sombre",Ch,Coul,False)

#Jard
P3=Bobj.Porte("Baie vitrée du Salon",Jard,Sal,False)

#Coul
P4=Bobj.Porte("vers le salon", Coul,Sal,False)
P5=Bobj.Porte("Porte d'entrée",Coul, Coul,True)

#Sal
P6=Bobj.Porte("vers la cuisine",Sal,Cuis,False)

#####

#inventaire :

#Player :
H=Bobj.Hero("Richard", Ch)

#Indexion du niveau :

LOBJ={}
LOBJ["Nom"] = ("Refuge de Lady Gatling")
LOBJ["Hero"]=H
LOBJ["Room"]=Ch,Jard,Coul,Sal,Cuis
LOBJ["Objets"]=P1,P2,P3,P4,P5,P6



