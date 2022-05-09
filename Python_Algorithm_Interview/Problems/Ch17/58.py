from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, head1, head2):
        if not head2:
            return head1

        root = ListNode()

        node = root
        while head1 and head2:
            if head1.val > head2.val:
                node.next, head2 = head2, head2.next
            else:
                node.next, head1 = head1, head1.next

            node = node.next

        while head1:
            node.next, head1 = head1, head1.next
            node = node.next

        while head2:
            node.next, head2 = head2, head2.next
            node = node.next

        return root.next

    def my_sol(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if head and not head.next:
            return head

        runner = head
        fast_runner = head.next

        while fast_runner and fast_runner.next:
            runner = runner.next
            fast_runner = fast_runner.next.next

        head2, runner.next = runner.next, None

        left = self.sortList(head)
        right = self.sortList(head2)

        return self.merge(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sol1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

    def sol3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head
