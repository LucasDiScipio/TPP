from fonctions import *

chaine = ""
mode = "byte"
version = 1
EC_lvl = 'L'

liste = string_to_binary(chaine)

print(liste)

liste = add_mode_indicator(liste, mode)

print(liste)

liste = add_character_count_indicator(chaine, liste, mode, version)

print(liste)

liste = add_terminator(liste, version, EC_lvl)

print(liste)

