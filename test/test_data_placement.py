from fonctions import data_placement
import numpy as np

def test_data_placement_correct_pattern():
    Correct_Matrix = np.ones(64, np.int32)
    Correct_Matrix[::2] = 0
    Correct_Matrix = Correct_Matrix.reshape(8,8)
    
    QR_Code_Matrix = (np.ones(64)*.5).reshape((8,8))
    final_message = np.zeros(64)
    final_message[::2] = 1
    QR_Code_size = 8
    mask_number = -1

    assert np.array_equal(Correct_Matrix, data_placement(QR_Code_Matrix, QR_Code_size, final_message, mask_number))
