from fonctions import *
import pandas as pd
import numpy as np

# parametres pour la generation du QR code
chaine = "oui"
mode = "byte"
version = 7
EC_lvl = 'L'
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

# List of Versions and Required Remainder Bits
df_Versions_Required_Remainder_Bits = pd.read_csv("./data/Versions and Required Remainder Bits.csv", delimiter=';', index_col='QR Version')

# encodage de la chaine de caracteres
data_codewords = data_encoding(chaine, mode, version, EC_lvl)

# separation des mots codes en groupes et blocs
groups_list = break_data_codewords_into_blocks(data_codewords, version, EC_lvl)

# Format and Version String Tables
df_Version_Information_Strings = pd.read_csv("./data/Version Information Strings.csv", delimiter=';', index_col='Version').astype({"Version Information String": str})
df_Format_Information_Strings = pd.read_csv("./data/Format Information Strings.csv", delimiter=';', index_col = ['ECC Level',  'Mask Pattern']).astype({"Type Information Bits": str})

print(df_Version_Information_Strings)
print(df_Format_Information_Strings)

exit()

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

# ENTRELACEMENT ET MESSAGE FINAL
final_message = final_message_generator(version, version_and_EC_lvl, degree_generator_polynomial, groups_number, groups_list, df_Error_correction_table, df_Versions_Required_Remainder_Bits)

# GENERATION DU QR_CODE
QR_Code_Matrix, QR_Code_size = QR_Code_Matrix_generator(version, final_message)

# MEILLEUR MASK


# AFFICHAGE
render_QR_Code(QR_Code_Matrix, QR_Code_size)