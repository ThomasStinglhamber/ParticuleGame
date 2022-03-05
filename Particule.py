#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:10:26 2022
@author: thomasstinglhamber
"""
import numpy as np
from ComptabilisationEnergy import *

puntos = checkpoint_noprint()
palier1,palier2,palier3 = Palier(puntos)


    

def Up_quark():
    name ='Up_quark'
    energy = 2.3 #MeV/c^2
    interaction = {'Up_quark'+'Down_quark': 'Proton',
                   'Down_quark'+'Up_quark': 'Proton',
                   
                   'Down_quark'+'Down_quark': 'Neutron',
                   
                   'Down_quark'+'Strange_quark': 'Lambda',
                   'Strange_quark'+'Down_quark': 'Lambda',
                   
                   'Down_quark'+'Charmed_quark': 'Charmed_Lambda',
                   'Charmed_quark'+'Down_quark': 'Charmed_Lambda',
                   
                   'Down_quark'+'Bottom_quark': 'Bottom_Lambda',
                   'Bottom_quark'+'Down_quark': 'Bottom_Lambda',
                   
                   'Up_quark'+'Strange_quark': 'Sigma',
                   'Strange_quark'+'Up_quark': 'Sigma',
                   
                   'Up_quark'+'Charmed_quark': 'Charmed_Sigma',
                   'Charmed_quark'+'Up_quark': 'Charmed_Sigma',
                   
                   'Up_quark'+'Bottom_quark': 'Bottom_Sigma',
                   'Bottom_quark'+'Up_quark': 'Bottom_Sigma',
                   
                   'Strange_quark'+'Strange_quark': 'Xi',
                   
                   'Strange_quark'+'Charmed_quark': 'Charmed_Xi',
                   'Charmed_quark'+'Strange_quark': 'Charmed_Xi',
                   
                   'Charmed_quark'+'Charmed_quark': 'Double_Charmed_Xi',
                   
                   'Strange_quark'+'Bottom_quark': 'Bottom_Xi',
                   'Bottom_quark'+'Strange_quark': 'Bottom_Xi',
                   
                   'Bottom_quark'+'Bottom_quark': 'Double_Bottom_Xi',
                   
                   'Charmed_quark'+'Bottom_quark': 'Charmed_Bottom_Xi',
                   'Bottom_quark'+'Charmed_quark': 'Charmed_Bottom_Xi',
                   
                   'Up_quark'+'Up_quark': 'Delta',
                   
                   'Down_antiquark' : 'Pion',
                   
                   'Strange_antiquark': 'Kaon',
                   
                   'Bottom_antiquark': 'B_Meson'}
    return name,energy,interaction

def Up_antiquark():
    name ='Up_antiquark'
    energy = 2.3
    interaction = {'Charmed_quark': 'D_Meson'}
    return name,energy,interaction


def Down_quark():
    name='Down_quark'
    energy = 4.8
    interaction = {'Up_quark'+'Up_quark' : 'Proton',
                   
                   'Up_quark'+'Down_quark' : 'Neutron',
                   'Down_quark'+'Up_quark' : 'Neutron',
                   
                   'Up_quark'+'Strange_quark': 'Lambda',
                   'Strange_quark'+'Up_quark': 'Lambda',
                   
                   'Up_quark'+'Charmed_quark': 'Charmed_Lambda',
                   'Charmed_quark'+'Up_quark': 'Charmed_Lambda',
                   
                   'Up_quark'+'Bottom_quark': 'Bottom_Lambda',
                   'Bottom_quark'+'Up_quark': 'Bottom_Lambda',
                   
                   'Strange_quark'+'Down_quark' : 'Sigma',
                   'Down_quark'+'Strange_quark' : 'Sigma',
                   
                   'Down_quark'+'Charmed_quark': 'Charmed_Sigma',
                   'Charmed_quark'+'Down_quark': 'Charmed_Sigma',
                   
                   'Down_quark'+'Bottom_quark': 'Bottom_Sigma',
                   'Bottom_quark'+'Down_quark': 'Bottom_Sigma',
                   
                   'Strange_quark'+'Strange_quark': 'Xi',
                   
                   'Strange_quark'+'Charmed_quark': 'Charmed_Xi',
                   'Charmed_quark'+'Strange_quark': 'Charmed_Xi',
                   
                   'Charmed_quark'+'Charmed_quark': 'Double_Charmed_Xi',
                   
                   'Strange_quark'+'Bottom_quark': 'Bottom_Xi',
                   'Bottom_quark'+'Strange_quark': 'Bottom_Xi',
                   
                   'Bottom_quark'+'Bottom_quark': 'Double_Bottom_Xi',
                   
                   'Charmed_quark'+'Bottom_quark': 'Charmed_Bottom_Xi',
                   'Bottom_quark'+'Charmed_quark': 'Charmed_Bottom_Xi',
                   
                   'Down_quark'+'Down_quark': 'Delta',
                   
                   'Strange_antiquark': 'Kaon',
                   
                   'Bottom_antiquark': 'B_Meson'}
    return name,energy,interaction

def Down_antiquark():
    name ='Down_antiquark'
    energy = 4.8
    interaction = {'Up_quark': 'Pion',
                   'Charmed_quark': 'D_Meson'}
    return name,energy,interaction


def Strange_quark():
    name='Strange_quark'
    energy = 95
    interaction = {'Up_quark'+'Down_quark' :'Lambda',
                   'Down_quark'+'Up_quark' :'Lambda',
                   
                   'Up_quark'+'Up_quark' :'Sigma',
                   'Down_quark'+'Down_quark' :'Sigma',
                   
                   'Up_quark'+'Strange_quark' :'Xi',
                   'Strange_quark'+'Up_quark' :'Xi',
                   
                   'Down_quark'+'Strange_quark' :'Xi',
                   'Strange_quark'+'Down_quark' :'Xi',
                   
                   'Up_quark'+'Charmed_quark': 'Charmed_Xi',
                   'Charmed_quark'+'Up_quark': 'Charmed_Xi',
                   
                   'Down_quark'+'Charmed_quark': 'Charmed_Xi',
                   'Charmed_quark'+'Down_quark': 'Charmed_Xi',
                   
                   'Up_quark'+'Bottom_quark': 'Bottom_Xi',
                   'Bottom_quark'+'Up_quark': 'Bottom_Xi',
                   
                   'Down_quark'+'Bottom_quark': 'Bottom_Xi',
                   'Bottom_quark'+'Down_quark': 'Bottom_Xi',
                   
                   'Charmed_quark'+'Strange_quark': 'Charmed_Omega',
                   'Strange_quark'+'Charmed_quark': 'Charmed_Omega',
                   
                   'Bottom_quark'+'Strange_quark': 'Bottom_Omega',
                   'Strange_quark'+'Bottom_quark': 'Bottom_Omega',
                   
                   'Charmed_quark'+'Charmed_quark': 'Double_Charmed_Omega',
                   
                   'Bottom_quark'+'Charmed_quark': 'Charmed_Bottom_Omega',
                   'Charmed_quark'+'Bottom_quark': 'Charmed_Bottom_Omega',
                   
                   'Bottom_quark'+'Bottom_quark': 'Double_Bottom_Omega',
                   
                   'Strange_antiquark' :'Phi_Meson',
                   
                   'Bottom_antiquark': 'Strange_B_Meson'}
    return name,energy,interaction

def Strange_antiquark():
    name ='Strange_antiquark'
    energy = 95
    interaction = {'Strange_quark' :'Phi_Meson',
                   
                   'Up_quark': 'Kaon',
                   'Down_quark': 'Kaon',
                   
                   'Charmed_quark': 'Strange_D_Meson'}
    return name,energy,interaction


if palier2==True:
    def Charmed_quark():
        name='Charmed_quark'
        energy = 1275
        interaction = {'Up_quark'+'Down_quark' :'Charmed_Lambda',
                       'Down_quark'+'Up_quark' :'Charmed_Lambda',
                       
                       'Up_quark'+'Up_quark' :'Charmed_Sigma',
                       'Down_quark'+'Down_quark' :'Charmed_Sigma',
                       
                       'Up_quark'+'Strange_quark': 'Charmed_Xi',
                       'Strange_quark'+'Up_quark': 'Charmed_Xi',
                       
                       'Down_quark'+'Strange_quark': 'Charmed_Xi',
                       'Strange_quark'+'Down_quark': 'Charmed_Xi',
                       
                       'Up_quark'+'Charmed_quark': 'Double_Charmed_Xi',
                       'Charmed_quark'+'Up_quark': 'Double_Charmed_Xi',
                       
                       'Down_quark'+'Charmed_quark': 'Double_Charmed_Xi',
                       'Charmed_quark'+'Down_quark': 'Double_Charmed_Xi',
                       
                       'Up_quark'+'Bottom_quark': 'Charmed_Bottom_Xi',
                       'Bottom_quark'+'Up_quark': 'Charmed_Bottom_Xi',
                       
                       'Down_quark'+'Bottom_quark': 'Charmed_Bottom_Xi',
                       'Bottom_quark'+'Down_quark': 'Charmed_Bottom_Xi',
                       
                       'Strange_quark'+'Strange_quark': 'Charmed_Omega',
                       
                       'Strange_quark'+'Charmed_quark': 'Double_Charmed_Omega',
                       'Charmed_quark'+'Strange_quark': 'Double_Charmed_Omega',
                       
                       'Strange_quark'+'Bottom_quark': 'Charmed_Bottom_Omega',
                       'Bottom_quark'+'Strange_quark': 'Charmed_Bottom_Omega',
                       
                       'Bottom_quark'+'Charmed_quark': 'Double_Charmed_Bottom_Omega',
                       'Charmed_quark'+'Bottom_quark': 'Double_Charmed_Bottom_Omega',
                       
                       'Bottom_quark'+'Bottom_quark': 'Charmed_Double_Bottom_Omega',
                       
                       'Charmed_antiquark':'Charmed_Eta_Meson',
                       
                       'Down_antiquark': 'D_Meson',
                       'Up_antiquark': 'D_Meson',
                       
                       'Strange_antiquark': 'Strange_D_Meson',
                       
                       'Bottom_antiquark': 'Charmed_B_Meson'}
        return name,energy,interaction
    
    def Charmed_antiquark():
        name ='Charmed_antiquark'
        energy = 1275
        interaction = {'Charmed_quark':'Charmed_Eta_Meson'}
        return name,energy,interaction
    
    
    print('Vous avez débloqué le palier 2')
        
if palier3==True:
    def Bottom_quark():
        name ='Bottom_quark'
        energy = 4180
        interaction={'Up_quark'+'Down_quark' : 'Bottom_Lambda',
                     'Down_quark'+'Up_quark' : 'Bottom_Lambda',
                     
                     'Up_quark'+'Up_quark' : 'Bottom_Sigma',
                     'Down_quark'+'Down_quark' : 'Bottom_Sigma',
                     
                     'Up_quark'+'Strange_quark': 'Bottom_Xi',
                     'Strange_quark'+'Up_quark': 'Bottom_Xi',
                     
                     'Down_quark'+'Strange_quark': 'Bottom_Xi',
                     'Strange_quark'+'Down_quark': 'Bottom_Xi',
                     
                     'Down_quark'+'Bottom_quark': 'Double_Bottom_Xi',
                     'Bottom_quark'+'Down_quark': 'Double_Bottom_Xi',
                     
                     'Up_quark'+'Bottom_quark': 'Double_Bottom_Xi',
                     'Bottom_quark'+'Up_quark': 'Double_Bottom_Xi',
                     
                     'Up_quark'+'Charmed_quark': 'Charmed_Bottom_Xi',
                     'Charmed_quark'+'Up_quark': 'Charmed_Bottom_Xi',
                     
                     'Down_quark'+'Charmed_quark': 'Charmed_Bottom_Xi',
                     'Charmed_quark'+'Down_quark': 'Charmed_Bottom_Xi',
                     
                     'Strange_quark'+'Strange_quark': 'Bottom_Omega',
                     
                     'Strange_quark'+'Charmed_quark': 'Charmed_Bottom_Omega',
                     'Charmed_quark'+'Strange_quark': 'Charmed_Bottom_Omega',
                     
                     'Strange_quark'+'Bottom_quark': 'Double_Bottom_Omega',
                     'Bottom_quark'+'Strange_quark': 'Double_Bottom_Omega',
                     
                     'Charmed_quark'+'Charmed_quark': 'Double_Charmed_Bottom_Omega',
                     
                     'Charmed_quark'+'Bottom_quark': 'Charmed_Double_Bottom_Omega',
                     'Bottom_quark'+'Charmed_quark': 'Charmed_Double_Bottom_Omega',
                     
                     'Bottom_antiquark' : 'Upsilon_Meson'}
        return name,energy,interaction
    
    def Bottom_antiquark():
        name ='Bottom_antiquark'
        energy = 4180
        interaction = {'Bottom_quark' : 'Upsilon_Meson',
                       
                       'Up_quark': 'B_Meson',
                       'Down_quark': 'B_Meson',
                       
                       'Strange_quark': 'Strange_B_Meson',
                       
                       'Charmed_quark': 'Charmed_B_Meson'}
        return name,energy,interaction
    print('Vous avez débloqué le palier 3')

def Top_quark():
    name ='Top_quark'
    energy = 173210
    interaction={}
    return name,energy,interaction


def Top_antiquark():
    name ='Top_antiquark'
    energy = 173210
    interaction={}
    return name,energy,interaction

#-------------------------------------------------
def Pion():
    name ='Pion'
    energy = 139.50
    interaction={}
    return name,energy,interaction

def Kaon():
    name ='Kaon'
    energy = 493.66
    interaction={}
    return name,energy,interaction

def Proton():
    name ='Proton'
    energy = 938.20
    interaction={}
    return name,energy,interaction

def Neutron():
    name ='Neutron'
    energy = 939.50
    interaction={}
    return name,energy,interaction

def Phi_Meson():
    name ='Phi_Meson'
    energy = 1019.40
    interaction={}
    return name,energy,interaction

def Lambda():
    name ='Lambda'
    energy = 1115.60
    interaction={}
    return name,energy,interaction

def Sigma():
    name ='Sigma'
    energy = 1189.30
    interaction={}
    return name,energy,interaction

def Delta():
    name ='Delta'
    energy = 1232.00
    interaction={}
    return name,energy,interaction

def Xi():
    name ='Xi'
    energy = 1314.80
    interaction={}
    return name,energy,interaction

def D_Meson():
    name ='D_Meson'
    energy = 2010.26
    interaction={}
    return name,energy,interaction

def Strange_D_Meson():
    name ='Strange_D_Meson'
    energy = 2112.10
    interaction={}
    return name,energy,interaction

def Charmed_Lambda():
    name ='Charmed_Lambda'
    energy = 2286.40
    interaction={}
    return name,energy,interaction

def Charmed_Sigma():
    name ='Charmed_Sigma'
    energy = 2453,90
    interaction={}
    return name,energy,interaction

def Charmed_Xi():
    name ='Charmed_Xi'
    energy = 2467.40
    interaction={}
    return name,energy,interaction

def Charmed_Omega():
    name ='Charmed_Omega'
    energy = 2695.20
    interaction={}
    return name,energy,interaction

def Charmed_Eta_Meson():
    name ='Charmed_Eta_Meson'
    energy = 2983.60
    interaction={}
    return name,energy,interaction

def Double_Charmed_Xi():
    name ='Double_Charmed_Xi'
    energy = 3621.20
    interaction={}
    return name,energy,interaction

def B_Meson():
    name ='B_Meson'
    energy = 5325.20
    interaction={}
    return name,energy,interaction

def Strange_B_Meson():
    name ='Strange_B_Meson'
    energy = 5415.40
    interaction={}
    return name,energy,interaction

def Bottom_Lambda():
    name ='Bottom_Lambda'
    energy = 5619.60
    interaction={}
    return name,energy,interaction

def Bottom_Xi():
    name ='Bottom_Xi'
    energy = 5791.90
    interaction={}
    return name,energy,interaction

def Bottom_Sigma():
    name ='Bottom_Sigma'
    energy = 5810.50
    interaction={}
    return name,energy,interaction

def Bottom_Omega():
    name ='Bottom_Omega'
    energy = 6046.10
    interaction={}
    return name,energy,interaction

def Upsilon_Meson():
    name ='Upsilon_Meson'
    energy = 9460.30
    interaction={}
    return name,energy,interaction












































