def string_to_binary(chaine):
    
    # liste des caracteres de la chaine encodes en binaire
    encodage = []

    for char in chaine:

        # ajout du mot binaire correspondant a chacun des caracteres (norme ASCII - Unicode)    
        encodage.append(format(ord(char),'b'))

        # ajout d'un bit nul en debut de byte si le caractere ne requiert que 7 bits pour etre encode
        if len(encodage[-1]) == 7:
            encodage[-1] = '0' + encodage[-1]
    
    return encodage