import collections


class MyStack:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)
        for _ in range(len(self.queue) - 1):
            self.queue.appendleft(self.queue.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
