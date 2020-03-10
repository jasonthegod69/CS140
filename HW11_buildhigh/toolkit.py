import numpy as np

def get_block_combination(block):
    result = [block]
    result.append([block[0], block[2], block[1]])
    result.append([block[1], block[0], block[2]])
    result.append([block[1], block[2], block[0]])
    result.append([block[2], block[0], block[1]])
    result.append([block[2], block[1], block[0]])
    return result


# If I give you a input file, like 3, 268, 123, 357, give me a 2-d array of all the combinations of the three possible objects.
def get_all_combinations(block_array):
    total2D = []
    for item in block_array:
        for subitem in get_block_combination(item):
            total2D.append(subitem)
    return total2D


def clean_repetitive_and_reverse(combinations):
    endArray = []
    for item in combinations:
        if item not in endArray and item[0] <= item[1]:
            endArray.append(item)
    return endArray


def sort_in_x(Array2d):
    newarray = sorted(Array2d, key=lambda x: (x[0], x[1]))
    return newarray


# Returns true if b1 is clearly smaller than b2
def clearly_smaller(b1, b2):
    return (b1[0] < b2[0] and b1[1] < b2[1])


# [value, index in array]
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


def max_DP(DP):
    max_height = -1
    prev_ind = -1
    for item in DP:
        if item[0] > max_height:
            max_height = item[0]
            prev_ind = item[1]
    return [max_height, prev_ind]


def traceBack(max_height, DP):
    indeces = []
    indeces.append(DP.index(max_height) - 1)
    i = max_height[1]
    while i != -1:
        indeces.append(i)
        i = DP[i + 1][1]
    return indeces

