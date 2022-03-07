#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:57:33 2022

@author: thomasstinglhamber
"""
from Energy import *

def Gauge(particule):
    """

    Parameters
    ----------
    particule : Nom de la particule.

    Returns
    -------
    Jauge : liste des points en fonction de chaque particule decouvertte.
    point : les points de la decouverte.

    """
    Jauge ={'Up_quark':	0,
                 'Up_antiquark' :	0,
                    'Down_quark':	0,
                    'Down_antiquark':	0,
                    'Strange_quark':	0,
                    'Strange_antiquark':	0,
                    'Pion': 200,
                    'Kaon': 200,
                    'Proton':	200,
                    'Neutron':200,
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
                    'Top_quark':	1000,              # pas encore sur a partir de la 
                    'Top_antiquark':	1000,
                    'Double_Bottom_Xi':	1000,
                    'Charmed_Bottom_Xi':	1000,
                    'Charmed_Bottom_Omega':	1000,
                    'Double_Charmed_Omega':	1000,
                    'Double_Bottom_Omega':	1000,
                    'Double_Charmed_Bottom_Omega':	1000,
                    'Charmed_Double_Bottom_Omega':1000,
                    'Charmed_B_Meson':1000}
    
    point=0
    for i in Jauge:
        #print(i)
        if i == particule:
            #print('ok')
            point =Jauge[i]
            break
        else : pass
    
    
    return Jauge, point


palier1=False

def checkpoint(): # permet d'update  les points et print
    file5=open('Point.txt', 'r')
    totalepoint =file5.read()
    print("Point total :" ,totalepoint,"MeV/c^2")
    file5.close()
    
    return totalepoint

def checkpoint_noprint():# permet d'update  les points mais ne print pas
    file5=open('Point.txt', 'r')
    totalepoint =file5.read()
    #print("Point total :" ,totalepoint,"MeV/c^2")
    file5.close()
    
    return totalepoint




