from fonctions import generate_message_polynomial
from classes import Block

# generate_message_polynomial(block)
def test_generate_message_polynomial():
    codewords_list = []
    EC_codewords_list = []
    block = Block(codewords_list, EC_codewords_list)