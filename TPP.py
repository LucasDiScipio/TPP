def string_to_binary(chaine):
    
    # liste des caracteres de la chaine encodes en binaire
    encodage = []

    # ajout du mot binaire correspondant a chacun des caracteres (norme ASCII)
    for char in chaine:
        encodage.append(format(ord(char),'b'))

    return encodage


