# https://leetcode.com/problems/valid-palindrome
# O(N) T | O(1) S


def is_palindrome(string: str) -> bool:
    index_from_start = 0
    index_from_end = len(string) - 1

    while index_from_start < index_from_end:
        if not string[index_from_start].isalnum():
            index_from_start += 1
            continue

        if not string[index_from_end].isalnum():
            index_from_end -= 1
            continue

        if string[index_from_start].lower() != string[index_from_end].lower():
            return False

        index_from_start += 1
        index_from_end -= 1

    return True
