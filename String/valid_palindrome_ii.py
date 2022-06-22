# https://leetcode.com/problems/valid-palindrome-ii
# O(N) TS


def valid_palindrome_ii(string: str) -> bool:
    def check_palindrome(left: int, right: int, removed: bool) -> bool:
        if left >= right:
            return True

        if string[left] == string[right]:
            return check_palindrome(left + 1, right - 1, removed)

        if removed is True:
            return False

        return check_palindrome(left + 1, right, True) or check_palindrome(left, right - 1, True)

    return check_palindrome(0, len(string) - 1, False)
