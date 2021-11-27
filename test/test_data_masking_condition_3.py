from fonctions import data_masking_condition_3
import numpy as np

def test_data_masking_condition_3_score_0():
    assert data_masking_condition_3(np.zeros((1,11))) == 0

def test_data_masking_condition_3_score_40():
    assert data_masking_condition_3(np.array([1,0,1,1,1,0,1,0,0,0,0])) == 40

def test_data_masking_condition_3_score_40_reversed():
    assert data_masking_condition_3(np.array([0,0,0,0,1,0,1,1,1,0,1])) == 40
