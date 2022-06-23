from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def my_sol(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        odd, even = head, head.next
        even_root = even

        while odd.next and odd.next.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_root

        return head
