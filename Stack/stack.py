class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __len__(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return self.__len__() == 0

    @property
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack.pop()

    def push(self, number):
        return self.stack.append(number)
