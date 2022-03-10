#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:10:00 2022

@author: thomasstinglhamber
"""

def Palier1(totalepoint):
    file1 = open('ListeParticule.txt', 'r')
    data1 = file1.read().splitlines()
    if 'Charmed_quark'and 'Charmed_antiquark' not in data1 and int(totalepoint) >= 1300:
        file2 = open('ListeParticule.txt', 'a')
        file2.write('Charmed_quark'+ "\n")
        file2.write('Charmed_antiquark'+ "\n")
        file2.close()
        print('Palier 1 Débloqué --> Nouvelle particule disponible !')
    if int(totalepoint) <= 1300:
        pass
        #print('pas assez denergie')
    if 'Charmed_quark'and 'Charmed_antiquark'  in data1 and int(totalepoint) >= 1300:
        pass
    else : pass

    file1.close()

def Palier2(totalepoint):
    file1 = open('ListeParticule.txt', 'r')
    data1 = file1.read().splitlines()
    if 'Bottom_quark'and 'Bottom_antiquark' not in data1 and totalepoint >= str(4200):
        
        file2 = open('ListeParticule.txt', 'a')
        file2.write('Bottom_quark'+ "\n")
        file2.write('Bottom_antiquark'+ "\n")
        file2.close()
        print('Palier 2 Débloqué --> Nouvelle particule disponible !')
    if totalepoint <= str(4200):
        pass
        #print('pas assez denergie')
    if 'Bottom_quark'and 'Bottom_antiquark'  in data1 and totalepoint >= str(4200):
        pass
    else : pass

    file1.close()
    
def Palier3(totalepoint):
    file1 = open('ListeParticule.txt', 'r')
    data1 = file1.read().splitlines()
    if 'Top_quark'and 'Top_antiquark' not in data1 and totalepoint >= str(10000):
        
        file2 = open('ListeParticule.txt', 'a')
        file2.write('Top_quark'+ "\n")
        file2.write('Top_antiquark'+ "\n")
        file2.close()
        print('Palier 3 Débloqué --> Nouvelle particule disponible !')
    if totalepoint <= str(10000):
        pass
        #print('pas assez denergie')
    if 'Top_quark'and 'Top_antiquark'  in data1 and totalepoint >= str(10000):
        pass
    else : pass

    file1.close()