# https://leetcode.com/problems/design-hashmap

class HashMap:
    def __init__(self):
        self.size = 1998
        self.multiple = 2602
        self.data = [None] * self.size

    def hash(self, value) -> int:
        return (value * self.multiple) % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        hashed_key = self.hash(key)
        if self.data[hashed_key] is None:
            self.data[hashed_key] = []
        self.data[hashed_key].append((key, value))

    def get(self, key: int) -> int:
        hashed_key = self.hash(key)
        if not self.data[hashed_key]:
            return -1

        for original_key, value in self.data[hashed_key]:
            if key == original_key:
                return value
        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.hash(key)
        if not self.data[hashed_key]:
            return

        for index, (original_key, value) in enumerate(self.data[hashed_key]):
            if key == original_key:
                self.data[hashed_key].pop(index)
                return
