####main/Interface - Free Novel

import os
import Fonct 


videur = False
godmode = False
   
Fonct.Start()##texte d'introduction + ce que voit le joueur en commençant

def God(godmode):
    
    godmode = not godmode
    
    if godmode == True:
        print ("GodMode On !")
    else:
        print ("GodMode Off...")

    
while videur is False:
    
    
        

    if godmode == False:
    
        cmd=input()
        cmd=cmd.strip()

        if cmd=="quit":
            fin=input("Voulez-vous quitter ? oui/non")

            if fin == ("oui"):    
                videur = True
                
        elif cmd=="GOD3615":
            God(godmode)

        else:    
            Fonct.command(cmd)

os.system("pause")
