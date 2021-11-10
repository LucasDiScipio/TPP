from fonctions import *
import pandas as pd
import numpy as np

# parametres pour la generation du QR code
chaine = "oui"
mode = "byte"
version = 1
EC_lvl = 'L'

# generation des tables log et antilog
alpha_exponents = np.arange(256)
integers = np.zeros(256)
integers[0] = 1
for k in range(1,256):

    if integers[k-1]*2 > 255:
        integers[k] = int(integers[k-1]) * 2 ^ 285 

    else:
        integers[k] = integers[k-1] * 2

df_antilog = pd.DataFrame(data=integers, columns=['integers'], index=alpha_exponents)
df_log = pd.DataFrame(df_antilog.index.values, index=df_antilog.integers).iloc[0:255, :]


# degre du polynome generateur
df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")
version_and_EC_lvl = str(version) + '-' + EC_lvl
degree = int(df_Error_correction_table.loc[version_and_EC_lvl, 'EC Codewords Per Block'])

# vecteur des coefficients du  polynome generateurs
coefficients = np.zeros(degree)

# x-2^0
coefficients[-1] = -(2**0)
coefficients[-2] = 2**0 


# (x-2^0)(x-2^1)...(x-2^n-1)
for i in range(1,degree):
    shifted_coefficients = np.zeros(degree)
    shifted_coefficients[0:-1] = coefficients[1:]
    coefficients = shifted_coefficients - (2**i)*coefficients