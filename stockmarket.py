import numpy as np
import sys

if len(sys.argv)==1:
    print("Please indicate input file")
    exit()
inputfile = sys.argv[1]
print(f"The input file is: {inputfile}")

outputfile = "output.txt"
if len(sys.argv)==3:
    outputfile = sys.argv[2]

file = open(inputfile, "r+")
datastring = file.readlines()
data = np.array([])

for line in datastring:
    number = line.split("\n")[0]
    data = np.append(data, int(number))
print(data)