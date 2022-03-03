from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def my_sol(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev_node = None
        carry = 0
        while l1 is not None and l2 is not None:
            sum = (l1.val + l2.val + carry) % 10
            prev_node = ListNode(sum, prev_node)

            carry = (l1.val + l2.val + carry) // 10

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = (l1.val + carry) % 10
            prev_node = ListNode(sum, prev_node)

            carry = (l1.val + carry) // 10
            l1 = l1.next

        while l2 is not None:
            sum = (l2.val + carry) % 10
            prev_node = ListNode(sum, prev_node)

            carry = (l2.val + carry) // 10
            l2 = l2.next

        if carry == 1:
            prev_node = ListNode(carry, prev_node)

        prev = None
        while prev_node is not None:
            prev_node.next, prev_node, prev = prev, prev_node.next, prev_node

        return prev

    def my_sol2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        result = head = ListNode()

        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return result.next

    def sol2(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
