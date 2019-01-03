# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:58:58 2018

@author: Dominic
"""

import numpy as np
np.set_printoptions(threshold=np.nan)

# Parametres du probleme
L_Plancher = 3.0
L_Clou = L_Plancher/2

# *** Estimation initiale (Tous les clous sont horizontaux) ***
def clou_aleatoire():
    pc = np.random.uniform (0,L_Plancher) #position du clou
    #Vecteur de direction
    directionX = np.random.uniform (-1,1)
    directionY = np.random.uniform(-1,1)
    angle = 0
    if directionY == 0:
        return angle == 1
    else:
        return angle == np.arctan(directionY/directionX)
    
    d_positif = pc+(L_Clou/2*np.cos(angle))
    d_negatif = pc-(L_Clou/2*np.cos(angle))
    #Determine si le clou touche une craque
    if d_positif >= L_Plancher:
        return True
    elif d_negatif <= 0:
        return True
    else:
        return False

nb_clou = 100
resultat = np.zeros(nb_clou)
# Produit l'experience 
for i in range(nb_clou):
    resultat[i]=clou_aleatoire()

hit = list(resultat).count(1)
# Estimation initiale de Pi
pi_estime = nb_clou/hit
print(pi_estime)



                                        