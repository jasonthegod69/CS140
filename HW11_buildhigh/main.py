
from toolkit import *

fName = "input.txt"
#fName = input("Enter input file name: ")
f = open(fName, 'r')
numBlocks = int(f.readline())
blockArray = []
maxL = 0
# Read in the input file
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

all_combs    = get_all_combinations(blockArray)
print("All combinations are: ")
print(all_combs)
print()
clean_combs  = clean_repetitive_and_reverse(all_combs)
print("After deleting the reverse and repetitives: ")
print(clean_combs)
print()
sorted_combs = sort_in_x(clean_combs)
print("After sorting in terms of the first entry: ")
print(sorted_combs)
print()

print("\n Running... \n\n")

DP = build_dynamic_table(sorted_combs)
print("Dynamic table: ")
print(DP)

max_height = max_DP(DP)
trace_back = traceBack(max_height, DP)
print()
print("Trace back: ")
print(trace_back)
print()
print()
print("-------- Answers -------")
print(f"\nThe tallest tower has {len(trace_back)} blocks and a height of {max_height[0]}")

blocks = []
for i in trace_back:
  blocks.append(sorted_combs[i])
print()
o = open("output.txt", "w+")
o.write(str(len(trace_back))+"\n")
print("The tallest build is: ")
for block in blocks:
  print(block)
  o.write(str(block[0])+" "+str(block[1])+ " " + str(block[2]))
  o.write("\n")
print("You can also see it in the output.txt file")

# Write to output
o.close()
f.close()
