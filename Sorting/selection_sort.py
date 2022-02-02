# https://www.algoexpert.io/questions/Selection%20Sort
# O(N^2) T - O(1) S

def selection_sort(numbers: list[int]):
    for index in range(len(numbers)):
        smallest_index = _get_smallest_index(numbers, index)
        _swap(numbers, index, smallest_index)
    return numbers


def _get_smallest_index(numbers: list[int], starting_index):
    smallest_index = starting_index
    for index in range(starting_index + 1, len(numbers)):
        if numbers[index] < numbers[smallest_index]:
            smallest_index = index
    return smallest_index


def _swap(numbers: list[int], left_index: int, right_index: int):
    numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]
