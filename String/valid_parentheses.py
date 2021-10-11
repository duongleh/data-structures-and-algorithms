# https://leetcode.com/problems/valid-parentheses/
# O(N) TS

def is_valid_parentheses(string: str) -> bool:
    stack = []
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for character in string:
        if character in matching_brackets.values():
            stack.append(character)
        else:
            if not stack or stack.pop() != matching_brackets[character]:
                return False

    return stack == []
