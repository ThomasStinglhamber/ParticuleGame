#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:11:06 2022
@author: thomasstinglhamber
"""
from Particule import *
from Collision import *
from Energy import *
from ComptabilisationEnergy import *
from conversionSTR_DEF import *
import time
#from fenetre import *
#from affichage_parti import *

def Principal(INTERACTION):
    failed=False   
    interac=[]
    #print(INTERACTION)
    for i in INTERACTION: 
        intermediaire = globals()[i]
        interac.append(intermediaire)
        #print(interac)

    NombreQuark =len(interac)
    
    
    NouvelleDecouverte = False
    
    
    QUARK = [Up_quark,Up_antiquark,Down_quark,Down_antiquark,Strange_quark,Strange_antiquark,Charmed_quark,Charmed_antiquark,Bottom_quark,Bottom_antiquark]
    if  failed==False:
        #name,energy,interaction=Down_quark()
        #name,energy,interaction=Up_quark()
        #name,energy,interaction=Strange_quark()
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
                    if mot in data1:                        # si deja dans la liste, on fait rien
                        print("Particule deja découverte")
                        print("Nom :",decouverte)
                        print("Energie :",energie)
                        NouvelleDecouverte = True
                        
                        break
                    if mot not in data1 :       # si pas dans la liste, on l'ajoute + on donne les points
                        print("------------- Nouvelle decouverte ! -------------")
                        print("Nom :",decouverte)
                        print("Energie :",energie)
                        NouvelleDecouverte = True
                        file2 = open('ListeParticule.txt', 'a')
                        file2.write(mot+ "\n")
                        file2.close()
                        
                        #------ Systeme d''ecriture des points
                        jauge,points=Gauge(mot)
                        file4 = open('Point.txt', 'r')
                        point=file4.read()#.splitlines()
                        #print(point)
                        #print(int(point))
                        tot = int(point)+ points
                        #print(tot)
                        tofile = str(tot)
                        
                        file3 = open('Point.txt', 'w')
                        file3.write(tofile)
                        file3.close()
                        file4.close()
                        
                        break
                file1.close() 
                break
            
        
        puntos = checkpoint()
        palier1,palier2,palier3 = Palier(puntos)
        #print(palier1)
        
        if NouvelleDecouverte == False:         # si la combinaison donne rien on le dit 
            print("la combinaison donne  rien")
            
        file.close()
        
        
    #else : print('Particule pas encore decouverte') # si on prend une particule qu'on a pas
    
    interac=[]
    return


