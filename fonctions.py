from classes import *
from bitarray import *
from bitarray.util import ba2int
from itertools import product
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def determine_smallest_version(chaine, EC_lvl, mode):

    characters_number = len(chaine)

    df_Character_Capacities = pd.read_csv('./data/Character Capacities Table.csv', delimiter=',', index_col=['Version','Error Correction Level'])
    
    version = 1
    while df_Character_Capacities.loc[(version, EC_lvl), mode] < characters_number:
        version += 1

    return version


def choose_most_efficient_mode(chaine):

    # alphanumeric table
    alphanumeric_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
                          'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
                          'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
                          '+': 40, '-': 41, '.': 42, '/': 43, ':': 44}
    
    if chaine.isdecimal():
        mode = 'numeric'
    
    elif all(characters in alphanumeric_table for characters in chaine):
        mode = 'alphanumeric'

    else:
        mode = 'byte'
    
    
    return mode


def byte_mode_encoding(chaine):
    """ Encode les caracteres de la chaine en mots de 8 bits
    
    INPUT
    -----
    - chaine: type -> string, la chaine de caractere a encoder
    
    OUTPUT
    ------
    - encodage : type -> list, liste contenant les mots de 8 bits qui encodent les caracteres
    """
    
    # liste des caracteres de la chaine encodes en binaire
    encodage = []

    for char in chaine:

        # ajout du mot binaire correspondant a chacun des caracteres (norme ASCII - Unicode)    
        encodage.append(bitarray(format(ord(char),'b')))

        # ajout eventuel de bits nuls de sorte a obtenir des mots de 8 bits
        while len(encodage[-1]) < 8:
            encodage[-1] = bitarray('0') + encodage[-1]
    
    return encodage


def alphanumeric_mode_encoding(chaine):

    # alphanumeric table
    alphanumeric_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
                        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
                        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, ' ': 36, '$': 37, '%': 38, '*': 39,
                        '+': 40, '-': 41, '.': 42, '/': 43, ':': 44}

    # encodage
    encodage = []

    # separer la chaine en paires de caracteres
    pairs = [chaine[index : index + 2] for index in range(0, len(chaine), 2)]

    for pair in pairs:

        if len(pair) % 2 == 0:

            encodage.append(bitarray(format(alphanumeric_table[pair[0]]*45 + alphanumeric_table[pair[1]],'b')))

            # ajout eventuel de bits nuls de sorte a obtenir des mots de 11 bits
            while len(encodage[-1]) < 11:
                encodage[-1] = bitarray('0') + encodage[-1]

        else:

            encodage.append(bitarray(format(alphanumeric_table[pair],'b')))

            # ajout eventuel de bits nuls de sorte a obtenir un mot de 6 bits
            while len(encodage[-1]) < 6:
                encodage[-1] = bitarray('0') + encodage[-1]
    
    return encodage


def numeric_mode_encoding(chaine):
    
    # encodage
    encodage = []

    # separer la chaine en paires de caracteres
    triplets = [chaine[index : index + 3] for index in range(0, len(chaine), 3)]

    for triplet in triplets:

        if len(triplet) == 3:

            if triplet[:2] == '00':
                encodage.append(bitarray(format(int(triplet[2]),'b'))) 

            elif triplet[0] == '0':
                encodage.append(bitarray(format(int(triplet[1:]),'b')))

            else:
                encodage.append(bitarray(format(int(triplet),'b')))
            
            # ajout eventuel de bits nuls de sorte a obtenir un mot de 10 bits
            while len(encodage[-1]) < 10:
                encodage[-1] = bitarray('0') + encodage[-1]

        elif len(triplet) == 2:
            
            if triplet[0] == '0':
                encodage.append(bitarray(format(int(triplet[1]),'b')))

            else:
                encodage.append(bitarray(format(int(triplet),'b')))

            # ajout eventuel de bits nuls de sorte a obtenir un mot de 7 bits
            while len(encodage[-1]) < 7:
                encodage[-1] = bitarray('0') + encodage[-1]
        
        else:
            encodage.append(bitarray(format(int(triplet),'b')))

            # ajout eventuel de bits nuls de sorte a obtenir un mot de 4 bits
            while len(encodage[-1]) < 4:
                encodage[-1] = bitarray('0') + encodage[-1]            

    return encodage

def add_mode_indicator(liste, mode):
    """ Ajoute le mode d'encodage au debut de liste
    
    INPUTS
    ------
    - liste : type -> list, une liste de mots binaires 
    - mode : type -> string, le mode d'encodage (numerique, alphanumerique, byte ou kanji)

    OUTPUT
    ------
    - liste : type -> list, une liste de mots binaires
    """
    mode_indicators = {'numeric': bitarray('0001'), 
                       'alphanumeric': bitarray('0010'),
                       'byte': bitarray('0100'),
                       'kanji': bitarray('1000')}

    liste = [mode_indicators[mode]] + liste

    return liste


def add_character_count_indicator(chaine, liste, mode, version):
    """ Ajoute l'indicateur du nombre de caracteres
    
    INPUTS
    ------
    - chaine : type -> string, la chaine de caractere a encoder
    - liste : type -> list, une liste de mots binaires 
    - mode : type -> string, le mode d'encodage (numerique, alphanumerique, byte ou kanji)
    - version : type -> int, la version du QR code

    OUTPUT
    ------
    - liste : type -> list, une liste de mots binaires
    """

    character_count_indicator_dict = {
        # versions 1 a 9
        (1, 'numeric') : 10,
        (1, 'alphanumeric') : 9,
        (1, 'byte') : 8,
        (1, 'kanji') : 8,

        # versions 10 a 26
        (2, 'numeric') : 12,
        (2, 'alphanumeric') : 11,
        (2, 'byte') : 16,
        (2, 'kanji') : 10,

        # versions 27 a 40
        (3, 'numeric') : 14,
        (3, 'alphanumeric') : 13,
        (3, 'byte') : 16,
        (3, 'kanji') : 12}

    if version <= 9:
        version_category = 1

    elif version <= 26:
        version_category = 2

    else:
        version_category = 3

    # nombre de caracteres de la chaine en mot binaire
    character_count_indicator = bitarray(format(len(chaine),'b'))

    # ajout eventuel de bits nuls en fonction du mode et de la version
    while len(character_count_indicator) < character_count_indicator_dict[(version_category, mode)]:
        character_count_indicator = bitarray('0') + character_count_indicator
    
    # insertion de l'indicateur 
    liste.insert(1, character_count_indicator)

    return liste


def add_terminator_padBytes(liste, version, EC_lvl):
    """ Ajoute les eventuels bits afin d'atteindre la capacite maximale du QR code
    
    INPUTS
    ------
    - liste : type -> list, une liste de mots binaires
    - version : type -> int, la version du QR code
    - EC_lvl : type -> str, le caractere correspondant au niveau de correction du QR code

    OUTPUT
    ------
    - liste : type -> list, une liste de mots binaires
    """
    # ouverture du fichier reprenant les nombres de bits du QR code en fonction de la version et du taux de corrections
    df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")

    # nombre total de bits necessaires pour le QR code
    version_and_EC_lvl = str(version) + '-' + EC_lvl
    total_bits_number = 8*int(df_Error_correction_table.loc[version_and_EC_lvl]['Total Number of Data Codewords for this Version and EC Level'])

    # calcul du nombre de bits de la liste
    bits_number = 0
    for word in liste:
        bits_number += len(word)

    # ajout des bits nuls eventuels en fin de message
    if total_bits_number - bits_number >= 4:
        terminator = 4*bitarray('0')

    elif total_bits_number - bits_number !=0:
        terminator = (total_bits_number - bits_number)*bitarray('0')
    
    liste = liste + [terminator]
    bits_number += len(terminator)

    # ajout des pad bytes eventuels en fin de message
    # ajout des bits tq bits_number % 8 == 0
    if bits_number % 8 != 0:
        liste = liste + [(8 - (bits_number % 8))*bitarray('0')]
        bits_number += bits_number % 8

    # ajout des bits de sorte a atteindre la capacite maximum
    remaining_capacity = total_bits_number - bits_number
    pad_byte_1 = bitarray('11101100')
    pad_byte_2 = bitarray('00010001')
    
    compteur = 1
    while remaining_capacity > 0:

        if compteur % 2 == 1:
            liste = liste + [pad_byte_1]
        
        else:
            liste = liste + [pad_byte_2]

        remaining_capacity -= 8
        compteur += 1
        
    return liste


def data_encoding(chaine, mode, version, EC_lvl):
    """ encode les donnees pour le mode d'encodage, la version et le niveau de correction du QR code
    
    INPUTS
    ------
    - chaine : type -> string, la chaine de caractere a encoder
    - mode : type -> string, le mode d'encodage (numerique, alphanumerique, byte ou kanji)
    - version : type -> int, la version du QR code
    - EC_lvl : type -> str, le caractere correspondant au niveau de correction du QR code

    OUTPUT
    ------
    - data_codewords : type -> bitarray, les mots codes binaires encodes et concatenes
    """
    if mode == 'byte':
        liste = byte_mode_encoding(chaine)

    elif mode == 'alphanumeric':
        liste = alphanumeric_mode_encoding(chaine)

    elif mode == 'numeric':
        liste = numeric_mode_encoding(chaine)

    liste = add_mode_indicator(liste, mode)
    liste = add_character_count_indicator(chaine, liste, mode, version)
    liste = add_terminator_padBytes(liste, version, EC_lvl)

    data_codewords = bitarray()
    for word in liste:
        data_codewords += word

    return data_codewords


def break_data_codewords_into_blocks(data_codewords, version, EC_lvl):
    """ separe les mots codes par groupes, eux memes separes en blocs
    
    INPUTS
    ------
    - data_codewords : type -> bitarray, les mots codes binaires encodes et concatenes
    - version : type -> int, la version du QR code
    - EC_lvl : type -> str, le caractere correspondant au niveau de correction du QR code

    OUTPUT
    ------
    - groups_list : type -> list, les groupes de blocs de mots codes
    """
    # ouverture du fichier reprenant le nombre de groupes et de blocs par version et niveau de correction d'erreur
    df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")

    # separation en groupes
    version_and_EC_lvl = str(version) + '-' + EC_lvl
    groups_number = int(pd.notnull(df_Error_correction_table.loc[version_and_EC_lvl, 'Number of Blocks in Group 1'])) + int(pd.notnull(df_Error_correction_table.loc[version_and_EC_lvl, 'Number of Blocks in Group 2']))
    groups_list = []
    compteur = 0

    for i in range(0,groups_number):

        blocks_number = int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Blocks in Group {i+1}"])
        blocks_list = []

        # separation en blocs
        for j in range(0, blocks_number):

            data_codewords_number = int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Data Codewords in Each of Group {i+1}'s Blocks"])
            codewords_list = []

            # separation en mots-codes
            for k in range(0, data_codewords_number):

                # ajout du mot code courant
                codeword = data_codewords[compteur:compteur+8]
                codewords_list.append(codeword)
                
                compteur += 8
            
            # ajout du bloc courant a la liste de blocs
            blocks_list.append(Block(codewords_list, []))
        
        groups_list.append(Group(blocks_list))
    
    return groups_list


def generate_message_polynomial(block):
    """ genere le polynome messager correspondant au bloc donne en argument
    
    INPUT
    ------
    block : type -> Block, le bloc reprenant les mots codes qui serviront de coefficients au polynome messager
    
    OUTPUT
    ------
    message_polynomial : type -> numpy array, le polynome messager correspondant au bloc 'block'
    """

    # recuperation des mots codes
    codewords_list = block.codewords_list

    # liste des coefficients du polynome messager
    coefficients_list = []
    for codeword in codewords_list:
        coefficients_list.append(ba2int(codeword))
    # coefficients_list.reverse()

    # generation du polynome messager
    message_polynomial = np.array(coefficients_list)

    return message_polynomial


def generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table):
    """ genere les exposants des coefficients du polynome generateur 
        pour le degre donne en argument
    
    INPUT
    ------
    degree_generator_polynomial : type -> int, le degre du polynome generateur
    df_Antilog_table : type -> pandas DataFrame, table antilog
    df_Log_table : type -> pandas DataFrame, table log
    
    OUTPUT
    ------
    generator_polynomial : type -> numpy array, les exposants des coefficients du polynome generateur    
    """

    # exposants des coefficients du polynome generateurs (initialisation)
    coefficients_exponents = np.zeros(2, dtype=np.uint8)

    # polynome generateur : (x-2^0)(x-2^1)...(x-2^{n-1})
    for i in range(1,degree_generator_polynomial):

        # multiplication par x^i
        shifted_coefficients_exponents = np.append(coefficients_exponents, 0)

        # multiplication par -2^i
        for j in range(0,len(coefficients_exponents)):

            if coefficients_exponents[j] + i > 255:
                exponent = (coefficients_exponents[j] + i) % 255

            else:
                exponent = coefficients_exponents[j] + i  

            # combiner les termes de memes degres
            if j != len(coefficients_exponents)-1:
                integer_counterpart = df_Antilog_table.loc[exponent]['integer'] ^ df_Antilog_table.loc[shifted_coefficients_exponents[j+1]]['integer']
            
            else:
                integer_counterpart = df_Antilog_table.loc[exponent]['integer']

            # retour a l'exposant
            shifted_coefficients_exponents[j+1] = df_Log_table.loc[integer_counterpart]['exponent']

        # mise a jour des exposants des coefficients
        coefficients_exponents = shifted_coefficients_exponents
    
    # polynome generateur
    generator_polynomial = coefficients_exponents

    return generator_polynomial


def EC_codewords_generator(message_polynomial, generator_polynomial, df_Antilog_table, df_Log_table):

    # nombre de termes du polynome generateur
    m = len(generator_polynomial)

    # le nombre d'etapes dans la division correspond au nombre de termes du polynome generateur
    steps = len(message_polynomial)
    k=0
    while k < steps:

        # nombre de termes du polynome messager
        n = len(message_polynomial)

        # multiplier le polynome generateur par le coefficient de tete du polynome messager
        head_exponent = df_Log_table.loc[message_polynomial[0]]['exponent']

        for i in range(0,m):

            if generator_polynomial[i] + head_exponent > 255:
                generator_polynomial[i] = (generator_polynomial[i] + head_exponent) % 255

            else:
                generator_polynomial[i] += head_exponent
            
            generator_polynomial[i] = df_Antilog_table.loc[generator_polynomial[i]]['integer']

        # division polynomiale (XOR)
        for i in range(0,min(m,n)):

            message_polynomial[i] = message_polynomial[i] ^ generator_polynomial[i]
        

        if n < m: 
            
            message_polynomial = np.append(message_polynomial, np.zeros(m-n, dtype=np.uint8))

            for i in range(n, n+(m-n)):
                message_polynomial[i] = message_polynomial[i] ^ generator_polynomial[i]

        
        if n > m:

            for i in range(n, n + (m-n)):
                message_polynomial[i] = message_polynomial[i] ^ 0


        while message_polynomial[0] == 0:
            message_polynomial = message_polynomial[1:]
            k += 1

        # reset polynome generateur
        generator_polynomial = generate_generator_polynomial(m-1, df_Antilog_table, df_Log_table)

    return message_polynomial


def final_message_generator(version, version_and_EC_lvl, degree_generator_polynomial, groups_number, groups_list, df_Error_correction_table, df_Versions_Required_Remainder_Bits):

    # ENTRELACEMENT
    interleaved_data = []

    # nombre total de blocs
    blocks_total_number = 0
    for i in range(1,groups_number+1):
        blocks_total_number += int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Blocks in Group {i}"])

    # longueur max des mots codes
    codewords_max_size = int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Data Codewords in Each of Group {groups_number}'s Blocks"])

    # matrice des mots codes (-1 -> valeur manquante)
    codewords_matrix = np.ones((blocks_total_number,codewords_max_size), dtype=np.uint8)*(-1)

    # matrice des mots correcteurs
    EC_codewords_matrix = np.zeros((blocks_total_number, degree_generator_polynomial), dtype=np.uint8)

    # groupe courant
    index = 0
    for i in range(0,groups_number):

        # bloc courant
        for j in range(0,len(groups_list[i].blocks_list)):
            
            for k in range(0,len(groups_list[i].blocks_list[j].codewords_list)):

                codewords_matrix[index,k] = ba2int(groups_list[i].blocks_list[j].codewords_list[k])
            
            EC_codewords_matrix[index] = groups_list[i].blocks_list[j].EC_codewords_list

            index += 1

    # entrelacement des mots codes
    for i in range(0,codewords_matrix.shape[1]):

        for j in range(0, codewords_matrix.shape[0]):

            if codewords_matrix[j,i] != -1:

                interleaved_data.append(codewords_matrix[j,i])

    # entrelacement des mots correcteurs
    for i in range(0, EC_codewords_matrix.shape[1]):

        for j in range(0, EC_codewords_matrix.shape[0]):

            interleaved_data.append(EC_codewords_matrix[j,i])

    # conversion du message final en notation binaire
    final_message_list = []
    final_message = bitarray()
    for word in interleaved_data:

        final_message_list.append(bitarray(format(word,'b')))

        # ajout eventuel de bits nuls de sorte a obtenir des mots de 8 bits
        while len(final_message_list[-1]) < 8:
            final_message_list[-1] = bitarray('0') + final_message_list[-1]

        final_message += final_message_list[-1]

    # ajout eventuel de bits requis
    final_message += int(df_Versions_Required_Remainder_Bits.loc[version])*bitarray('0')

    return final_message


def mask(mask_number, row, column, bit):

    if mask_number == 0 and (row + column) % 2 == 0:
        bit = bit ^ 1
 
    elif mask_number == 1 and row % 2 == 0:
        bit = bit ^ 1
 
    elif mask_number == 2 and column % 3 == 0:
        bit = bit ^ 1
 
    elif mask_number == 3 and (row + column) % 3 == 0:
        bit = bit ^ 1
 
    elif mask_number == 4 and (np.floor(row / 2) + np.floor(column/3) ) % 2 == 0:
        bit = bit ^ 1
 
    elif mask_number == 5 and ((row * column) % 2) + ((row * column) % 3) == 0 == 0:
        bit = bit ^ 1
 
    elif mask_number == 6 and ( ((row * column) % 2) + ((row * column) % 3) ) % 2 == 0:
        bit = bit ^ 1
 
    elif mask_number == 7 and ( ((row + column) % 2) + ((row * column) % 3) ) % 2 == 0:
        bit = bit ^ 1

    return bit

def data_masking_condition_1(QR_Code_row_or_column, QR_Code_size):

    penalty = 0
    i = 0
    while i <= QR_Code_size-6:

        if np.min(QR_Code_row_or_column[i:i+5]) == np.max(QR_Code_row_or_column[i:i+5]):
            
            penalty += 3
            i += 5

            if i == QR_Code_size-1:
                break

            while QR_Code_row_or_column[i] == QR_Code_row_or_column[i-1]:

                penalty += 1

                if i == QR_Code_size-1:
                    break

                i += 1

        else:

            i += 1
    
    return penalty

def data_masking_condition_2(QR_Code_Matrix_subblock):
    
    penalty = 0

    if np.max(QR_Code_Matrix_subblock[0:0+2,0:0+2]) == np.min(QR_Code_Matrix_subblock[0:0+2,0:0+2]):
        penalty = 3

    return penalty

def data_masking_condition_3(QR_code_Matrix_band):

    penalty = 0
    pattern = np.array([1,0,1,1,1,0,1,0,0,0,0], dtype=np.float64)

    if (QR_code_Matrix_band==pattern).all() or (np.flipud(QR_code_Matrix_band)==pattern).all():

        penalty += 40

    return penalty

def data_masking_condition_4(QR_Code_Matrix, QR_Code_size):

    # nombre de modules noirs
    dark_modules_number = np.count_nonzero(QR_Code_Matrix == 1)

    # nombre de modules
    modules_number = QR_Code_size ** 2

    # (modules noirs / modules) * 100
    dark_modules_ratio = dark_modules_number / modules_number * 100

    # multiples de 5 précédents et suivants
    previous_5_multiple = np.floor(dark_modules_ratio/5)*5
    next_5_multiple = np.ceil(dark_modules_ratio/5)*5

    # calcul de la penalite
    penalty_condition_4 = min(abs(previous_5_multiple-50), abs(next_5_multiple-50))*2

    return penalty_condition_4

def compute_penalty_score(QR_Code_Matrix, QR_Code_size):

    # Evaluation Condition #1
    penalty_condition_1 = 0
    for i in range(0,QR_Code_size):

        # lignes
        penalty_condition_1 += data_masking_condition_1(QR_Code_Matrix[i,:], QR_Code_size)

        # colonnes
        penalty_condition_1 += data_masking_condition_1(QR_Code_Matrix[:,i], QR_Code_size)


    # Evaluation Condition #2
    penalty_condition_2 = 0
    for i in range(0,QR_Code_size-1):

        for j in range(0,QR_Code_size-1):

            penalty_condition_2 += data_masking_condition_2(QR_Code_Matrix[i:i+2,j:j+2])


    # Evaluation Condition #3
    penalty_condition_3 = 0
    for i in range(0, QR_Code_size):

        for j in range(0, QR_Code_size-11):

            # lignes
            penalty_condition_3 += data_masking_condition_3(QR_Code_Matrix[i, j:j+11])

            # colonnes
            penalty_condition_3 += data_masking_condition_3(QR_Code_Matrix[j:j+11, i])


    # Evaluation Condition #4
    penalty_condition_4 = data_masking_condition_4(QR_Code_Matrix, QR_Code_size)

    print(f"penalty_condition_1 : {penalty_condition_1}")
    print(f"penalty_condition_2 : {penalty_condition_2}")
    print(f"penalty_condition_3 : {penalty_condition_3}")
    print(f"penalty_condition_4 : {penalty_condition_4}")

    return penalty_condition_1 + penalty_condition_2 + penalty_condition_3 + penalty_condition_4


def finder_patterns_placement(QR_Code_Matrix):

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

    return QR_Code_Matrix

def separators_placement(QR_Code_Matrix):

    # haut-gauche
    QR_Code_Matrix[7,:7] = np.zeros(7)
    QR_Code_Matrix[:8,7] = np.zeros(8)

    # haut-droit
    QR_Code_Matrix[:7,-8] = np.zeros(7)
    QR_Code_Matrix[7,-8:] = np.zeros(8)

    # bas-gauche
    QR_Code_Matrix[-8,:8] = np.zeros(8)
    QR_Code_Matrix[-7:,7] = np.zeros(7)

    return QR_Code_Matrix

def alignement_patterns_placement(QR_Code_Matrix, QR_Code_size, version):

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
    
    return QR_Code_Matrix


def format_information_areas_placement(QR_Code_Matrix):

    # haut-gauche
    QR_Code_Matrix[:9,8] = np.ones(9)*.7
    QR_Code_Matrix[8,:8] = np.ones(8)*.7

    # bas-gauche
    QR_Code_Matrix[-7:,8] = np.ones(7)*.7

    # haut-droit
    QR_Code_Matrix[8,-8:] = np.ones(8)*.7

    return QR_Code_Matrix


def version_information_areas_placement(QR_Code_Matrix):

    # haut-droit
    QR_Code_Matrix[:6,-11:-8] = np.ones((6,3))*.3

    # bas-gauche
    QR_Code_Matrix[-11:-8,:6] = np.ones((3,6))*.3

    return QR_Code_Matrix


def timing_patterns_placement(QR_Code_Matrix, QR_Code_size):
    
    Alternating_Pattern = np.zeros(QR_Code_size-16)
    Alternating_Pattern[::2] = 1
    QR_Code_Matrix[6,8:QR_Code_size-8] = Alternating_Pattern
    QR_Code_Matrix[8:QR_Code_size-8,6] = Alternating_Pattern

    return QR_Code_Matrix


def data_placement(QR_Code_Matrix, QR_Code_size, final_message, mask_number):

    current_bit = 0
    current_coordonates = [QR_Code_size-1,QR_Code_size-1]
    pattern_placement = ['upward', 'left']

    # PATTERN PLACEMENT
    while current_coordonates != [QR_Code_size-1,0] and current_coordonates[1] >= 0:

        # le module courant est disponible
        if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
            
            # placement du bit courant
            # QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]
            QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = mask(mask_number, current_coordonates[0], current_coordonates[1], final_message[current_bit])

            # mise a jour du bit courant
            current_bit += 1

        # prochain module
        if pattern_placement == ['upward', 'left']:

            current_coordonates[1] -= 1
            pattern_placement[1] = 'up-right'
            

        elif pattern_placement == ['upward', 'up-right']:

            current_coordonates[0] -= 1
            current_coordonates[1] += 1
            pattern_placement[1] = 'left'


        elif pattern_placement == ['downward', 'left']:

            current_coordonates[1] -= 1
            pattern_placement[1] = 'down-right'       


        elif pattern_placement == ['downward', 'down-right']:

            current_coordonates[0] += 1
            current_coordonates[1] += 1
            pattern_placement[1] = 'left'    

        # changement du sens vertical : upward -> downward
        if  current_coordonates[0] == 0 and pattern_placement[1] == 'up-right':

            # le module courant est disponible
            if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
                
                # placement du bit courant
                # QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]
                QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = mask(mask_number, current_coordonates[0], current_coordonates[1], final_message[current_bit])

                # mise a jour du bit courant
                current_bit += 1
            
            pattern_placement = ['downward', 'left']

            # /!\ vertical timing pattern /!\
            if current_coordonates[1] != 7:
                current_coordonates[1] -= 1

            else:
                current_coordonates[1] -= 2


        # changement du sens vertical : downward -> upward
        if  current_coordonates[0] == QR_Code_size-1 and pattern_placement[1] == 'down-right':

            # le module courant est disponible
            if QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] == .5:
                
                # placement du bit courant
                # QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = final_message[current_bit]
                QR_Code_Matrix[current_coordonates[0],current_coordonates[1]] = mask(mask_number, current_coordonates[0], current_coordonates[1], final_message[current_bit])
                # mise a jour du bit courant
                current_bit += 1

            pattern_placement = ['upward', 'left']
            current_coordonates[1] -= 1
    
    return QR_Code_Matrix


def QR_Code_Matrix_generator(version, final_message, mask_pattern):
    
    # taille qr code
    # version = 7
    QR_Code_size = (((version-1)*4)+21)

    # data 
    QR_Code_Matrix = np.ones((QR_Code_size, QR_Code_size))*.5

    # FINDERS PATTERNS
    # matrice des finder pattern
    QR_Code_Matrix = finder_patterns_placement(QR_Code_Matrix)

    # SEPARATORS
    QR_Code_Matrix = separators_placement(QR_Code_Matrix)

    # ALIGNEMENT PATTERNS
    if version > 1:
        QR_Code_Matrix = alignement_patterns_placement(QR_Code_Matrix, QR_Code_size, version)

    # FORMAT INFORMATION AREA
    QR_Code_Matrix = format_information_areas_placement(QR_Code_Matrix)

    # VERSION INFORMATION AREA
    if version >= 7:
        QR_Code_Matrix = version_information_areas_placement(QR_Code_Matrix)

    # DARK MODULE
    QR_Code_Matrix[(4 * version) + 9, 8] = 1

    # TIMIING PATTERNS
    QR_Code_Matrix = timing_patterns_placement(QR_Code_Matrix, QR_Code_size)

    # DATA PLACEMENT
    QR_Code_Matrix = data_placement(QR_Code_Matrix, QR_Code_size, final_message, mask_pattern)

    return QR_Code_Matrix, QR_Code_size


def get_type_information_bits(EC_lvl, mask_pattern, df_Format_Information_Strings):

    type_information_bits = bitarray('000000000000000')
    type_information_bits[-len(bitarray(df_Format_Information_Strings.loc[EC_lvl, mask_pattern][0])):] = bitarray(df_Format_Information_Strings.loc[EC_lvl, mask_pattern][0])
    
    return type_information_bits


def get_version_information_string(version, df_Version_Information_Strings):

    version_information_string = bitarray('000000000000000000')
    version_information_string[-len(bitarray(df_Version_Information_Strings.loc[version][0])):] = bitarray(df_Version_Information_Strings.loc[version][0])

    return version_information_string
 

def type_information_bits_placement(QR_Code_Matrix, type_information_bits):

    # conversion en liste
    type_information_bits = type_information_bits.tolist()

    # haut-gauche
    QR_Code_Matrix[8,0:6] = type_information_bits[0:6]
    QR_Code_Matrix[8,7:9] = type_information_bits[6:8]
    QR_Code_Matrix[7,8] = type_information_bits[8]
    QR_Code_Matrix[0:6,8] = type_information_bits[9:][::-1]

    # haut-droit
    QR_Code_Matrix[8,-8:] = type_information_bits[-8:]

    # bas-gauche
    QR_Code_Matrix[-7:,8] = type_information_bits[0:7][::-1]

    return QR_Code_Matrix

def version_information_string_placement(QR_Code_Matrix, version_information_string):

    # 
    version_information_string = np.array(version_information_string.tolist()[::-1]).reshape(6, 3)

    # haut-droit
    QR_Code_Matrix[0:6, -11:-8] = version_information_string

    # bas-gauche
    QR_Code_Matrix[-11:-8,0:6] =  version_information_string.transpose()

    return QR_Code_Matrix

def render_QR_Code(QR_Code_Matrix):
    # AFFICHAGE
    fig, ax = plt.subplots()
    ax.imshow(QR_Code_Matrix, cmap='Greys')
    ax.set_aspect('equal')
    ax.axis("off")
    plt.show()