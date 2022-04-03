# https://leetcode.com/problems/valid-parentheses
# O(N) TS

from stack import Stack


def is_valid_parentheses(string: str) -> bool:
    stack = Stack()
    matching_brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for character in string:
        if character in matching_brackets.values():
            stack.push(character)
        elif character in matching_brackets:
            if stack.is_empty():
                return False
            if stack.pop() != matching_brackets[character]:
                return False

    return stack.is_empty()
