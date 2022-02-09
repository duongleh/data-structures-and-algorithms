# https://leetcode.com/problems/binary-search/
# O(log(N)) T - O(1) S

def binary_search(array: list[int], target: int) -> int:
    start_index = 0
    end_index = len(array) - 1
    while end_index >= start_index:
        middle_index = start_index + (end_index - start_index) // 2
        if target == array[middle_index]:
            return middle_index
        elif target < array[middle_index]:
            end_index = middle_index - 1
        elif target > array[middle_index]:
            start_index = middle_index + 1
    return -1
