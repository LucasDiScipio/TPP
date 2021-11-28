from fonctions import get_version_information_string
from bitarray import bitarray
import pandas as pd

df_Version_Information_Strings = pd.read_csv("./data/Version Information Strings.csv", delimiter=';', index_col='Version').astype({"Version Information String": str})

# version : 7
def test_get_version_information_string_version_7():
    assert get_version_information_string(version=7, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('000111110010010100')

# version : 8
def test_get_version_information_string_version_8():
    assert get_version_information_string(version=8, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001000010110111100')

# version : 9
def test_get_version_information_string_version_9():
    assert get_version_information_string(version=9, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001001101010011001')

# version : 10
def test_get_version_information_string_version_10():
    assert get_version_information_string(version=10, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001010010011010011')

# version : 11
def test_get_version_information_string_version_11():
    assert get_version_information_string(version=11, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001011101111110110')

# version : 12
def test_get_version_information_string_version_12():
    assert get_version_information_string(version=12, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001100011101100010')

# version : 13
def test_get_version_information_string_version_13():
    assert get_version_information_string(version=13, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001101100001000111')

# version : 14
def test_get_version_information_string_version_14():
    assert get_version_information_string(version=14, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001110011000001101')

# version : 15
def test_get_version_information_string_version_15():
    assert get_version_information_string(version=15, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('001111100100101000')

# version : 16
def test_get_version_information_string_version_16():
    assert get_version_information_string(version=16, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010000101101111000')

# version : 17
def test_get_version_information_string_version_17():
    assert get_version_information_string(version=17, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010001010001011101')

# version : 18
def test_get_version_information_string_version_18():
    assert get_version_information_string(version=18, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010010101000010111')

# version : 19
def test_get_version_information_string_version_19():
    assert get_version_information_string(version=19, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010011010100110010')

# version : 20
def test_get_version_information_string_version_20():
    assert get_version_information_string(version=20, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010100100110100110')

# version : 21
def test_get_version_information_string_version_21():
    assert get_version_information_string(version=21, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010101011010000011')

# version : 22
def test_get_version_information_string_version_22():
    assert get_version_information_string(version=22, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010110100011001001')

# version : 23
def test_get_version_information_string_version_23():
    assert get_version_information_string(version=23, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('010111011111101100')

# version : 24
def test_get_version_information_string_version_24():
    assert get_version_information_string(version=24, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011000111011000100')

# version : 25
def test_get_version_information_string_version_25():
    assert get_version_information_string(version=25, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011001000111100001')

# version : 26
def test_get_version_information_string_version_26():
    assert get_version_information_string(version=26, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011010111110101011')

# version : 27
def test_get_version_information_string_version_27():
    assert get_version_information_string(version=27, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011011000010001110')

# version : 28
def test_get_version_information_string_version_28():
    assert get_version_information_string(version=28, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011100110000011010')

# version : 29
def test_get_version_information_string_version_29():
    assert get_version_information_string(version=29, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011101001100111111')

# version : 30
def test_get_version_information_string_version_30():
    assert get_version_information_string(version=30, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011110110101110101')

# version : 31
def test_get_version_information_string_version_31():
    assert get_version_information_string(version=31, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('011111001001010000')

# version : 32
def test_get_version_information_string_version_32():
    assert get_version_information_string(version=32, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100000100111010101')

# version : 33
def test_get_version_information_string_version_33():
    assert get_version_information_string(version=33, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100001011011110000')

# version : 34
def test_get_version_information_string_version_34():
    assert get_version_information_string(version=34, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100010100010111010')

# version : 35
def test_get_version_information_string_version_35():
    assert get_version_information_string(version=35, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100011011110011111')

# version : 36
def test_get_version_information_string_version_36():
    assert get_version_information_string(version=36, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100100101100001011')

# version : 37
def test_get_version_information_string_version_37():
    assert get_version_information_string(version=37, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100101010000101110')

# version : 38
def test_get_version_information_string_version_38():
    assert get_version_information_string(version=38, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100110101001100100')

# version : 39
def test_get_version_information_string_version_39():
    assert get_version_information_string(version=39, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('100111010101000001')

# version : 40
def test_get_version_information_string_version_40():
    assert get_version_information_string(version=40, df_Version_Information_Strings=df_Version_Information_Strings) == bitarray('101000110001101001')