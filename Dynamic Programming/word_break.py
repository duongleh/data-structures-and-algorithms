# https://leetcode.com/problems/word-break
# O(len(s) * len(word_dict)) T | O(len(s)) S


def word_break(s: str, word_dict: list[str]) -> bool:
    word_breakable = [False] * len(s)

    for char_index in range(len(s)):
        for word in word_dict:
            start_index = char_index - len(word) + 1
            if start_index < 0:
                continue

            if word != s[start_index : char_index + 1]:
                continue

            if start_index == 0:
                word_breakable[char_index] = True
            else:
                word_breakable[char_index] = word_breakable[start_index - 1]

            if word_breakable[char_index]:
                break

    return word_breakable[-1]
