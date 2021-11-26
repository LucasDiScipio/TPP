from fonctions import generate_generator_polynomial
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


# TEST: generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table)

# 2 error correction codewords : α^0*x^2 + α^25*x^1 + α^1*x^0
def test_generate_generator_polynomial_degree_2():
    degree_generator_polynomial=2
    assert np.array_equal(generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table), np.array([0,25,1]))

# 3 error correction codewords : α^0*x^3 + α^198*x^2 + α^199*x^1 + α^3*x^0
def test_generate_generator_polynomial_degree_3():
    degree_generator_polynomial=3
    assert np.array_equal(generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table), np.array([0,198,199,3]))

# 7 error correction codewords : α^0*x^7 + α^87*x^6 + α^229*x^5 + α^146*x^4 + α^149*x^3 + α^238*x^2 + α^102*x^1 + α^21*x^0
def test_generate_generator_polynomial_degree_7():
    degree_generator_polynomial=7
    assert np.array_equal(generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table), 
                          np.array([0,87,229,146,149,238,102,21]))

# 30 error correction codewords : 
# α^0*x^30 + α^41*x^29 + α^173*x^28 + α^145*x^27 + α^152*x^26 + α^216*x^25 + α^31*x^24 + α^179*x^23 + α^182*x^22 + α^50*x^21 + α^48*x^20 
# + α^110*x^19 + α^86*x^18 + α^239*x^17 + α^96*x^16 + α^222*x^15 + α^125*x^14 + α^42*x^13 + α^173*x^12 + α^226*x^11 + α^193*x^10 
# + α^224*x^9 + α^130*x^8 + α^156*x^7 + α^37*x^6 + α^251*x^5 + α^216*x^4 + α^238*x^3 + α^40*x^2 + α^192*x^1 + α^180*x^0
def test_generate_generator_polynomial_degree_30():
    degree_generator_polynomial=30
    assert np.array_equal(generate_generator_polynomial(degree_generator_polynomial, df_Antilog_table, df_Log_table), 
                          np.array([0,41,173,145,152,216,31,179,182,50,48,110,86,239,96,222,125,42,173,226,193,224,130,156,37,251,216,238,40,192,180]))