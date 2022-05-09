import collections


class MyCircularQueue:
    def __init__(self, k: int):
        self.circular_queue = [None] * k
        self.size = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.circular_queue[self.p2] is None:
            self.circular_queue[self.p2] = value
            self.p2 = (self.p2 + 1) % self.size
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.circular_queue[self.p1] is None:
            return False
        else:
            self.circular_queue[self.p1] = None
            self.p1 = (self.p1 + 1) % self.size
            return True

    def Front(self) -> int:
        return (
            -1 if self.circular_queue[self.p1] is None else self.circular_queue[self.p1]
        )

    def Rear(self) -> int:
        return (
            -1
            if self.circular_queue[self.p2 - 1] is None
            else self.circular_queue[self.p2 - 1]
        )

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.circular_queue[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.circular_queue[self.p1] is not None
