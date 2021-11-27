from fonctions import data_masking_condition_4
import numpy as np

def test_data_masking_condition_4():
    dark_modules = np.ones((1,213))
    white_modules = np.zeros((1,228))
    QR_Code_Matrix = np.append(dark_modules, white_modules).reshape((21,21))
    assert data_masking_condition_4(QR_Code_Matrix, QR_Code_size=21) == 0
