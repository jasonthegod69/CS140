# Boyuan(Jack) Chen  &  Jason Phillips
# 2020/03/10 Tuesday
# The code comprises of two parts: the main file, where you run the code; and the
# toolkit file, where the functions are stored. We have explanary comments in both
# files.
from toolkit import *

#Prompts user to type in input file and output file.
fName = input("Enter input file name: ")
oName = input("Enter output file name: ")
f = open(fName, 'r')
numBlocks = int(f.readline())
blockArray = []
maxL = 0

# ------ Read in the input file ------
for line in f:
  if numBlocks==0:
    break
  aBlock = line.split()
  aBlock[0] = int(aBlock[0])
  aBlock[1] = int(aBlock[1])
  aBlock[2] = int(aBlock[2])
  if maxL < max(aBlock):
    maxL = max(aBlock)
  blockArray.append(aBlock)
  numBlocks-=1

# ------ Get the sorted, clean, combination list ------
# Find all combinations of edge length all the objects. Put them in a single array
all_combs    = get_all_combinations(blockArray)
print("All combinations are: ")
print(all_combs)
print()
# Delete ones that are repetitive and each comb that [0]<[1].
# Say we have [3,5,7], then we would delete [5,3,7], because it is symmetric
clean_combs  = clean_repetitive_and_reverse(all_combs)
print("After deleting the reverse and repetitives: ")
print(clean_combs)
print()
# Sort in ascending order of [0]. If same, sort in [1].
# Note that you have to build a tower in the sequence of this array.
# There is no repetition or missing possibilities.
sorted_combs = sort_in_x(clean_combs)
print("After sorting in terms of the first entry: ")
print(sorted_combs)
print()

# ------ Build Dynamic Table ------
# Build dynamic table of each of the sorted_combs. The value means "The greatest
# height you can get up to this block". For each new block, check the previous blocks
# that are "clearly smaller"(see toolkit) than the current one, and find the maximum;
# then, add the previous height with its own height.
DP = build_dynamic_table(sorted_combs)
print("\n Running... \n\n")
print("Dynamic table: ")
print(DP)

# Using the trace back method described in toolkit, traces back the blocks that were
# used to build the maximum height.
max_height = max_DP(DP)
trace_back = traceBack(max_height, DP)
print()
print("Trace back: ")
print(trace_back)
print()
print()

# ------ Print and output the answers ------
print("-------- Answers -------")
print(f"\nThe tallest tower has {len(trace_back)} blocks and a height of {max_height[0]}")
blocks = []
for i in trace_back:
  blocks.append(sorted_combs[i])
print()
o = open(oFile, "w+")
o.write(str(len(trace_back))+"\n")
print("The tallest build is: ")
for block in blocks:
  print(block)
  o.write(str(block[0])+" "+str(block[1])+ " " + str(block[2]))
  o.write("\n")
print("You can also see it in the output file")

# Close the files
o.close()
f.close()
