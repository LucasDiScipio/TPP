from fonctions import choose_most_efficient_mode

def test_choose_most_efficient_mode_numeric():
    assert choose_most_efficient_mode(chaine='0123456789') == 'numeric'

def test_choose_most_efficient_mode_alphanumeric():
    assert choose_most_efficient_mode(chaine='A0123456789') == 'alphanumeric'