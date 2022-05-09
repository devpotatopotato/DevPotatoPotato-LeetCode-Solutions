import collections
from typing import List, Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def my_sol(head: Optional[ListNode]) -> bool:
    val_list: List = []
    while head != None:
        val_list.append(head.val)
        head = head.next

    return val_list == list(reversed(val_list))


def sol1(head: Optional[ListNode]) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


def sol2(head: Optional[ListNode]) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


def sol4(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev
