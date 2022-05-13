# https://leetcode.com/problems/decode-ways
# O(N) T | O(1) S


def num_ways_of_decodings(s: str) -> int:
    second_last_char, last_char = 0, 1

    for index in range(len(s) - 1, -1, -1):
        temp_last_char = last_char
        if s[index] == "0":
            last_char = 0
        elif int(s[index : index + 2]) <= 26 and index + 1 < len(s):
            last_char += second_last_char
        second_last_char = temp_last_char

    return last_char
