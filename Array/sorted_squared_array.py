# https://leetcode.com/problems/squares-of-a-sorted-array/
# O(N) TS

def sortedSquaredArray(array):
    sorted_squared_array = [0] * len(array)
    smaller_value_index = 0
    larger_value_index = len(array) - 1

    while smaller_value_index <= larger_value_index:
        smaller_value = array[smaller_value_index]
        larger_value = array[larger_value_index]

        if abs(larger_value) > abs(smaller_value):
            sorted_squared_array[larger_value_index - smaller_value_index] = larger_value ** 2
            larger_value_index -= 1
        else:
            sorted_squared_array[larger_value_index - smaller_value_index] = smaller_value ** 2
            smaller_value_index += 1

    return sorted_squared_array
