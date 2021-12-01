import pandas as pd
import numpy as np

# Error Correction Table
df_Error_correction_table = pd.read_csv("./data/Error Correction Table.csv", index_col="Version and EC Level")

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

# List of Versions and Required Remainder Bits
df_Versions_Required_Remainder_Bits = pd.read_csv("./data/Versions and Required Remainder Bits.csv", delimiter=';', index_col='QR Version')

# Format and Version String Tables
df_Format_Information_Strings = pd.read_csv("./data/Format Information Strings.csv", delimiter=';', index_col = ['ECC Level',  'Mask Pattern']).astype({"Type Information Bits": str})
df_Version_Information_Strings = pd.read_csv("./data/Version Information Strings.csv", delimiter=';', index_col='Version').astype({"Version Information String": str})