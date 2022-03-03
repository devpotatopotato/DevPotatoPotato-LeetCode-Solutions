class MyCircularDeque:
    def __init__(self, k: int):
        self.dq = [None] * k
        self.front = 0
        self.rear = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.dq[self.front] is None:
            self.dq[self.front] = value
            self.front = (self.front + 1) % self.size
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        next_idx = (self.rear - 1) % self.size
        if self.dq[next_idx] is None:
            self.dq[next_idx] = value
            self.rear = next_idx
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        last_idx = (self.front - 1) % self.size
        if self.dq[last_idx] is None:
            return False
        else:
            self.dq[last_idx] = None
            self.front = last_idx
            return True

    def deleteLast(self) -> bool:
        if self.dq[self.rear] is None:
            return False
        else:
            self.dq[self.rear] = None
            self.rear = (self.rear + 1) % self.size
            return True

    def getFront(self) -> int:
        last_idx = (self.front - 1) % self.size
        if self.dq[last_idx] is None:
            return -1
        else:
            return self.dq[last_idx]

    def getRear(self) -> int:
        if self.dq[self.rear] is None:
            return -1
        else:
            return self.dq[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.dq[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.dq[self.front] is not None
