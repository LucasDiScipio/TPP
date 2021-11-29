from fonctions import alphanumeric_mode_encoding
from bitarray import bitarray

def test_alphanumeric_mode_encoding_HELLOWORLD():
    assert alphanumeric_mode_encoding(chaine='HELLO WORLD') == [bitarray('01100001011'), bitarray('01111000110'), bitarray('10001011100'),
                                                                bitarray('10110111000'), bitarray('10011010100'), bitarray('001101')]