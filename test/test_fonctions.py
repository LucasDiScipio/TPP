from fonctions import *

# add_mode_indicator(liste, mode)
def test_add_mode_indicator_return_numeric():
    output = add_mode_indicator([], mode='numeric')
    assert output[0] == bitarray('0001')

def test_add_mode_indicator_return_alphanumeric():
    output = add_mode_indicator([], mode='alphanumeric')
    assert output[0] == bitarray('0010')

def test_add_mode_indicator_return_byte():
    output = add_mode_indicator([], mode='byte')
    assert output[0] == bitarray('0100')

def test_add_mode_indicator_return_kanji():
    output = add_mode_indicator([], mode='kanji')
    assert output[0] == bitarray('1000')


# add_character_count_indicator(chaine, liste, mode, version)
