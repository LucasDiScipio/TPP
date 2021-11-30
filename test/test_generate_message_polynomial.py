from fonctions import generate_message_polynomial
from bitarray import bitarray
from classes import Block
import numpy as np

def test_generate_message_polynomial():

    codewords_list = [bitarray('01000011'), bitarray('01010101'), bitarray('01000110'), bitarray('10000110'), 
                      bitarray('01010111'), bitarray('00100110'), bitarray('01010101'), bitarray('11000010'), 
                      bitarray('01110111'), bitarray('00110010'), bitarray('00000110'), bitarray('00010010'), 
                      bitarray('00000110'), bitarray('01100111'), bitarray('00100110')]

    block = Block(codewords_list, EC_codewords_list=[])
    
    correct_message_polynomial = np.array([67,85,70,134,87,38,85,194,119,50,6,18,6,103,38])

    assert np.array_equal(generate_message_polynomial(block),correct_message_polynomial)

