from fonctions import *

chaine = "oui"
mode = "byte"
version = 1
EC_lvl = 'Q'

data_codewords = data_encoding(chaine, mode, version, EC_lvl)

print(data_codewords)



