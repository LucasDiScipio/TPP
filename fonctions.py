from bitarray import *

def string_to_binary(chaine):
    """ Encode les caracteres de la chaine en mots de 8 bits
    
    INPUT
    -----
    - chaine: une chaine de caracteres
    
    OUTPUT
    ------
    - encodage : liste contenant les mots de 8 bits qui encodent les caracteres
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
    - liste :
    - mode :

    Return
    ------
    - liste :
    """
    
    mode_indicators = {'numeric': bitarray('0001'), 
                       'alphanumeric': bitarray('0010'),
                       'byte': bitarray('0100'),
                       'kanji': bitarray('1000')}
    
    liste = [mode_indicators[mode]] + liste

    return liste


def add_character_count_indicator(chaine, liste, mode, version):

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