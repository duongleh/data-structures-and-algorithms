# https://leetcode.com/problems/merge-sorted-array
# O(M+N) TS


def merge_sorted_arrays(arr_1, arr_2):
    len_1 = len(arr_1)
    len_2 = len(arr_2)
    index_1 = 0
    index_2 = 0
    merged_arrays = []

    while index_1 < len_1 and index_2 < len_2:
        if arr_1[index_1] <= arr_2[index_2]:
            merged_arrays.append(arr_1[index_1])
            index_1 += 1
        else:
            merged_arrays.append(arr_2[index_2])
            index_2 += 1

    if index_1 == len_1:
        merged_arrays = merged_arrays + arr_2[index_2:]

    if index_2 == len_2:
        merged_arrays = merged_arrays + arr_1[index_1:]

    return merged_arrays
