# https://www.algoexpert.io/questions/Bubble%20Sort
# O(N^2) T | O(1) S


def bubble_sort(numbers: list[int]):
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        # After each iteration, the largest element among the unsorted elements is placed at the end
        # Therefore, we don't have to go all the way to the end of the list
        for index in range(len(numbers) - counter - 1):
            if numbers[index] <= numbers[index + 1]:
                continue

            _swap(numbers, index, index + 1)
            is_sorted = False

        counter += 1

    return numbers


def _swap(numbers: list[int], left_index: int, right_index: int):
    numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]
