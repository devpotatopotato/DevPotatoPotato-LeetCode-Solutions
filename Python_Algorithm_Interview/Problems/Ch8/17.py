from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def my_sol(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        last = None
        result = head.next
        while head and head.next:
            if last:
                last.next = head.next
            head.next.next, head.next = head, head.next.next
            head, last = head.next, head

        return result

    def sol2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    def sol3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.sol3(p.next)
            p.next = head
            return p
        return head
