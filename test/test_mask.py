from fonctions import mask

# mask(mask_number, row, column, bit)
# mask 0 : (row + column) mod 2 == 0
def test_mask_0_no_switch():
    assert mask(mask_number=0, row=0, column=3, bit=1) == 1 and mask(mask_number=0, row=0, column=3, bit=0) == 0

def test_mask_0_switch():
    assert mask(mask_number=0, row=0, column=4, bit=1) == 0 and mask(mask_number=0, row=0, column=4, bit=0) == 1

# mask 1 : (row) mod 2 == 0
def test_mask_1_no_switch():
    assert mask(mask_number=1, row=1, column=0, bit=1) == 1 and mask(mask_number=1, row=1, column=0, bit=0) == 0

def test_mask_1_switch():
    assert mask(mask_number=1, row=0, column=0, bit=1) == 0 and mask(mask_number=1, row=0, column=0, bit=0) == 1

# mask 2 : (column) mod 3 == 0
def test_mask_2_no_switch():
    assert mask(mask_number=2, row=0, column=1, bit=1) == 1 and mask(mask_number=2, row=0, column=1, bit=0) == 0

def test_mask_2_switch():
    assert mask(mask_number=2, row=0, column=3, bit=1) == 0 and mask(mask_number=2, row=0, column=3, bit=0) == 1

# mask 3 : (row + column) mod 3 == 0
def test_mask_3_no_switch():
    assert mask(mask_number=3, row=0, column=1, bit=1) == 1 and mask(mask_number=3, row=0, column=1, bit=0) == 0

def test_mask_3_switch():
    assert mask(mask_number=3, row=1, column=2, bit=1) == 0 and mask(mask_number=3, row=0, column=3, bit=0) == 1

# mask 4 : (floor(row / 2) + floor(column / 3)) mod 2 == 0
def test_mask_4_no_switch():
    assert mask(mask_number=4, row=2, column=0, bit=1) == 1 and mask(mask_number=4, row=2, column=0, bit=0) == 0

def test_mask_4_switch():
    assert mask(mask_number=4, row=2, column=3, bit=1) == 0 and mask(mask_number=4, row=2, column=3, bit=0) == 1

# mask 5 : ((row * column) mod 2) + ((row * column) mod 3) == 0
def test_mask_5_no_switch():
    assert mask(mask_number=5, row=1, column=1, bit=1) == 1 and mask(mask_number=5, row=1, column=1, bit=0) == 0

def test_mask_5_switch():
    assert mask(mask_number=5, row=0, column=0, bit=1) == 0 and mask(mask_number=5, row=0, column=0, bit=0) == 1

# mask 6 : (((row * column) mod 2) + ((row * column) mod 3)) mod 2 == 0
def test_mask_6_no_switch():
    assert mask(mask_number=6, row=1, column=3, bit=1) == 1 and mask(mask_number=6, row=1, column=3, bit=0) == 0

def test_mask_6_switch():
    assert mask(mask_number=6, row=0, column=0, bit=1) == 0 and mask(mask_number=6, row=0, column=0, bit=0) == 1

# mask 7 : (((row + column) mod 2) + ((row * column) mod 3)) mod 2 == 0
def test_mask_7_no_switch():
    assert mask(mask_number=7, row=0, column=3, bit=1) == 1 and mask(mask_number=7, row=0, column=3, bit=0) == 0

def test_mask_7_switch():
    assert mask(mask_number=7, row=0, column=0, bit=1) == 0 and mask(mask_number=7, row=0, column=0, bit=0) == 1