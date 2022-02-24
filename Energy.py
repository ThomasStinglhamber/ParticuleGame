#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:15:25 2022

@author: thomasstinglhamber
"""
from Particule import *

def Energy(item):
    #test=particule
    listenergy ={'Up_quark':	2.30,
                 'Up_antiquark' :	2.30,
                    'Down_quark':	4.80,
                    'Down_antiquark':	4.80,
                    'Strange_quark':	9500,
                    'Strange_antiquark':	95.00,
                    'Pion': 139.50,
                    'Kaon': 493.66,
                    'Proton':	938.20,
                    'Neutron	':939.50,
                    'Phi_Meson':	1019.40,
                    'Lambda':	1115.60,
                    'Sigma':	1189.30,
                    'Delta':	1232.00,
                    'Charmed_quark':	1275.00,
                    'Charmed_antiquark':	1275.00,
                    'Xi':	1314.80,
                    'D_Meson':2010.26,
                    'Strange_D_Meson':2112.10,
                    'Charmed_Lambda':	2286.40,
                    'Charmed_Sigma':	2453.90,
                    'Charmed_Xi':	2467.40,
                    'Charmed_Omega':	2695.20,
                    'Charmed_Eta_Meson':	2983.60,
                    'Double_Charmed_Xi':	3621.20,
                    'Bottom_quark':	4180.00,
                    'Bottom_antiquark':	4180.00,
                    'B_Meson':	5325.20,
                    'Strange_B_Meson':5415.40,
                    'Bottom_Lambda':	5619.60,
                    'Bottom_Xi':	5791.90,
                    'Bottom_Sigma':	5810.50,
                    'Bottom_Omega':	6046.10,
                    'Upsilon_Meson':	9460.30,
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

    ener=0
    for i in listenergy:
        #print(i)
        if i == item:
            #print('ok')
            ener =listenergy[i]
            break
        else : pass


    return listenergy, ener
