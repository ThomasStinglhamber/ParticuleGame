#module qui dessine le tableau
#scenario?
table = {
#index:[Elm_chimique, Nom_complet, Masse, col, lin,  Famille_chimique, config_elec]
0:['H', 'Hydrogen', '1.00794', 1, 1, 'Diatomic nonmetal', ' 1s1'],
1:['He', 'Helium', '4.002602', 18, 1, 'Noble gas', ' 1s2'],
2:['Li', 'Lithium', '6.941', 1, 2, 'Alkali metal', ' [He] 2s1'],
3:['Be', 'Beryllium', '9.012182', 2, 2, 'Alkaline earth metal', ' [He] 2s2'],
4:['B', 'Boron', '10.811', 13, 2, 'Metalloid', ' [He] 2s2 2p1'],
5:['C', 'Carbon', '12.0107', 14, 2, 'Polyatomic nonmetal', ' [He] 2s2 2p2'],
6:['N', 'Nitrogen', '14.0067', 15, 2, 'Diatomic nonmetal', ' [He] 2s2 2p3'],
7:['O', 'Oxygen', '15.9994', 16, 2, 'Diatomic nonmetal', ' [He] 2s2 2p4'],
8:['F', 'Fluorine', '18.9984032', 17, 2, 'Diatomic nonmetal', ' [He] 2s2 2p5'],
9:['Ne', 'Neon', '20.1797', 18, 2, 'Noble gas', ' [He] 2s2 2p6'],
10:['Na', 'Sodium', '22.98976...', 1, 3, 'Alkali metal', ' [Ne] 3s1'],
11:['Mg', 'Magnesium', '24.305', 2, 3, 'Alkaline earth metal', ' [Ne] 3s2'],
12:['Al', 'Aluminium', '26.9815386', 13, 3, 'Poor metal', ' [Ne] 3s2 3p1'],
13:['Si', 'Silicon', '28.0855', 14, 3, 'Metalloid', ' [Ne] 3s2 3p2'],
14:['P', 'Phosphorus', '30.973762', 15, 3, 'Polyatomic nonmetal', ' [Ne] 3s2 3p3'],
15:['S', 'Sulfur', '32.065', 16, 3, 'Polyatomic nonmetal', ' [Ne] 3s2 3p4'],
16:['Cl', 'Chlorine', '35.453', 17, 3, 'Diatomic nonmetal', ' [Ne] 3s2 3p5'],
17:['Ar', 'Argon', '39.948', 18, 3, 'Noble gas', ' [Ne] 3s2 3p6'],
18:['K', 'Potassium', '39.948', 1, 4, 'Alkali metal', ' [Ar] 4s1'],
19:['Ca', 'Calcium', '40.078', 2, 4, 'Alkaline earth metal', ' [Ar] 4s2'],
20:['Sc', 'Scandium', '44.955912', 3, 4, 'Transition metal', ' [Ar] 3d1 4s2'],
21:['Ti', 'Titanium', '47.867', 4, 4, 'Transition metal', ' [Ar] 3d2 4s2'],
22:['V', 'Vanadium', '50.9415', 5, 4, 'Transition metal', ' [Ar] 3d3 4s2'],
23:['Cr', 'Chromium', '51.9961', 6, 4, 'Transition metal', ' [Ar] 3d5 4s1'],
24:['Mn', 'Manganese', '54.938045', 7, 4, 'Transition metal', ' [Ar] 3d5 4s2'],
25:['Fe', 'Iron', '55.845', 8, 4, 'Transition metal', ' [Ar] 3d6 4s2'],
26:['Co', 'Cobalt', '58.933195', 9, 4, 'Transition metal', ' [Ar] 3d7 4s2'],
27:['Ni', 'Nickel', '58.6934', 10, 4, 'Transition metal', ' [Ar] 3d8 4s2'],
28:['Cu', 'Copper', '63.546', 11, 4, 'Transition metal', ' [Ar] 3d10 4s1'],
29:['Zn', 'Zinc', '65.38', 12, 4, 'Transition metal', ' [Ar] 3d10 4s2'],
30:['Ga', 'Gallium', '69.723', 13, 4, 'Poor metal', ' [Ar] 3d10 4s2 4p1'],
31:['Ge', 'Germanium', '72.63', 14, 4, 'Metalloid', ' [Ar] 3d10 4s2 4p2'],
32:['As', 'Arsenic', '74.9216', 15, 4, 'Metalloid', ' [Ar] 3d10 4s2 4p3'],
33:['Se', 'Selenium', '78.96', 16, 4, 'Polyatomic nonmetal', ' [Ar] 3d10 4s2 4p4'],
34:['Br', 'Bromine', '79.904', 17, 4, 'Diatomic nonmetal', ' [Ar] 3d10 4s2 4p5'],
35:['Kr', 'Krypton', '83.798', 18, 4, 'Noble gas', ' [Ar] 3d10 4s2 4p6'],
36:['Rb', 'Rubidium', '85.4678', 1, 5, 'Alkali metal', ' [Kr] 5s1'],
37:['Sr', 'Strontium', '87.62', 2, 5, 'Alkaline earth metal', ' [Kr] 5s2'],
38:['Y', 'Yttrium', '88.90585', 3, 5, 'Transition metal', ' [Kr] 4d1 5s2'],
39:['Zr', 'Zirconium', '91.224', 4, 5, 'Transition metal', ' [Kr] 4d2 5s2'],
40:['Nb', 'Niobium', '92.90628', 5, 5, 'Transition metal', ' [Kr] 4d4 5s1'],
41:['Mo', 'Molybdenum', '95.96', 6, 5, 'Transition metal', ' [Kr] 4d5 5s1'],
42:['Tc', 'Technetium', '(98)', 7, 5, 'Transition metal', ' [Kr] 4d5 5s2'],
43:['Ru', 'Ruthenium', '101.07', 8, 5, 'Transition metal', ' [Kr] 4d7 5s1'],
44:['Rh', 'Rhodium', '102.9055', 9, 5, 'Transition metal', ' [Kr] 4d8 5s1'],
45:['Pd', 'Palladium', '106.42', 10, 5, 'Transition metal', ' [Kr] 4d10'],
46:['Ag', 'Silver', '107.8682', 11, 5, 'Transition metal', ' [Kr] 4d10 5s1'],
47:['Cd', 'Cadmium', '112.411', 12, 5, 'Transition metal', ' [Kr] 4d10 5s2'],
48:['In', 'Indium', '114.818', 13, 5, 'Poor metal', ' [Kr] 4d10 5s2 5p1'],
49:['Sn', 'Tin', '118.71', 14, 5, 'Poor metal', ' [Kr] 4d10 5s2 5p2'],
50:['Sb', 'Antimony', '121.76', 15, 5, 'Metalloid', ' [Kr] 4d10 5s2 5p3'],
51:['Te', 'Tellurium', '127.6', 16, 5, 'Metalloid', ' [Kr] 4d10 5s2 5p4'],
52:['I', 'Iodine', '126.90447', 17, 5, 'Diatomic nonmetal', ' [Kr] 4d10 5s2 5p5'],
53:['Xe', 'Xenon', '131.293', 18, 5, 'Noble gas', ' [Kr] 4d10 5s2 5p6'],
54:['Cs', 'Caesium', '132.9054', 1, 6, 'Alkali metal', ' [Xe] 6s1'],
55:['Ba', 'Barium', '132.9054', 2, 6, 'Alkaline earth metal', ' [Xe] 6s2'],
56:['La', 'Lanthanum', '138.90547', 4, 9, 'Lanthanide', ' [Xe] 5d1 6s2'],
57:['Ce', 'Cerium', '140.116', 5, 9, 'Lanthanide', ' [Xe] 4f1 5d1 6s2'],
58:['Pr', 'Praseodymium', '140.90765', 6, 9, 'Lanthanide', ' [Xe] 4f3 6s2'],
59:['Nd', 'Neodymium', '144.242', 7, 9, 'Lanthanide', ' [Xe] 4f4 6s2'],
60:['Pm', 'Promethium', '(145)', 8, 9, 'Lanthanide', ' [Xe] 4f5 6s2'],
61:['Sm', 'Samarium', '150.36', 9, 9, 'Lanthanide', ' [Xe] 4f6 6s2'],
62:['Eu', 'Europium', '151.964', 10, 9, 'Lanthanide', ' [Xe] 4f7 6s2'],
63:['Gd', 'Gadolinium', '157.25', 11, 9, 'Lanthanide', ' [Xe] 4f7 5d1 6s2'],
64:['Tb', 'Terbium', '158.92535', 12, 9, 'Lanthanide', ' [Xe] 4f9 6s2'],
65:['Dy', 'Dysprosium', '162.5', 13, 9, 'Lanthanide', ' [Xe] 4f10 6s2'],
66:['Ho', 'Holmium', '164.93032', 14, 9, 'Lanthanide', ' [Xe] 4f11 6s2'],
67:['Er', 'Erbium', '167.259', 15, 9, 'Lanthanide', ' [Xe] 4f12 6s2'],
68:['Tm', 'Thulium', '168.93421', 16, 9, 'Lanthanide', ' [Xe] 4f13 6s2'],
69:['Yb', 'Ytterbium', '173.054', 17, 9, 'Lanthanide', ' [Xe] 4f14 6s2'],
70:['Lu', 'Lutetium', '174.9668', 18, 9, 'Lanthanide', ' [Xe] 4f14 5d1 6s2'],
71:['Hf', 'Hafnium', '178.49', 4, 6, 'Transition metal', ' [Xe] 4f14 5d2 6s2'],
72:['Ta', 'Tantalum', '180.94788', 5, 6, 'Transition metal', ' [Xe] 4f14 5d3 6s2'],
73:['W', 'Tungsten', '183.84', 6, 6, 'Transition metal', ' [Xe] 4f14 5d4 6s2'],
74:['Re', 'Rhenium', '186.207', 7, 6, 'Transition metal', ' [Xe] 4f14 5d5 6s2'],
75:['Os', 'Osmium', '190.23', 8, 6, 'Transition metal', ' [Xe] 4f14 5d6 6s2'],
76:['Ir', 'Iridium', '192.217', 9, 6, 'Transition metal', ' [Xe] 4f14 5d7 6s2'],
77:['Pt', 'Platinum', '195.084', 10, 6, 'Transition metal', ' [Xe] 4f14 5d9 6s1'],
78:['Au', 'Gold', '196.966569', 11, 6, 'Transition metal', ' [Xe] 4f14 5d10 6s1'],
79:['Hg', 'Mercury', '200.59', 12, 6, 'Transition metal', ' [Xe] 4f14 5d10 6s2'],
80:['Tl', 'Thallium', '204.3833', 13, 6, 'Poor metal', ' [Xe] 4f14 5d10 6s2 6p1'],
81:['Pb', 'Lead', '207.2', 14, 6, 'Poor metal', ' [Xe] 4f14 5d10 6s2 6p2'],
82:['Bi', 'Bismuth', '208.9804', 15, 6, 'Poor metal', ' [Xe] 4f14 5d10 6s2 6p3'],
83:['Po', 'Polonium', '(209)', 16, 6, 'Poor metal', ' [Xe] 4f14 5d10 6s2 6p4'],
84:['At', 'Astatine', '(210)', 17, 6, 'Metalloid', ' [Xe] 4f14 5d10 6s2 6p5'],
85:['Rn', 'Radon', '(222)', 18, 6, 'Noble gas', ' [Xe] 4f14 5d10 6s2 6p6'],
86:['Fr', 'Francium', '(223)', 1, 7, 'Alkali metal', ' [Rn] 7s1'],
87:['Ra', 'Radium', '(226)', 2, 7, 'Alkaline earth metal', ' [Rn] 7s2'],
88:['Ac', 'Actinium', '(227)', 4, 10, 'Actinide', ' [Rn] 6d1 7s2'],
89:['Th', 'Thorium', '232.03806', 5, 10, 'Actinide', ' [Rn] 6d2 7s2'],
90:['Pa', 'Protactinium', '231.0588', 6, 10, 'Actinide', ' [Rn] 5f2 6d1 7s2'],
91:['U', 'Uranium', '238.02891', 7, 10, 'Actinide', ' [Rn] 5f3 6d1 7s2'],
92:['Np', 'Neptunium', '(237)', 8, 10, 'Actinide', ' [Rn] 5f4 6d1 7s2'],
93:['Pu', 'Plutonium', '(244)', 9, 10, 'Actinide', ' [Rn] 5f6 7s2'],
94:['Am', 'Americium', '(243)', 10, 10, 'Actinide', ' [Rn] 5f7 7s2'],
95:['Cm', 'Curium', '(247)', 11, 10, 'Actinide', ' [Rn] 5f7 6d1 7s2'],
96:['Bk', 'Berkelium', '(247)', 12, 10, 'Actinide', ' [Rn] 5f9 7s2'],
97:['Cf', 'Californium', '(251)', 13, 10, 'Actinide', ' [Rn] 5f10 7s2'],
98:['Es', 'Einstenium', '(252)', 14, 10, 'Actinide', ' [Rn] 5f11 7s2'],
99:['Fm', 'Fermium', '(257)', 15, 10, 'Actinide', ' [Rn] 5f12 7s2'],
100:['Md', 'Mendelevium', '(258)', 16, 10, 'Actinide', ' [Rn] 5f13 7s2'],
101:['No', 'Nobelium', '(259)', 17, 10, 'Actinide', ' [Rn] 5f14 7s2'],
102:['Lr', 'Lawrencium', '(262)', 18, 10, 'Actinide', ' [Rn] 5f14 7s2 7p1'],
103:['Rf', 'Rutherfordium', '(267)', 4, 7, 'Transition metal', ' [Rn] 5f14 6d2 7s2'],
104:['Db', 'Dubnium', '(268)', 5, 7, 'Transition metal', ' [Rn] 5f14 6d3 7s2'],
105:['Sg', 'Seaborgium', '(271)', 6, 7, 'Transition metal', ' [Rn] 5f14 6d4 7s2'],
106:['Bh', 'Bohrium', '(272)', 7, 7, 'Transition metal', ' [Rn] 5f14 6d5 7s2'],
107:['Hs', 'Hassium', '(270)', 8, 7, 'Transition metal', ' [Rn] 5f14 6d6 7s2'],
108:['Mt', 'Meitnerium', '(276)', 9, 7, 'Unknown', ' [Rn] 5f14 6d7 7s2'],
109:['Ds', 'Darmstadium', '(281)', 10, 7, 'Unknown', ' [Rn] 5f14 6d8 7s2'],
110:['Rg', 'Roentgenium', '(280)', 11, 7, 'Unknown', ' [Rn] 5f14 6d9 7s2'],
111:['Cn', 'Copernicium', '(285)', 12, 7, 'Transition metal', ' [Rn] 5f14 6d10 7s2'],
112:['Uut', 'Unutrium', '(284)', 13, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p1'],
113:['Fl', 'Flerovium', '(289)', 14, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p2'],
114:['Uup', 'Ununpentium', '(288)', 15, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p3'],
115:['Lv', 'Livermorium', '(293)', 16, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p4'],
116:['Uus', 'Ununseptium', '(294)', 17, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p5'],
117:['Uuo', 'Ununoctium', '(294)', 18, 7, 'Unknown', ' [Rn] 5f14 6d10 7s2 7p6'],
}

import pygame
import couleur



def init(surface):
    '''Fonction qui initialise le tableau.
    Argument: Surface: display
    Retour: Dict'''
    
    att={}

    return att


def dessine(scen, surface):
    ''' Appele les differentes fonctions de dessin.
    arguments:
        scen: dict
        surface: display
    Retour:
        None '''
    
    dessine_tab(surface)
    ecris(surface)
    carre(surface)
   


#fonctions de dessin:

def dessine_tab(surface):
    ''' '''
    for i in table:
        lg=59
        lr=59
        x=lg*table[i][3]
        y=lr*table[i][4]

        if table[i][5]=='Noble gas':
            pygame.draw.rect(surface, (240, 195, 0), [x,y, lg,lr])
        elif table[i][5]=='Diatomic nonmetal':
            pygame.draw.rect(surface, (34, 66, 124), [x,y, lg,lr])
        elif table[i][5]=='Alkali metal':
            pygame.draw.rect(surface, (200,173,127), [x,y, lg,lr])
        elif table [i][5]=='Alkaline earth metal':
            pygame.draw.rect(surface, (0,128,0), [x,y, lg,lr])
        elif table[i][5]=='Metalloid':
            pygame.draw.rect(surface, (0,128,99), [x,y, lg,lr])
        elif table[i][5]=='Polyatomic nonmetal':
            pygame.draw.rect(surface, (99,228,99), [x,y, lg,lr])
        elif table[i][5]=='Poor metal':
            pygame.draw.rect(surface, (200,228,99), [x,y, lg,lr])
        elif table[i][5]=='Transition metal':
            pygame.draw.rect(surface, (100,0,0), [x,y, lg,lr])
        elif table[i][5]=='Actinide':
            pygame.draw.rect(surface, (250,0,0), [x,y, lg,lr])
        elif table[i][5]=='Unknown':
            pygame.draw.rect(surface, (250,0,70), [x,y, lg,lr])
        elif table[i][5]=='Lanthanide':
            pygame.draw.rect(surface, (0,150,150), [x,y, lg,lr])
        
        pygame.draw.rect(surface, (0, 0, 0), [x,y,lg,lr], 1)


#def tableau_gris(surface):
   # pygame.draw.rect(surface, GRIS, [x,y,lg,lr], 1)

def ecris(surface):
    '''  '''
    
    for i in table:
        lg=59
        lr=59
        x=lg*table[i][3]
        y=lr*table[i][4]
        e=1*table[i][0]
        
        police=pygame.font.Font(None, 25)
        texte=police.render(e, True, (255,255,255))
        surface.blit(texte, [x+5,y+2]) #+5 pour decaler l'ecriture
            
        m=1*table[i][2]
        police=pygame.font.Font(None, 16)
        texte=police.render(m, True, (255,255,255))
        surface.blit(texte, [x+2,y+40]) #+40 pour decaler l'ecriture


def carre(surface):
    ''' Dessine le grand carre de l'element pointe
    Argument:
        surface: display
    Retour:??'''
    pygame.draw.rect(surface,(200,200,200), [250,50, 150, 150])

def update(scenario):
    ''' '''
    pass
