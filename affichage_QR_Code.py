from typing import final
from main import final_message, version
from itertools import product
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# taille qr code
# version = 7
QR_Code_size = (((version-1)*4)+21)

# data 
QR_Code_Matrix = np.ones((QR_Code_size, QR_Code_size))*.5

# FINDERS PATTERNS
# matrice des finder pattern
Finder_Pattern = np.ones((7,7))
Finder_Pattern[1:6,1:6] = np.zeros((5,5))
Finder_Pattern[2:5,2:5] = np.ones((3,3))

# placements des finder patterns
# haut-gauche
QR_Code_Matrix[:7,:7] = Finder_Pattern

# haut-droit
QR_Code_Matrix[:7,-7:] = Finder_Pattern

# bas-gauche
QR_Code_Matrix[-7:,:7] = Finder_Pattern


# SEPARATORS
# haut-gauche
QR_Code_Matrix[7,:7] = np.zeros(7)
QR_Code_Matrix[:8,7] = np.zeros(8)

# haut-droit
QR_Code_Matrix[:7,-8] = np.zeros(7)
QR_Code_Matrix[7,-8:] = np.zeros(8)

# bas-gauche
QR_Code_Matrix[-8,:8] = np.zeros(8)
QR_Code_Matrix[-7:,7] = np.zeros(7)

# ALIGNEMENT PATTERNS

if version > 1:

    # matrice des alignement patterns
    Alignement_Pattern = np.ones((5,5))
    Alignement_Pattern[1:4, 1:4] = np.zeros((3,3))
    Alignement_Pattern[2,2] = 1

    # centre des modules d'alignement
    df_Alignement_Pattern_Locations = pd.read_csv('./data/Alignment Pattern Locations.csv', delimiter=';', index_col='Version').fillna(0).astype(int).apply(list, axis=1)
    df_Alignement_Pattern_Locations.columns = ['Center Module Row and Column']
    centres_modules = df_Alignement_Pattern_Locations.loc[f"QR Version {version}"]
    centres_modules = list(filter(lambda x: x != 0, centres_modules))
    centres_modules = list(product(centres_modules, repeat=2))

    for centre in centres_modules:

        # les modules d'alignement ne peuvent pas overlap les finder pattern
        if centre[0]-2 <= 7:

            if centre[1]-2 >= 8 and centre[1]+2 <= QR_Code_size-9:

                QR_Code_Matrix[centre[0]-2:centre[0]+3, centre[1]-2:centre[1]+3] = Alignement_Pattern

            
        elif centre[0]-2 >= 8 and centre[0]+2 <= QR_Code_size-9:

            QR_Code_Matrix[centre[0]-2:centre[0]+3, centre[1]-2:centre[1]+3] = Alignement_Pattern

        else:

            if centre[1]-2 >= 8:

                QR_Code_Matrix[centre[0]-2:centre[0]+3, centre[1]-2:centre[1]+3] = Alignement_Pattern

# FORMAT INFORMATION AREA
# haut-gauche
QR_Code_Matrix[:9,8] = np.ones(9)*.7
QR_Code_Matrix[8,:8] = np.ones(8)*.7

# bas-gauche
QR_Code_Matrix[-7:,8] = np.ones(7)*.7

# haut-droit
QR_Code_Matrix[8,-8:] = np.ones(8)*.7

# VERSION INFORMATION AREA
if version >= 7:

    # haut-droit
    QR_Code_Matrix[:6,-11:-8] = np.ones((6,3))*.3

    # bas-gauche
    QR_Code_Matrix[-11:-8,:6] = np.ones((3,6))*.3

# DARK MODULE
QR_Code_Matrix[(4 * version) + 9, 8]  = 1

# TIMIING PATTERNS
Altenating_Pattern = np.zeros(QR_Code_size-16)
Altenating_Pattern[::2] = 1
QR_Code_Matrix[6,8:QR_Code_size-8] = Altenating_Pattern
QR_Code_Matrix[8:QR_Code_size-8,6] = Altenating_Pattern

# DATA
current_bit = 0
current_coordonates = [QR_Code_size-1,QR_Code_size-1]
pattern_placement = ['upward', 'left']

# PATTERN PLACEMENT
stop = 0
# while current_coordonates != [QR_Code_size-1,0]:
while current_coordonates != [QR_Code_size-1,0] and current_coordonates[1] >= 0:

    # le module courant est disponible
    if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
        
        # placement du bit courant
        QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]

        # mise a jour du bit courant
        current_bit += 1

    # prochain module
    if pattern_placement == ['upward', 'left']:

        current_coordonates[1] -= 1
        pattern_placement[1] = 'up-right'

        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")
        

    elif pattern_placement == ['upward', 'up-right']:

        current_coordonates[0] -= 1
        current_coordonates[1] += 1
        pattern_placement[1] = 'left'

        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")

    elif pattern_placement == ['downward', 'left']:

        current_coordonates[1] -= 1
        pattern_placement[1] = 'down-right'       

        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")

    elif pattern_placement == ['downward', 'down-right']:

        current_coordonates[0] += 1
        current_coordonates[1] += 1
        pattern_placement[1] = 'left'    

        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")


    # changement du sens vertical : upward -> downward
    if  current_coordonates[0] == 0 and pattern_placement[1] == 'up-right':

        # le module courant est disponible
        if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
            
            # placement du bit courant
            QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]

            # mise a jour du bit courant
            current_bit += 1
        
        pattern_placement = ['downward', 'left']

        # /!\ vertical timing pattern /!\
        if current_coordonates[1] != 7:
            current_coordonates[1] -= 1

        else:
            print(" ")
            print("TIMING PATTERN")
            print(" ")
            current_coordonates[1] -= 2
        
        print("upward -> downward")
        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")


    # changement du sens vertical : downward -> upward
    if  current_coordonates[0] == QR_Code_size-1 and pattern_placement[1] == 'down-right':

        # le module courant est disponible
        if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
            
            # placement du bit courant
            QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]

            # mise a jour du bit courant
            current_bit += 1

        pattern_placement = ['upward', 'left']
        current_coordonates[1] -= 1

        print("downward -> upward")
        print(f"current_coordonates : {current_coordonates}")
        print(f"pattern_placement : {pattern_placement}")

        
        
# print(QR_Code_Matrix)

# AFFICHAGE
fig, ax = plt.subplots()
ax.imshow(QR_Code_Matrix, cmap='Greys')
ax.set_aspect('equal')
plt.show()