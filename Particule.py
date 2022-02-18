#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:10:26 2022
@author: thomasstinglhamber
"""
import numpy as np



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


def Top_quark():
    name ='Top_quark'
    energy = 173210
    interaction={}
    return name,energy,interaction


# ANTI QUARKS --------------------------------------------------

def Up_antiquark():
    name ='Up_antiquark'
    energy = 2.3
    interaction = {'Charmed_quark': 'D_Meson'}
    return name,energy,interaction


def Down_antiquark():
    name ='Down_antiquark'
    energy = 4.8
    interaction = {'Up_quark': 'Pion',
                   'Charmed_quark': 'D_Meson'}
    return name,energy,interaction


def Strange_antiquark():
    name ='Strange_antiquark'
    energy = 95
    interaction = {'Strange_quark' :'Phi_Meson',
                   
                   'Up_quark': 'Kaon',
                   'Down_quark': 'Kaon',
                   
                   'Charmed_quark': 'Strange_D_Meson'}
    return name,energy,interaction

def Charmed_antiquark():
    name ='Charmed_antiquark'
    energy = 1275
    interaction = {'Charmed_quark':'Charmed_Eta_Meson'}
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

def Top_antiquark():
    name ='Top_antiquark'
    energy = 173210
    interaction={}
    return name,energy,interaction

