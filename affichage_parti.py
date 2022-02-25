#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:33:47 2022

@author: thomasstinglhamber
"""
def affichage_particule(particule):
    """

    Parameters
    ----------
    particule : Nom de la particule.

    Returns
    -------
    Jauge : liste des points en fonction de chaque particule decouvertte.
    point : les points de la decouverte.

    """
    Aff ={'Up_quark':	0,
                 'Up_antiquark' :	1,
                    'Down_quark':	2,
                    'Down_antiquark':	3,
                    'Strange_quark':	4,
                    'Strange_antiquark':	5,
                    'Pion': 6,
                    'Kaon': 7,
                    'Proton':	8,
                    'Neutron':9,
                    'Phi_Meson':	10,
                    'Lambda':	11,
                    'Sigma':	12,
                    'Delta':	13,
                    'Charmed_quark':	14,
                    'Charmed_antiquark':	15,
                    'Xi':	16,
                    'D_Meson':17,
                    'Strange_D_Meson':18,
                    'Charmed_Lambda':	19,
                    'Charmed_Sigma':	20,
                    'Charmed_Xi':	21,
                    'Charmed_Omega':	22,
                    'Charmed_Eta_Meson':	23,
                    'Double_Charmed_Xi':	24,
                    'Bottom_quark':	25,
                    'Bottom_antiquark':	26,
                    'B_Meson':	27,
                    'Strange_B_Meson':28,
                    'Bottom_Lambda':	29,
                    'Bottom_Xi':	30,
                    'Bottom_Sigma':	31,
                    'Bottom_Omega':	32,
                    'Upsilon_Meson':	33,
                    'Top_quark':	34,
                    'Top_antiquark':	35,
                    'Double_Bottom_Xi':	36,
                    'Charmed_Bottom_Xi':	37,
                    'Charmed_Bottom_Omega':	38,
                    'Double_Charmed_Omega':	39,
                    'Double_Bottom_Omega':	40,
                    'Double_Charmed_Bottom_Omega':	41,
                    'Charmed_Double_Bottom_Omega':43,
                    'Charmed_B_Meson':43}
    
    chiffre=0
    for i in Aff:
        #print(i)
        if i == particule:
            #print('ok')
            chiffre =Aff[i]
            break
        else : pass
    
    
    return chiffre


# =============================================================================
# file4 = open('ListeParticule.txt', 'r')
# parti=file4.read().splitlines()
# file4.close()
# 
# print(parti)
# for i in parti:
#     chif=affichage_particule(i)
#     print(chif)
# =============================================================================
