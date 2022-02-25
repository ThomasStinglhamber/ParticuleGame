#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:19:23 2022

@author: thomasstinglhamber
"""
from Collision import *

def conversionn(particule):
    """

    Parameters
    ----------
    particule : Nom de la particule.

    Returns
    -------
    Jauge : liste des points en fonction de chaque particule decouvertte.
    point : les points de la decouverte.

    """
    conv ={'Up_quark':Up_quark,
                 'Up_antiquark' :	Up_antiquark,
                    'Down_quark':	Down_quark,
                    'Down_antiquark':	Down_antiquark,
                    'Strange_quark':	Strange_quark,
                    'Strange_antiquark':	Strange_antiquark,
                    'Pion': 'Pion',
                    'Kaon': 'Kaon',
                    'Proton':	'Proton',
                    'Neutron':'Neutron',
                    'Phi_Meson':	'Phi_Meson',
                    'Lambda':	'Lambda',
                    'Sigma':	'Sigma',
                    'Delta':	'Delta',
                    'Charmed_quark':	Charmed_quark,
                    'Charmed_antiquark':	Charmed_antiquark,
                    'Xi':	'Xi',
                    'D_Meson':'D_Meson',
                    'Strange_D_Meson':'Strange_D_Meson',
                    'Charmed_Lambda':	'Charmed_Lambda',
                    'Charmed_Sigma':	'Charmed_Sigma',
                    'Charmed_Xi':	'Charmed_Xi',
                    'Charmed_Omega':	'Charmed_Omega',
                    'Charmed_Eta_Meson':	'Charmed_Eta_Meson',
                    'Double_Charmed_Xi':	'Double_Charmed_Xi',
                    'Bottom_quark':	Bottom_quark,
                    'Bottom_antiquark':	Bottom_antiquark,
                    'B_Meson':	'B_Meson',
                    'Strange_B_Meson':'Strange_B_Meson',
                    'Bottom_Lambda':	'Bottom_Lambda',
                    'Bottom_Xi':	'Bottom_Xi',
                    'Bottom_Sigma':	'Bottom_Sigma',
                    'Bottom_Omega':	'Bottom_Omega',
                    'Upsilon_Meson':	'Upsilon_Meson',
                    'Top_quark':	Top_quark,              # pas encore sur a partir de la 
                    'Top_antiquark':	Top_antiquark,
                    'Double_Bottom_Xi':	'Double_Bottom_Xi',
                    'Charmed_Bottom_Xi':	'Charmed_Bottom_Xi',
                    'Charmed_Bottom_Omega':	'Charmed_Bottom_Omega',
                    'Double_Charmed_Omega':	'Double_Charmed_Omega',
                    'Double_Bottom_Omega':	'Double_Bottom_Omega',
                    'Double_Charmed_Bottom_Omega':	'Double_Charmed_Bottom_Omega',
                    'Charmed_Double_Bottom_Omega':'Charmed_Double_Bottom_Omega',
                    'Charmed_B_Meson':'Charmed_B_Meson'}
    
    vrainame=0
    for i in conv:
        #print(i)
        if i == particule:
            #print('ok')
            vrainame =conv[i]
            break
        else : pass
    
    
    return vrainame

