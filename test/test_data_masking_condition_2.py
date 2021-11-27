from fonctions import data_masking_condition_2
import numpy as np

def test_data_masking_condition_2_score_0():
    assert data_masking_condition_2(np.array([0,0,0,1]).reshape(2,2)) == 0

def test_data_masking_condition_2_score_3_zeros():
    assert data_masking_condition_2(np.zeros((2,2))) == 3

def test_data_masking_condition_2_score_3_ones():
    assert data_masking_condition_2(np.ones((2,2))) == 3