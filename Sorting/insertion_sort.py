# https://www.algoexpert.io/questions/Insertion%20Sort
# O(N^2) T | O(1) S


def insertion_sort(numbers: list[int]):
    for index in range(1, len(numbers)):
        swap_index = index
        while swap_index > 0 and numbers[swap_index] < numbers[swap_index - 1]:
            _swap(numbers, swap_index, swap_index - 1)
            swap_index -= 1
    return numbers


def _swap(numbers: list[int], left_index: int, right_index: int):
    numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]
