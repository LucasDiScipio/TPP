from bitarray import *
from fonctions import *

chaine = "test"
mode = "byte"
version = 1
liste = string_to_binary(chaine)

print(liste)

liste = add_mode_indicator(liste, mode)

print(liste)

liste = add_character_count_indicator(chaine, liste, mode, version)

print(liste)