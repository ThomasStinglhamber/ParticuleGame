#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:11:06 2022
@author: thomasstinglhamber
"""
from Particule import *
from Collision import *
from Energy import *
#ListParticule=['Up_quark','Down_quark','Proton','Neutron','Strange_quark']
#ListParticuleDecouverte=['Up_quark','Down_quark']

interac =[Up_quark,Bottom_antiquark]

NombreQuark =len(interac)

NouvelleDecouverte = False

if __name__ == "__main__" :
    name,energy,interaction=Down_quark()
    name,energy,interaction=Up_quark()
    name,energy,interaction=Strange_quark()
    print("Collision :")
    if NombreQuark ==3:
        decouverte,nom1,nom2,nom3 =collision3(interac[0],interac[1],interac[2])
        print(nom1,"+",nom2,"+",nom3,"-->",decouverte)
    else : 
        decouverte,nom1,nom2 =collision2(interac[0],interac[1])
        print(nom1,"+",nom2,"-->",decouverte)
    
    
    
    mot = decouverte
    
    
    
    listenergy,energie =Energy(mot)
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
                    print("Particule deja découverte")
                    print("Nom :",decouverte)
                    print("Energie :",energie)
                    NouvelleDecouverte = True
                    break
                if mot not in data1 :
                    print("------------- Nouvelle decouverte ! -------------")
                    print("Nom :",decouverte)
                    print("Energie :",energie)
                    NouvelleDecouverte = True
                    file2 = open('ListeParticule.txt', 'a')
                    file2.write(mot+ "\n")
                    file2.close()
                    break
            file1.close() 
            break
    if NouvelleDecouverte == False:
        print("la combinaison donne  rien")
        
    file.close()
    
    

    
