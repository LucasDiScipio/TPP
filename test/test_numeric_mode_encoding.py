from fonctions import numeric_mode_encoding
from bitarray import bitarray

def test_numeric_mode_encoding_8675309():
    assert numeric_mode_encoding(chaine='8675309') == [bitarray('1101100011 '), bitarray('1000010010'), bitarray('1001')]