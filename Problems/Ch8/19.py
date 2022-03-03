from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def my_sol(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        root = node = ListNode(None, head)
        position = 0

        if left == right:
            return head

        while position <= right:
            if position == left - 1:
                start = node
            elif position == left:
                reverse_head = node
            position += 1
            node = node.next

        last = node
        while reverse_head != node:
            reverse_head.next, reverse_head, last = (
                last,
                reverse_head.next,
                reverse_head,
            )
        start.next = last

        return root.next

    def sol1(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next
