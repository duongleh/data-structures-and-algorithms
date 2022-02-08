# https://www.algoexpert.io/questions/Merge%20Sort
# O(Nlog(N)) T - O(Nlog(N)) S

from Array.merge_sorted_arrays import merge_sorted_arrays


def merge_sort(array: list[int]) -> list[int]:
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left_sorted_array = merge_sort(array[0:middle])
    right_sorted_array = merge_sort(array[middle:])

    return merge_sorted_arrays(left_sorted_array, right_sorted_array)
