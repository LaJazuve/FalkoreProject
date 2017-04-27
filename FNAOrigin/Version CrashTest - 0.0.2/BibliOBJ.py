##Bibliothéque Item
######Decor
import Fonct

        
class Hero:

    def __init__(self,nom,position,sac):

        self.nom = nom
        self.position = position
        self.sac=sac


    def voir(self,dic):     
            
        liste=[]

        

        for i in dic:
            

            if not hasattr(i,"pos_b"):

                if i.position==self.position or i.position==("inventaire"):
                    liste.append(i.nom)
                    
            elif i.pos_b==self.position or i.position == self.position:
                
                liste.append(i.nom)###contourne le big des portes
                    
      
        if len(liste)==0:
            print ("Il n'y a rien")
        else:
            print ("Il y a : ",liste)



    def utiliser(self,obj):

        if  obj.lock==False and (self.position == obj.position or obj.position =="inventaire"):##utiliser objets de la piece
            obj.use(self)
            
        elif obj.lock==False and self.position==obj.pos_b:###pour porte 
            obj.use(self)

        else:
            print ("Cela ne marche pas...")


class Obj:
    """""Objet lambda de teste"""
              
    def __init__(self,nom,propriete,fonction,lock,position,port):
        
        self.nom = nom
        self.propriete = False
        self.lock = False
        self.position = position
        self.port=True


        
class Salle:

    def __init__(self,nom,description,vision,port):

        self.nom = nom
        self.description = description
        self.vision=vision
        self.port=False

class Porte:

    def __init__(self,nom,position,pos_b,lock,port):

        self.nom = nom
        self.position = position
        self.pos_b = pos_b
        self.lock = lock
        self.port=False

    def use(self,h):

        if h.position == self.position:
            h.position=self.pos_b
            
        elif h.position == self.pos_b:
            h.position=self.position
            
        Fonct.command("voir")

class Clef:

    def __init__(self,nom,porte,position,lock,port):

        self.nom=nom
        self.porte=porte
        self.position=position
        self.lock=lock
        self.port=port

    def use(self,h):

        P=input("sur quoi ?")
        
        Pp=Fonct.command(P)#recupére la vrai porte a partir de la string

        
        if self.porte==Pp:
            print ('ça passe')

            if Pp.lock==False:
                Pp.lock=True
                print("Vous avez fermé la porte à clef...")

            elif Pp.lock==True:
                Pp.lock=False
                print("Vous avez ouvert la porte...")
    

class Lampe:
              
    def __init__(self,nom,propriete,lock,position,port):
        
        self.nom = nom
        self.propriete = False
        self.lock = False
        self.position = position
        self.port=True

    def use(self,h):

        if self.propriete == False :

            self.propriete = True

            if type(self.position)==str:
                
                h.position.vision=True
                print("La Lumiere S'allume...")##pensé a éteindre quand quitte la piece si c'est lampe de poche de l'inventaire.
                Fonct.command("voir")
                
            else:
                
                self.postion.vision=True
                print("La Lumiere S'allume...")
                Fonct.command("voir")
            
            

        elif self.propriete == True :

            self.propriete = False

            if type(self.position)==str:
                
                h.position.vision=False
                print("La Lumiere S'éteint")##pensé a éteindre quand quitte la piece si c'est lampe de poche de l'inventaire.
                Fonct.command("voir")
                
            else:
                
                self.postion.vision=True
                print("La Lumiere S'éteint...")
                Fonct.command("voir")


    
        

    

        

