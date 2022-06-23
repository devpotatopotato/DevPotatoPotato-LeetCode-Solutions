from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def my_sol(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        elif list1 is None:
            return list2

        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            pointer = list1
            list1 = list1.next
        else:
            pointer = list2
            list2 = list2.next

        head = pointer

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        while list1 is not None:
            pointer.next = list1
            pointer = pointer.next
            list1 = list1.next

        while list2 is not None:
            pointer.next = list2
            pointer = pointer.next
            list2 = list2.next

        return head

    def sol1(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list1, list2

        if list1:
            list1.next = self.sol1(list1.next, list2)

        return list1
