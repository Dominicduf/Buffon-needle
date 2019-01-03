# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:58:58 2018

@author: Dominic
"""

import numpy as np
np.set_printoptions(threshold=np.nan)

L_Plancher = 3.0
L_Clou = L_Plancher/2



def clou_aleatoire():
    pc = np.random.uniform (0,L_Plancher)
    angle = np.random.uniform (0,np.pi/2)
    d_positif = pc+(L_Clou/2*np.cos(angle))
    d_negatif = pc-(L_Clou/2*np.cos(angle))

    if d_positif >= L_Plancher:
        return True
    elif d_negatif <= 0:
        return True
    else:
        return False

nb_clou = 10000
resultat = np.zeros(nb_clou)

for i in range(nb_clou):
    resultat[i]=clou_aleatoire()

print (resultat)

hit = list(resultat).count(1)
no_hit =list(resultat).count(0)

pi_estime = nb_clou/hit
print (pi_estime)                                                                                                                                                                                                                          