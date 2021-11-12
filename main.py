from fonctions import *
import pandas as pd
import numpy as np

# parametres pour la generation du QR code
chaine = "oui"
mode = "byte"
version = 1
EC_lvl = 'M'
version_and_EC_lvl = str(version) + '-' + EC_lvl

# generation des tables log et antilog
alpha_exponents = np.arange(256, dtype=np.uint8)
integers = np.zeros(256, dtype=np.uint8)
integers[0] = 1
for k in range(1,256):

    if integers[k-1]*2 > 255:
        integers[k] = int(integers[k-1]) * 2 ^ 285 

    else:
        integers[k] = integers[k-1] * 2

df_Antilog_table = pd.DataFrame(data=integers, columns=['integer'], index=alpha_exponents)
df_Antilog_table.index.name = 'exponent'
df_Log_table = pd.DataFrame(df_Antilog_table.index.values, columns=['exponent'], 
                            index=df_Antilog_table.integer).iloc[0:255, :].sort_index()


# encodage de la chaine de caracteres
data_codewords = data_encoding(chaine, mode, version, EC_lvl)

# separation des mots codes en groupes et blocs
groups_list = break_data_codewords_into_blocks(data_codewords, version, EC_lvl)

# polynome messager
block = groups_list[0].blocks_list[0]
message_polynomial = generate_message_polynomial(block)
print('message_polynomial :')
print(message_polynomial)

# polynome generateur
df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")
degree_generator_polynomial = int(df_Error_correction_table.loc[version_and_EC_lvl, 'EC Codewords Per Block'])
generator_polynomial = generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table)
print('generator_polynomial :')
print(generator_polynomial)


# division polynomiale

# degres des polynomes messager et generateur
degree_message_polynomial = len(message_polynomial)-1

print(degree_message_polynomial)
print(degree_generator_polynomial)