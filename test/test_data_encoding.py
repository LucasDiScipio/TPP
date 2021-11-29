from fonctions import data_encoding
from bitarray import bitarray

def test_data_encoding_alphanumeric_HELLOWORLD():
    assert data_encoding(chaine='HELLO WORLD', mode='alphanumeric', version=1, EC_lvl='Q') == bitarray('00100000010110110000101101111000110100010111001011011100010011010100001101000000111011000001000111101100')
    