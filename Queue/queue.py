class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __len__(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.queue.pop(0)
