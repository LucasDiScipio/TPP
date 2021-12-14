# import OS module
import os

# Get the list of all files and directories
path = "C:/Users/lucas/Documents/Facc/TPP/QRCODES"
dir_list = os.listdir(path)

# missing QRCODES
missing_QRCODES = []
for i in range(0,10000):
    
    if not("QRCODE_#{0:05d}.png".format(i) in dir_list):

        missing_QRCODES.append("QRCODE_#{0:05d}.png".format(i))


# fichier texte
with open("QRCODES_manquants_1.txt", "w") as f:

    for element in missing_QRCODES:

        f.write(element + "\n")

