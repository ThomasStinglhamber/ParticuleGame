#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:13:16 2022
@author: thomasstinglhamber
"""

from Particule import *


def collision3(particule1,particule2,particule3):
    
    decouverte=''
    particule1_name,particule1_energy,particule1_interaction= particule1()
    particule2_name,particule2_energy,particule2_interaction= particule2()
    particule3_name,particule3_energy,particule3_interaction= particule3()
    name1=particule1_name+particule2_name
    #print(name1)
    for i in particule3_interaction:
        if i == name1:
            decouverte =particule3_interaction[i]
            #print(decouverte)
            break
        else : pass
        
    return decouverte,particule1_name,particule2_name,particule3_name

def collision2(particule1,particule2):
    
    decouverte=''
    particule1_name,particule1_energy,particule1_interaction= particule1()
    particule2_name,particule2_energy,particule2_interaction= particule2()
   
    #print(name1)
    for i in particule2_interaction:
        if i == particule1_name:
            decouverte =particule2_interaction[i]
            #print(decouverte)
            break
        else : pass
        
    return decouverte,particule1_name,particule2_name