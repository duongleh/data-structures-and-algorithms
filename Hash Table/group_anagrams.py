# https://leetcode.com/problems/group-anagrams
# O(NKlogK) T | O(NK) S
# N is the length of strings, and K is the maximum length of a string in strings


def group_anagrams(strings: list[str]) -> list[list[str]]:
    anagram_group = {}
    for string in strings:
        sorted_string = str(sorted(string))
        if sorted_string not in anagram_group:
            anagram_group[sorted_string] = []
        anagram_group[sorted_string].append(string)
    return anagram_group.values()
