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
        encodage.append(format(ord(char),'b'))

        # ajout d'un bit nul en debut de byte si le caractere ne requiert que 7 bits pour etre encode
        while len(encodage[-1]) < 8:
            encodage[-1] = '0' + encodage[-1]
    
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
    
    mode_indicators = {'numeric': '0001', 
                       'alphanumeric': '0010',
                       'byte': '0100',
                       'kanji': '1000'}
    
    liste = [mode_indicators[mode]] + liste

    return liste