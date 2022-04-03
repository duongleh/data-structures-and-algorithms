# https://leetcode.com/problems/min-stack
# https://leetcode.com/problems/max-stack
# O(1) TS

from stack import Stack


class MinMaxStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.min_max_stack = []

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        min_max = {
            "min": number if not self.stack else min(number, self.get_min()),
            "max": number if not self.stack else max(number, self.get_max()),
        }
        self.min_max_stack.append(min_max)
        return self.stack.append(number)

    def get_min(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.min_max_stack[-1]["min"]

    def get_max(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.min_max_stack[-1]["max"]
