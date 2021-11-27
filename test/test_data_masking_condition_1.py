from fonctions import data_masking_condition_1
import numpy as np

def test_data_masking_condition_1_row_score_0():
    assert data_masking_condition_1(np.array([0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]), 22) == 0

def test_data_masking_condition_1_row_score_3():
    assert data_masking_condition_1(np.array([0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]), 22) == 3

def test_data_masking_condition_1_row_score_4():
    assert data_masking_condition_1(np.array([0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]), 22) == 4

def test_data_masking_condition_1_row_score_10():
    assert data_masking_condition_1(np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]), 22) == 10

def test_data_masking_condition_1_column_score_0():
    assert data_masking_condition_1(np.array([0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]).reshape(22,1), 22) == 0

def test_data_masking_condition_1_column_score_3():
    assert data_masking_condition_1(np.array([0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]).reshape(22,1), 22) == 3

def test_data_masking_condition_1_column_score_4():
    assert data_masking_condition_1(np.array([0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0]).reshape(22,1), 22) == 4

def test_data_masking_condition_1_column_score_10():
    assert data_masking_condition_1(np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0]).reshape(22,1), 22) == 10