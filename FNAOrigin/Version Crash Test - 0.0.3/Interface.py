####main/Interface - Free Novel

import os
import Fonct 


videur = False
godmode = False
   
##texte d'introduction + ce que voit le joueur en commençant



def God(godmode):
    
    godmode = not godmode
    
    if godmode == True:
        print ("Your the RealGod!")
    return godmode

def Moteur(godmode,videur):
        
    while videur is False and godmode is False:
        
        
            cmd=input()
            cmd=cmd.strip()

            if cmd=="quit":
                fin=input("Voulez-vous quitter ? oui/non")

                if fin == ("oui"):    
                    videur = True
                    
            elif cmd=="GOD3615":
                godmode=God(godmode)
                return godmode

            else:    
                Fonct.command(cmd)
                
Moteur(godmode,videur)
os.system("pause")
