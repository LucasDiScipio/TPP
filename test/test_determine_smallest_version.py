from fonctions import determine_smallest_version

def test_determine_smallest_version_HELLO_WORLD_Q():
    assert determine_smallest_version(chaine='HELLO WORLD', EC_lvl='Q', mode='alphanumeric') == 1

def test_determine_smallest_version_HELLO_DISNEY_WORLD_Q():
    assert determine_smallest_version(chaine='HELLO DISNEY WORLD', EC_lvl='Q', mode='alphanumeric') == 2