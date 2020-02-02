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
#print(data)

# theList = np.arange(16)
# np.random.shuffle(theList)
# print(theList)
theList = data
# np.array([15, 10, 0, 8, 2, 3, 1, 9, 14, 4, 13, 5, 7, 11, 6, 12])
print(f"The list is {theList}")

def split(arr, l, r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = int((l + (r - 1)) / 2)

        # Sort first and second halves
        lbn, lbi = split(arr, l, m)
        #print(f"lbn is: {lbn}")
        rbn, rbi = split(arr, m+1, r)
        #print(f"right side length is: {r - m}")
        #print(f"rbn is: {rbn}")
        return merge(arr, l, m, r, lbi, lbn, rbi, rbn)
    else:
        return(1,l)

def merge(arr, l, m, r, lbi, lbn, rbi, rbn):
    mbn = -1
    mbi = -1
    if arr[m]>arr[m+1]:
        mbn = 1
        mbi = m
    else:
        i = m
        while(i>l and arr[i-1]<=arr[i]):
            i-=1
        j = m+1
        while(j<r and arr[j+1]>=arr[j]):
            j+=1
        #print(f"i is {i}; j is {j}")
        mbn = j-abs(i)+1
        mbi = i

    print(f"{lbn,mbn,rbn}")
    bn = max(mbn, lbn, rbn)
    bi = -1
    if bn==lbn:
        bi = lbi
    elif bn==rbn:
        bi = rbi
    else:
        bi = mbi
    print(f"length is {r-l+1}")
    print(f"bn and bi are: {bn,bi}")
    return(bn, bi)

bestList = np.array([])
print(split(theList, 0, len(theList)-1))

