from tables import *
from fonctions import *
from bitarray import *

# parametres pour la generation du QR code
chaine = "gang"
EC_lvl = 'L'
mode = choose_most_efficient_mode(chaine)
version = determine_smallest_version(chaine, EC_lvl, mode)
version_and_EC_lvl = f"{version}-{EC_lvl}"

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

# ENTRELACEMENT ET MESSAGE FINAL
final_message = final_message_generator(version, version_and_EC_lvl, degree_generator_polynomial, groups_number, groups_list, df_Error_correction_table, df_Versions_Required_Remainder_Bits)
    
# boucle sur les mask pattern
for mask_pattern in range(0,8):

    # GENERATION DU QR_CODE
    QR_Code_Matrix, QR_Code_size = QR_Code_Matrix_generator(version, final_message, mask_pattern)

    # FORMAT AND VERSION INFORMATION PLACEMENT
    # type information bits placement  
    type_information_bits = get_type_information_bits(EC_lvl, mask_pattern, df_Format_Information_Strings)
    QR_Code_Matrix = type_information_bits_placement(QR_Code_Matrix, type_information_bits)

    # version information string placement
    if version >= 7:
        version_information_string = get_version_information_string(version, df_Version_Information_Strings)
        QR_Code_Matrix = version_information_string_placement(QR_Code_Matrix, version_information_string)

    # evaluation du mask pattern courant
    QR_Code_Matrix_score = compute_penalty_score(QR_Code_Matrix, QR_Code_size)

    if mask_pattern > 0 and QR_Code_Matrix_score < QR_Code_Matrix_final_score :
        QR_Code_Matrix_final_score = QR_Code_Matrix_score
        QR_Code_Matrix_final = QR_Code_Matrix        

    elif mask_pattern == 0:
        QR_Code_Matrix_final_score = QR_Code_Matrix_score
        QR_Code_Matrix_final = QR_Code_Matrix

# AFFICHAGE
render_QR_Code(QR_Code_Matrix_final)