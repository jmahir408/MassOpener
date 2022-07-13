#github.com/jmahir408
#Read the README before using
import os
file_path = 'links.txt'

file = open(file_path, 'r')

for line in file:
    for link in line.split():
          os.system("open \"\" " + link)
file.close()

