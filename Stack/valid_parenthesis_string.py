# https://leetcode.com/problems/valid-parenthesis-string
# O(N) TS


def valid_parenthesis_string(string: str) -> bool:
    parenthesis_stack = []
    star_stack = []
    for index, character in enumerate(string):
        if character == "(":
            parenthesis_stack.append(index)

        if character == "*":
            star_stack.append(index)

        if character == ")":
            if parenthesis_stack:
                parenthesis_stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while parenthesis_stack and star_stack:
        if parenthesis_stack.pop() > star_stack.pop():
            return False

    return not parenthesis_stack
