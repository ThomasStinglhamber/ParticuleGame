#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:20:41 2022

@author: thomasstinglhamber
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:33:47 2022

@author: thomasstinglhamber
"""
def color_parti(particule):
    """

    Parameters
    ----------
    particule : Nom de la particule.

    Returns
    -------
    Jauge : liste des points en fonction de chaque particule decouvertte.
    point : les points de la decouverte.

    """
    Col ={'Up_quark':	(255,0,0),
                 'Up_antiquark' :	(0,255,255),
                    'Down_quark':	(0,0,255),
                    'Down_antiquark':	(255,255,0),
                    'Strange_quark':	(0,255,0),
                    'Strange_antiquark':	(255,0,255),
                    'Pion': (84,85,248),
                    'Kaon': (84,248,184),
                    'Proton':	(119,119,59),
                    'Neutron':(81,81,81),
                    'Phi_Meson':	(10,119,111),
                    'Lambda':	(96,9,96),
                    'Sigma':	(38,21,102),
                    'Delta':	(102,21,21),
                    'Charmed_quark':	(101,0,255),
                    'Charmed_antiquark':	(154,255,0),
                    'Xi':	(0,0,0),
                    'D_Meson':(255,0,242),
                    'Strange_D_Meson':(0,50,255),
                    'Charmed_Lambda':	(149,255,0),
                    'Charmed_Sigma':	(255,155,0),
                    'Charmed_Xi':	(4,7,122),
                    'Charmed_Omega':	(122,4,4),
                    'Charmed_Eta_Meson':	(255,108,0),
                    'Double_Charmed_Xi':	(70,98,21),
                    'Bottom_quark':	(255,126,126),
                    'Bottom_antiquark':	(0,129,129),
                    'B_Meson':	(65,17,123),
                    'Strange_B_Meson':(110,120,110),
                    'Bottom_Lambda':	(73,185,255),
                    'Bottom_Xi':	(202,202,202),
                    'Bottom_Sigma':	(178,0,0),
                    'Bottom_Omega':	(112,60,30),
                    'Upsilon_Meson':	(128,163,210),
                    'Top_quark':	(142,128,210),
                    'Top_antiquark':	(113,127,45),
                    'Double_Bottom_Xi':	(122,84,26),
                    'Charmed_Bottom_Xi':	(219,255,0),
                    'Charmed_Bottom_Omega':	(12,62,11),
                    'Double_Charmed_Omega':	(239,186,144),
                    'Double_Bottom_Omega':	(82,69,59),
                    'Double_Charmed_Bottom_Omega':	(255,232,215),
                    'Charmed_Double_Bottom_Omega':(255,255,255),
                    'Charmed_B_Meson':(255,255,255)}
    
    color=0
    for i in Col:
        #print(i)
        if i == particule:
            #print('ok')
            color =Col[i]
            break
        else : pass
    
    
    return color

