from typing import Optional


class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.item_count = 0
        self.bucket_size = 8
        self.buckets = [None] * self.bucket_size
        self.load_factor = self.item_count / self.bucket_size

    def double(self):
        self.bucket_size *= 2
        self.load_factor = self.item_count / self.bucket_size
        new_bucket = [None] * self.bucket_size

        for node in self.buckets:
            while node is not None:
                hashcode = node.key % self.bucket_size
                if new_bucket[hashcode] is None:
                    new_bucket[hashcode] = ListNode(node.key, node.value)
                else:
                    temp = new_bucket[hashcode]
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = ListNode(node.key, node.value)
                node = node.next
        self.buckets = new_bucket

    def put(self, key: int, value: int) -> None:
        if self.load_factor >= 0.75:
            self.double()

        hashcode = key % self.bucket_size

        if self.buckets[hashcode] is None:
            self.buckets[hashcode] = ListNode(key, value)
            self.item_count += 1
        else:
            temp = self.buckets[hashcode]
            last = None
            is_exist = False
            while temp is not None:
                if temp.key == key:
                    temp.value = value
                    is_exist = True
                    break
                last, temp = temp, temp.next
            if not is_exist:
                last.next = ListNode(key, value)
                self.item_count += 1

        self.load_factor = self.item_count / self.bucket_size

    def get(self, key: int) -> int:
        hashcode = key % self.bucket_size
        temp = self.buckets[hashcode]

        while temp is not None:
            if temp.key == key:
                return temp.value
            temp = temp.next

        return -1

    def remove(self, key: int) -> None:
        hashcode = key % self.bucket_size
        temp = self.buckets[hashcode]
        last = None

        while temp is not None:
            if temp.key == key and last == None:
                self.buckets[hashcode] = temp.next
                break
            elif temp.key == key and last != None:
                last.next = temp.next
                break
            last, temp = temp, temp.next

    def print_map(self) -> None:
        print("=============hashmap=============")
        print(f"item_count: {self.item_count}")
        print(f"bucket_size: {self.bucket_size}")
        print(f"load_factor: {self.load_factor}")
        print("_________________________________")
        for i in self.buckets:
            if i is None:
                print("None")
            else:
                while i is not None:
                    print(f"({i.key}, {i.value}) -> ", end="")
                    i = i.next
                print(i)
        print("=================================")
