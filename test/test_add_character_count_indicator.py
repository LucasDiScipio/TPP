from fonctions import add_character_count_indicator
from bitarray import bitarray

def test_add_character_count_indicator_alphanumeric_HELLOWORLD():
    assert add_character_count_indicator(chaine='HELLO WORLD', liste=[], mode='alphanumeric', version=1) == [bitarray('000001011')]