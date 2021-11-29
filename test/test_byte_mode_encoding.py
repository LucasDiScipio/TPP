from fonctions import byte_mode_encoding
from bitarray import bitarray

def test_byte_mode_encoding():
    assert byte_mode_encoding(chaine='Hello, world!') == [bitarray('01001000'), bitarray('01100101'), bitarray('01101100'), bitarray('01101100'), 
                                                          bitarray('01101111'), bitarray('00101100'), bitarray('00100000'), bitarray('01110111'),
                                                          bitarray('01101111'), bitarray('01110010'), bitarray('01101100'), bitarray('01100100'),
                                                          bitarray('00100001')]