#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:57:33 2022

@author: thomasstinglhamber
"""
from Energy import *

def Gauge(particule):
    Jauge ={'Up_quark':	0,
                 'Up_antiquark' :	0,
                    'Down_quark':	0,
                    'Down_antiquark':	0,
                    'Strange_quark':	0,
                    'Strange_antiquark':	0,
                    'Pion': 200,
                    'Kaon': 200,
                    'Proton':	200,
                    'Neutron	':200,
                    'Phi_Meson':	200,
                    'Lambda':	200,
                    'Sigma':	200,
                    'Delta':	200,
                    'Charmed_quark':	50,
                    'Charmed_antiquark':	50,
                    'Xi':	400,
                    'D_Meson':400,
                    'Strange_D_Meson':400,
                    'Charmed_Lambda':	400,
                    'Charmed_Sigma':	400,
                    'Charmed_Xi':	400,
                    'Charmed_Omega':	400,
                    'Charmed_Eta_Meson':	400,
                    'Double_Charmed_Xi':	400,
                    'Bottom_quark':	200,
                    'Bottom_antiquark':	200,
                    'B_Meson':	700,
                    'Strange_B_Meson':700,
                    'Bottom_Lambda':	700,
                    'Bottom_Xi':	700,
                    'Bottom_Sigma':	700,
                    'Bottom_Omega':	700,
                    'Upsilon_Meson':	700,
                    'Top_quark':	173210.00,
                    'Top_antiquark':	173210.00,
                    'Double_Bottom_Xi':	'Unknown',
                    'Charmed_Bottom_Xi':	'Unknown',
                    'Charmed_Bottom_Omega':	'Unknown',
                    'Double_Charmed_Omega':	'Unknown',
                    'Double_Bottom_Omega':	'Unknown',
                    'Double_Charmed_Bottom_Omega':	'Unknown',
                    'Charmed_Double_Bottom_Omega':'Unknown',
                    'Charmed_B_Meson':'Unknown'}
    
    point=0
    for i in Jauge:
        #print(i)
        if i == particule:
            #print('ok')
            point =Jauge[i]
            break
        else : pass
    
    
    return Jauge, point

# =============================================================================
#     1er pallier, on a de base 100 Mev et on doit avoir 1300 MeV pour pouvoir debloquer
#     le quark et antiquark charmed. On a 8 reaction mais on peut dire que si on en trouve
#     6 alors on debloque charmed. chaque decouverte donne donc 200MeV a notre jauge.
#     Une fois les 1300 MeV, on debloque charmed, on a donc acces a des reactions supplementaire.
#     
#     2eme pallier, dee 1300 a 4200 pour debloque le quark et antiquark botttom. Il y a 9 reaction donc 
#     on va dire que si  on en trouve 7 c est bon --> plusoum 415 MeV par decouverte.
#     
#     3eme pallier --> mega free il reste 7 reaction jusque quark top mais on l utilise nulle part
#     donc jusqu a la fin il reste 15 reaction.
#     
#     4eme pallier --> il y a des particule on connait par  leur masse donc on peut
#     dire que a partir du pallier 3 chaque decouverte donne x MeV.
# =============================================================================
    

# =============================================================================
#     TO DO :
#         - faire le systeme de pallier en faisant en sorte que les quarks qu on a pas
#         debloqué n apparaissent pas ou  alors ne peut  pas etre utilisé.
#         - mettre les step pour chaque decouverte ( dico surement)
# =============================================================================
        

# =============================================================================
#     creer un .txt avec la jauge d energie qu on a, a chaque decouverte, on ecrit l energie en plus
#     et au sauvegarde 
# =============================================================================
        
    return 
