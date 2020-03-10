# Returns an array with all of a single block's 6 length, width, height combinations
def get_block_combination(block):
    result = [block]
    result.append([block[0], block[2], block[1]])
    result.append([block[1], block[0], block[2]])
    result.append([block[1], block[2], block[0]])
    result.append([block[2], block[0], block[1]])
    result.append([block[2], block[1], block[0]])
    return result


# Returns a 2d array of each block and its combinations of length, width, and height
def get_all_combinations(block_array):
    total2D = []
    for item in block_array:
        for subitem in get_block_combination(item):
            total2D.append(subitem)
    return total2D

# From a 2d array of all the blocks and their combinations, remove all repetitive
# blocks except a single occurance (ex: [4, 4, 10] [4, 4, 10]) and all blocks that
# have a length bigger than its width (ex: remove [5, 3, 10]) because by formatting
# all such blocks this way, we have to go through fewer combinations
def clean_repetitive_and_reverse(combinations):
    endArray = []
    for item in combinations:
        if item not in endArray and item[0] <= item[1]:
            endArray.append(item)
    return endArray

# Sorts a 2d array of blocks by length (the first element), and if two blocks have
# the same length, then sort by width (the second element)
def sort_in_x(Array2d):
    newarray = sorted(Array2d, key=lambda x: (x[0], x[1]))
    return newarray


# Returns true if a block's width and length are smaller than another blocks
def clearly_smaller(b1, b2):
    return (b1[0] < b2[0] and b1[1] < b2[1])


# Creates a dynamic table that goes through the sorted array while choosing the
# max solution for each block, resulting in a max height for each block at their
# respective indeces. It is formatted with the max height and the block's
# index that builds on it, with -1 referring to no block.
def build_dynamic_table(sorted_array):
    DP = [[0, -1]]
    for i in range(0, len(sorted_array)):
        if i == 0:
            DP.append([sorted_array[i][2], -1])
        else:
            j = i
            prev_max = 0
            prev_ind = -1
            while j >= 0:
                if clearly_smaller(sorted_array[j], sorted_array[i]):
                    if (DP[j + 1][0] > prev_max):
                        prev_max = DP[j + 1][0]
                        prev_ind = j
                j -= 1
            # This entry's height + the last entry's height
            value = sorted_array[i][2] + prev_max
            DP.append([value, prev_ind])
    return DP

# Finds the maximum height by searching through the dynamic table and returning
# the maximum height and the index of the block that builds on it
def max_DP(DP):
    max_height = -1
    prev_ind = -1
    for item in DP:
        if item[0] > max_height:
            max_height = item[0]
            prev_ind = item[1]
    return [max_height, prev_ind]

# Using the max_height and the index of the block that is built on it,
# creates an array of indeces with all of the blocks that are built on it.
def traceBack(max_height_and_prev, DP):
    indeces = []
    indeces.append(DP.index(max_height_and_prev) - 1)
    i = max_height_and_prev[1]
    while i != -1:
        indeces.append(i)
        i = DP[i + 1][1]
    return indeces

