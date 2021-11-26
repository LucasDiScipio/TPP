from fonctions import EC_codewords_generator
import numpy as np
import pandas as pd

# generation des tables log et antilog
alpha_exponents = np.arange(256, dtype=np.uint8)
integers = np.zeros(256, dtype=np.uint8)
integers[0] = 1
for k in range(1,256):

    if integers[k-1]*2 > 255:
        integers[k] = int(integers[k-1]) * 2 ^ 285 

    else:
        integers[k] = integers[k-1] * 2

df_Antilog_table = pd.DataFrame(data=integers, columns=['integer'], index=alpha_exponents)
df_Antilog_table.index.name = 'exponent'
df_Log_table = pd.DataFrame(df_Antilog_table.index.values, columns=['exponent'], index=df_Antilog_table.integer).iloc[0:255, :].sort_index()

# TEST: EC_codewords_generator(message_polynomial, generator_polynomial, df_Antilog_table, df_Log_table)
def test_EC_codewords_generator_1():
    message_polynomial = np.array([32,91,11,120,209,114,220,77,67,64,236,17,236])
    generator_polynomial = np.array([0,74,152,176,100,86,100,106,104,130,218,206,140,78])
    EC_codewords = EC_codewords_generator(message_polynomial, generator_polynomial, df_Antilog_table, df_Log_table)
    assert np.array_equal(EC_codewords, np.array([168,72,22,82,217,54,156,0,46,15,180,122,16]))
