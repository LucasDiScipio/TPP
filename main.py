from fonctions import *
import pandas as pd
import numpy as np

# parametres pour la generation du QR code
chaine = "test"
mode = "byte"
version = 5
EC_lvl = 'Q'
version_and_EC_lvl = str(version) + '-' + EC_lvl

# Error Correction Table
df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")

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
df_Log_table = pd.DataFrame(df_Antilog_table.index.values, columns=['exponent'], index=df_Antilog_table.integer).iloc[0:255, :].sort_index()

# encodage de la chaine de caracteres
data_codewords = data_encoding(chaine, mode, version, EC_lvl)

# separation des mots codes en groupes et blocs
groups_list = break_data_codewords_into_blocks(data_codewords, version, EC_lvl)

# GENERATION DES MOTS CORRECTEURS
# groupe courant
groups_number = len(groups_list)
for i in range(0,groups_number):

    # bloc courant
    for j in range(len(groups_list[i].blocks_list)):
        
        # polynome messager
        block = groups_list[i].blocks_list[j]
        message_polynomial = generate_message_polynomial(block)

        # polynome generateur
        degree_generator_polynomial = int(df_Error_correction_table.loc[version_and_EC_lvl, 'EC Codewords Per Block'])
        generator_polynomial = generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table)

        # mots correcteurs
        groups_list[i].blocks_list[j].EC_codewords_list = EC_codewords_generator(message_polynomial, generator_polynomial, df_Antilog_table, df_Log_table)


# ENTRELACEMENT
final_message = []

# nombre total de blocs
blocks_total_number = 0
for i in range(1,groups_number+1):
    blocks_total_number += int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Blocks in Group {i}"])

# longueur max des mots codes
codewords_max_size = int(df_Error_correction_table.loc[version_and_EC_lvl, f"Number of Data Codewords in Each of Group {groups_number}'s Blocks"])

# matrice des mots codes (-1 -> valeur manquante)
codewords_matrix = np.ones((blocks_total_number,codewords_max_size), dtype=np.uint8)*(-1)

# matrice des mots correcteurs
EC_codewords_matrix = np.zeros((blocks_total_number, degree_generator_polynomial), dtype=np.uint8)

# groupe courant
index = 0
for i in range(0,groups_number):

    # bloc courant
    for j in range(0,len(groups_list[i].blocks_list)):
        
        for k in range(0,len(groups_list[i].blocks_list[j].codewords_list)):

            codewords_matrix[index,k] = ba2int(groups_list[i].blocks_list[j].codewords_list[k])
        
        EC_codewords_matrix[index] = groups_list[i].blocks_list[j].EC_codewords_list

        index += 1

print(codewords_matrix)
print(EC_codewords_matrix)

# entrelacement des mots codes
for i in range(0,codewords_matrix.shape[1]):

    for j in range(0, codewords_matrix.shape[0]):

        if codewords_matrix[j,i] != -1:

            final_message.append(codewords_matrix[j,i])

# entrelacement des mots correcteurs
for i in range(0, EC_codewords_matrix.shape[1]):

    for j in range(0, EC_codewords_matrix.shape[0]):

        final_message.append(EC_codewords_matrix[j,i])

# conversion du message final en notation binaire


# ajouts d'eventuels bits nuls 

print(final_message)