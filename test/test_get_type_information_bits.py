from fonctions import get_type_information_bits
from bitarray import *
import pandas as pd

df_Format_Information_Strings = pd.read_csv("./data/Format Information Strings.csv", delimiter=';', index_col = ['ECC Level',  'Mask Pattern']).astype({"Type Information Bits": str})

# ECC Level : L - Mask Pattern : 0
def test_get_type_information_bits_L0():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=0, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('111011111000100')

# ECC Level : L - Mask Pattern : 1
def test_get_type_information_bits_L1():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=1, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('111001011110011')
    
# ECC Level : L - Mask Pattern : 2
def test_get_type_information_bits_L2():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=2, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('111110110101010')

# ECC Level : L - Mask Pattern : 3
def test_get_type_information_bits_L3():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=3, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('111100010011101')

# ECC Level : L - Mask Pattern : 4
def test_get_type_information_bits_L4():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=4, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('110011000101111')

# ECC Level : L - Mask Pattern : 5
def test_get_type_information_bits_L5():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=5, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('110001100011000')

# ECC Level : L - Mask Pattern : 6
def test_get_type_information_bits_L6():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=6, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('110110001000001')

# ECC Level : L - Mask Pattern : 7
def test_get_type_information_bits_L7():
    assert get_type_information_bits(EC_lvl='L', mask_pattern=7, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('110100101110110')

# ECC Level : M - Mask Pattern : 0
def test_get_type_information_bits_M0():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=0, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('101010000010010')

# ECC Level : M - Mask Pattern : 1
def test_get_type_information_bits_M1():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=1, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('101000100100101')
    
# ECC Level : M - Mask Pattern : 2
def test_get_type_information_bits_M2():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=2, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('101111001111100')

# ECC Level : M - Mask Pattern : 3
def test_get_type_information_bits_M3():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=3, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('101101101001011')

# ECC Level : M - Mask Pattern : 4
def test_get_type_information_bits_M4():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=4, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('100010111111001')

# ECC Level : M - Mask Pattern : 5
def test_get_type_information_bits_M5():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=5, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('100000011001110')

# ECC Level : M - Mask Pattern : 6
def test_get_type_information_bits_M6():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=6, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('100111110010111')

# ECC Level : M - Mask Pattern : 7
def test_get_type_information_bits_M7():
    assert get_type_information_bits(EC_lvl='M', mask_pattern=7, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('100101010100000')

# ECC Level : Q - Mask Pattern : 0
def test_get_type_information_bits_Q0():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=0, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('011010101011111')

# ECC Level : Q - Mask Pattern : 1
def test_get_type_information_bits_Q1():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=1, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('011000001101000')
    
# ECC Level : Q - Mask Pattern : 2
def test_get_type_information_bits_Q2():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=2, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('011111100110001')

# ECC Level : Q - Mask Pattern : 3
def test_get_type_information_bits_Q3():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=3, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('011101000000110')

# ECC Level : Q - Mask Pattern : 4
def test_get_type_information_bits_Q4():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=4, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('010010010110100')

# ECC Level : Q - Mask Pattern : 5
def test_get_type_information_bits_Q5():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=5, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('010000110000011')

# ECC Level : Q - Mask Pattern : 6
def test_get_type_information_bits_Q6():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=6, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('010111011011010')

# ECC Level : Q - Mask Pattern : 7
def test_get_type_information_bits_Q7():
    assert get_type_information_bits(EC_lvl='Q', mask_pattern=7, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('010101111101101')

# ECC Level : H - Mask Pattern : 0
def test_get_type_information_bits_H0():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=0, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('001011010001001')

# ECC Level : H - Mask Pattern : 1
def test_get_type_information_bits_H1():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=1, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('001001110111110')
    
# ECC Level : H - Mask Pattern : 2
def test_get_type_information_bits_H2():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=2, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('001110011100111')

# ECC Level : H - Mask Pattern : 3
def test_get_type_information_bits_H3():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=3, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('001100111010000')

# ECC Level : H - Mask Pattern : 4
def test_get_type_information_bits_H4():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=4, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('000011101100010')

# ECC Level : H - Mask Pattern : 5
def test_get_type_information_bits_H5():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=5, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('000001001010101')

# ECC Level : H - Mask Pattern : 6
def test_get_type_information_bits_H6():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=6, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('000110100001100')

# ECC Level : H - Mask Pattern : 7
def test_get_type_information_bits_H7():
    assert get_type_information_bits(EC_lvl='H', mask_pattern=7, df_Format_Information_Strings=df_Format_Information_Strings) == bitarray('000100000111011')