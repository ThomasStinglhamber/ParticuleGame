#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:11:06 2022
@author: thomasstinglhamber
"""
from Particule import *
from Collision import *
#ListParticule=['Up_quark','Down_quark','Proton','Neutron','Strange_quark']
#ListParticuleDecouverte=['Up_quark','Down_quark']

interac =[Up_quark,Down_antiquark]

NombreQuark =len(interac)



if __name__ == "__main__" :
    name,energy,interaction=Down_quark()
    name,energy,interaction=Up_quark()
    name,energy,interaction=Strange_quark()
    if NombreQuark ==3:
        decouverte =collision3(interac[0],interac[1],interac[2])
    else : 
        decouverte =collision2(interac[0],interac[1])

    print(decouverte)
    
    
    mot = decouverte

    # opening a file in 'r'
    file = open('ParticuleTotale.txt', 'r')
    data = file.read().splitlines()
    # printing the data
    #print(len(data))
    
    for i in range(len(data)):
        #print(data[i])
        if mot == data[i]:
            #print(data[i])
            file1 = open('ListeParticule.txt', 'r')
            data1 = file1.read().splitlines()
            #print(data1)
            for j in range(len(data1)):
                #print(data1[j])
                if mot in data1:
                    print("dedans")
                    break
                if mot not in data1 :
                    print("pas dedans")
                    file2 = open('ListeParticule.txt', 'a')
                    file2.write(mot+ "\n")
                    file2.close()
                    break
            file1.close() 
            break
        
    file.close()
