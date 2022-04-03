# https://leetcode.com/problems/valid-anagram
# O(N) TS


def is_anagram(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False

    table = {}
    for character in first_string:
        table[character] = table.get(character, 0) + 1

    for character in second_string:
        if character not in table:
            return False

        table[character] -= 1
        if table[character] == 0:
            table.pop(character)

    return table == {}
