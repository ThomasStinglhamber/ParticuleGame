#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:20:41 2022

@author: thomasstinglhamber
"""
def name_parti(particule):
    """

    Parameters
    ----------
    particule : Nom de la particule.

    Returns
    -------
    Jauge : liste des points en fonction de chaque particule decouvertte.
    point : les points de la decouverte.

    """
    Col ={0:'Up_quark',
                 1:'Up_antiquark',
                  2:  'Down_quark',
                   3: 'Down_antiquark',
                   4: 'Strange_quark',
                   5: 'Strange_antiquark',
                   6: 'Pion',
                    7:'Kaon',
                   8: 'Proton',
                   9: 'Neutron',
                   10: 'Phi_Meson',
                   11: 'Lambda',
                   12: 'Sigma',
                   13: 'Delta',
                   14: 'Charmed_quark',
                   15: 'Charmed_antiquark',
                   16: 'Xi',
                   17: 'D_Meson',
                    18:'Strange_D_Meson',
                   19: 'Charmed_Lambda',
                   20: 'Charmed_Sigma',
                   21: 'Charmed_Xi',
                   22: 'Charmed_Omega',
                   23: 'Charmed_Eta_Meson',
                   24: 'Double_Charmed_Xi',
                   25: 'Bottom_quark',
                   26: 'Bottom_antiquark',
                   27: 'B_Meson',
                   28: 'Strange_B_Meson',
                   29: 'Bottom_Lambda',
                   30: 'Bottom_Xi',
                   31: 'Bottom_Sigma',
                   32: 'Bottom_Omega',
                   33: 'Upsilon_Meson',
                   34: 'Top_quark',
                   35: 'Top_antiquark',
                   36: 'Double_Bottom_Xi',
                   37: 'Charmed_Bottom_Xi',
                    38:'Charmed_Bottom_Omega',
                   39: 'Double_Charmed_Omega',
                   40: 'Double_Bottom_Omega',
                   41: 'Double_Charmed_Bottom_Omega',
                   42: 'Charmed_Double_Bottom_Omega',
                   43: 'Charmed_B_Meson'}
    
    name=0
    for i in Col:
        #print(i)
        if i == particule:
            #print('ok')
            name =Col[i]
            break
        else : pass
    
    
    return name


