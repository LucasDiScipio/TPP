from fonctions import *

def test_string_to_binary_return_type():
    assert isinstance(string_to_binary("test"), list)

def test_add_mode_indicator_return_type_numeric():
    assert isinstance(add_mode_indicator([], mode='numeric'), list)

def test_add_mode_indicator_return_type_alphanumeric():
    assert isinstance(add_mode_indicator([], mode='alphanumeric'), list)

def test_add_mode_indicator_return_type_byte():
    assert isinstance(add_mode_indicator([], mode='byte'), list)

def test_add_mode_indicator_return_type_kanji():
    assert isinstance(add_mode_indicator([], mode='kanji'), list)