import numpy as np
import matplotlib.pyplot as plt
from sys import argv

num = int(argv[1])
filename = "files/file {0:03d}.txt".format(num)

with open (filename,'w') as f:
    # f.write("Hello from program number {0:2d}".format(num))
    for i in range(1,num+1):
        f.write(f"{i**2}")

print ("Progam ended successfully")