from fonctions import *
from numpy.polynomial import Polynomial
import pandas as pd

chaine = "oui"
mode = "byte"
version = 1
EC_lvl = 'Q'

# degre du polynome generateur
df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")
version_and_EC_lvl = str(version) + '-' + EC_lvl
degree = int(df_Error_correction_table.loc[version_and_EC_lvl, 'EC Codewords Per Block'] - 1)




print(p.coef)




