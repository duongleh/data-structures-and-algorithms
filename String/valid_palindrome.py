# https://leetcode.com/problems/valid-palindrome
# O(N) T | O(1) S


def is_palindrome(string: str) -> bool:
    start = 0
    end = len(string) - 1

    while start < end:
        if not string[start].isalnum():
            start += 1
            continue

        if not string[end].isalnum():
            end -= 1
            continue

        if string[start].lower() != string[end].lower():
            return False

        start += 1
        end -= 1

    return True
