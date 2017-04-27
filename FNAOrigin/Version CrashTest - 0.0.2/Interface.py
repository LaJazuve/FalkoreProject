####main/Interface - Free Novel

import os
import Fonct 


videur = False

   
Fonct.Start()##texte d'introduction + ce que voit le joueur en commençant


while videur is False:
    
    cmd=input()
    cmd=cmd.strip()

    if cmd=="quit":
        fin=input("Voulez-vous quitter ? oui/non")

        if fin == ("oui"):    
            videur = True
        
    else:    
        Fonct.command(cmd)

os.system("pause")
