# https://leetcode.com/problems/palindrome-number
# O(log10(N)) T | O(1) S (we divided the input by 10 for every iteration)


def palindrome_number(number: int) -> bool:
    # If the last digit of the number is 0, in order to be a palindrome,
    # the first digit of the number also needs to be 0. Only 0 satisfy this property.
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reverted_number = 0
    while reverted_number < number:
        reverted_number = reverted_number * 10 + number % 10
        number //= 10

    return number in [reverted_number, reverted_number // 10]
