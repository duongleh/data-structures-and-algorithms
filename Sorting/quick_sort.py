# https://www.algoexpert.io/questions/Quick%20Sort
# Best: O(Nlog(N)) T - O(log(N)) S
# Worst: O(N^2) T - O(log(N)) S

def quick_sort(array: list[int]) -> list[int]:
    sort(array, 0, len(array) - 1)
    return array


def sort(array: list[int], start_index: int, end_index: int) -> None:
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_index = pivot_index + 1
    right_index = end_index
    while left_index <= right_index:
        if array[left_index] < array[pivot_index]:
            left_index += 1
            continue

        if array[right_index] > array[pivot_index]:
            right_index -= 1
            continue

        swap(array, left_index, right_index)
        left_index += 1
        right_index -= 1

    swap(array, pivot_index, right_index)

    sort(array, start_index, right_index - 1)
    sort(array, right_index + 1, end_index)


def swap(array: list[int], left_index: int, right_index: int) -> None:
    array[left_index], array[right_index] = array[right_index], array[left_index]
