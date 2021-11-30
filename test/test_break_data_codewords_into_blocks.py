from fonctions import break_data_codewords_into_blocks
from bitarray import bitarray

# mots codes a decomposer
data_codewords  = bitarray('01000011 01010101 01000110 10000110 01010111 00100110 01010101 11000010 01110111 00110010')
data_codewords += bitarray('00000110 00010010 00000110 01100111 00100110 11110110 11110110 01000010 00000111 01110110')
data_codewords += bitarray('10000110 11110010 00000111 00100110 01010110 00010110 11000110 11000111 10010010 00000110')
data_codewords += bitarray('10110110 11100110 11110111 01110111 00110010 00000111 01110110 10000110 01010111 00100110')
data_codewords += bitarray('01010010 00000110 10000110 10010111 00110010 00000111 01000110 11110111 01110110 01010110')
data_codewords += bitarray('11000010 00000110 10010111 00110010 11100000 11101100 00010001 11101100 00010001 11101100')
data_codewords += bitarray('00010001 11101100')

def test_break_data_codewords_into_blocks_thonky_5Q_group1_block1():
     correct_codewords_list = [bitarray('01000011'), bitarray('01010101'), bitarray('01000110'), bitarray('10000110'), 
                                   bitarray('01010111'), bitarray('00100110'), bitarray('01010101'), bitarray('11000010'), 
                                   bitarray('01110111'), bitarray('00110010'), bitarray('00000110'), bitarray('00010010'), 
                                   bitarray('00000110'), bitarray('01100111'), bitarray('00100110')]
     
     groups_list = break_data_codewords_into_blocks(data_codewords=data_codewords, version=5, EC_lvl='Q')

     assert groups_list[0].blocks_list[0].codewords_list == correct_codewords_list
