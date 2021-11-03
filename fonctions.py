from classes import *
from bitarray import *
from bitarray.util import ba2int
from numpy.polynomial import Polynomial
import numpy as np
import pandas as pd

def string_to_binary(chaine):
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


def add_mode_indicator(liste, mode):
    """ Ajoute le mode d'encodage au debut de liste
    INPUTS
    ------
    - liste : type -> list, une liste de mots binaires 
    - mode : type -> string, le mode d'encodage (numerique, alphanumerique, byte ou kanji)

    Return
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

    Return
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

    Return
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
        liste = liste + [(bits_number % 8)*bitarray('0')]
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

    Return
    ------
    - data_codewords : type -> bitarray, les mots codes binaires encodes et concatenes
    """

    liste = string_to_binary(chaine)
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

    Return
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
        #print("group: " + str(i+1))
        blocks_number = int(df_Error_correction_table.loc[version_and_EC_lvl, 'Number of Blocks in Group ' + str(i+1)])
        blocks_list = []

        # separation en blocs
        for j in range(0, blocks_number):
            #print('block: ' + str(j+1))
            data_codewords_number = int(df_Error_correction_table.loc[version_and_EC_lvl, "Number of Data Codewords in Each of Group " + str(j+1) + "'s Blocks"])
            codewords_list = []

            # separation en mots-codes
            for k in range(0, data_codewords_number):

                # ajout du mot code courant
                codeword = data_codewords[compteur:compteur+7]
                codewords_list.append(codeword)
                
                compteur += 8
            
            # ajout du bloc courant a la liste de blocs
            blocks_list.append(Block(codewords_list, []))
        
        groups_list.append(Group(blocks_list))
    
    return groups_list


def generate_message_polynomial(block):
    """ genere le polynome messager correspondant au bloc donne en argument
    block : type -> Block, le bloc reprenant les mots codes qui serviront de coefficients au polynome messager
    """

    # recuperation des mots codes
    codewords_list = block.codewords_list

    # liste des coefficients du polynome messager
    coefficients_list = []
    for codeword in codewords_list:
        coefficients_list.append(ba2int(codeword))
    coefficients_list.reverse()

    # generation du polynome messager
    message_polynomial = Polynomial(coefficients_list)

    return message_polynomial