###fonction
import os
import levelManage as LM
import BibliOBJ as OBJ

    
    
def Inventaire():

    videur_inv=False

    while videur_inv == False:

        e=input()

        e=e.strip()
        e=e.split(" ")
    
        try:

            if e[0]==("utiliser"):###fonction utiliser

                del e[0]
            
                for i in lvl.objet:
                
                    b=(i.nom).split(" ")
                    
                    if b==e and i.position==("inventaire"):
                        
                        videur_inv=True
                        lvl.hero.utiliser(i)
                
            elif e[0]==("poser"):###fonction poser

                del e[0]
            
                for i in lvl.objet:
                
                    b=(i.nom).split(" ")
                    
                    if b==e and i.position==("inventaire"):
                        
                        videur_inv=True
                        lvl.hero.poser(i)
                        
            elif e[0]==("retour"):
                
                print("vous fermez votre sac")
                videur_inv=True
        

        except IndexError:
            print("...")


def command(cmd):
    
    cmd=cmd.strip()

    cmd=cmd.split(" ")
    b=0
    try:
        
        for i in cmd:###utiliser un len(cmd) à la place de b...
                b+=1
        if b <= 1 and cmd[0] ==("voir"):              #fonction voir.


            if lvl.hero.position.vision==True:               #voir l'ensemble de l'environnement...si possible     
                print("Vous etes dans ",lvl.hero.position.nom,".\n",lvl.hero.position.description,"\n")
                lvl.hero.voir(lvl.objet)

            elif lvl.hero.position.vision ==False:
                print("Vous ne voyez rien, il fait noir...")


        elif b <= 1 and cmd[0] ==("inventaire"):###voir inventaire de maniere plus direct peut étre retirer le voir+inventaire?
            print("Vous ouvrez votre sac...")
            lvl.hero.voirinv(lvl.objet)
            Inventaire()



        elif cmd[0]==("utiliser"):                ###fonction utiliser
            del cmd[0]

           #utiliser objet scéne
            
            for i in lvl.objet:
                
                b=(i.nom).split(" ")  
                if b==cmd:
                    lvl.hero.utiliser(i)



        elif b>1 and cmd[0]==("prendre"):
            del cmd[0]

            it=0

            for i in lvl.objet:
                c=(i.nom).split(" ")
                if c==cmd:
                    lvl.hero.prendre(i)


                        
        else:            #complement utilisation objet(ex : utilisation des clef en 2 temps) ///changer cela ?
        
            for i in lvl.objet:
                b=(i.nom).split(" ")

                if b==cmd:
                    return i

    except IndexError:
        print("...")



def Start():
    
    #lvl.text.intro
    input("appuyer sur une touche pour commencer l'aventure")
    command("voir")

def Menu():
    videur = False

    while videur==False:
        
        choix=input("Bienvenu dans le Test Free Novel Adventure /n/n Voulez vous tester ou créer?")

        if choix == ("tester"):
            print("cool!!!")
            nvL=LM.listing()
            videur = True
            return nvL
            
        elif choix == ("créer"):
            print ("desole pas encore...")
            videur = False
            
        else:
            print ("Pardon ??!")
            videur = False
def Ia():
    while True:
        command("voir")
        for i in lvl.objet:
            if hasattr(i,"pos_b"):
                if i.position==lvl.hero.position or i.pos_b == lvl.hero.position:
                    command("utiliser "+i.nom)
                    os.system("pause")
                    
                
lvl=Menu()
Start()
