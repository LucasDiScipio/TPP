from fonctions import *

chaine = "exemple"
mode = "alphanumeric"
version = 1
EC_lvl = 'Q'

liste = string_to_binary(chaine)

print(liste)

liste = add_mode_indicator(liste, mode)

print(liste)

liste = add_character_count_indicator(chaine, liste, mode, version)

print(liste)

liste = add_terminator_padBytes(liste, version, EC_lvl)

print(liste)

