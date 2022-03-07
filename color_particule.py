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
                 'Up_antiquark' :	(0,255,0),
                    'Down_quark':	(0,0,255),
                    'Down_antiquark':	(25,40,0),
                    'Strange_quark':	(55,0,70),
                    'Strange_antiquark':	(255,0,160),
                    'Pion': (255,100,0),
                    'Kaon': (255,0,255),
                    'Proton':	(5,180,50),
                    'Neutron':(255,190,190),
                    'Phi_Meson':	(50,40,40),
                    'Lambda':	(255,0,0),
                    'Sigma':	(255,0,0),
                    'Delta':	(255,0,0),
                    'Charmed_quark':	(255,180,0),
                    'Charmed_antiquark':	(255,0,180),
                    'Xi':	(255,0,0),
                    'D_Meson':(255,0,0),
                    'Strange_D_Meson':(255,0,0),
                    'Charmed_Lambda':	(255,0,0),
                    'Charmed_Sigma':	(255,0,0),
                    'Charmed_Xi':	(255,0,0),
                    'Charmed_Omega':	(255,0,0),
                    'Charmed_Eta_Meson':	(255,0,0),
                    'Double_Charmed_Xi':	(255,0,0),
                    'Bottom_quark':	(255,0,0),
                    'Bottom_antiquark':	(255,0,0),
                    'B_Meson':	(255,0,0),
                    'Strange_B_Meson':(255,0,0),
                    'Bottom_Lambda':	(255,0,0),
                    'Bottom_Xi':	(255,0,0),
                    'Bottom_Sigma':	(255,0,0),
                    'Bottom_Omega':	(255,0,0),
                    'Upsilon_Meson':	(255,0,0),
                    'Top_quark':	(255,0,0),
                    'Top_antiquark':	(255,0,0),
                    'Double_Bottom_Xi':	(255,0,0),
                    'Charmed_Bottom_Xi':	(255,0,0),
                    'Charmed_Bottom_Omega':	(255,0,0),
                    'Double_Charmed_Omega':	(255,0,0),
                    'Double_Bottom_Omega':	(255,0,0),
                    'Double_Charmed_Bottom_Omega':	(255,0,0),
                    'Charmed_Double_Bottom_Omega':(255,0,0),
                    'Charmed_B_Meson':(255,0,0)}
    
    color=0
    for i in Col:
        #print(i)
        if i == particule:
            #print('ok')
            color =Col[i]
            break
        else : pass
    
    
    return color

