from fonctions import choose_most_efficient_mode

def test_choose_most_efficient_mode_numeric():
    assert choose_most_efficient_mode(chaine='0123456789') == 'numeric'

def test_choose_most_efficient_mode_alphanumeric():
    assert choose_most_efficient_mode(chaine='A0123456789') == 'alphanumeric'

def test_choose_most_efficient_mode_byte():
    assert choose_most_efficient_mode(chaine='https://faculty.evansville.edu/ck6/encyclopedia/ETC.html') == 'byte'