import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def my_sol(self, root: Optional[TreeNode]) -> int:
        def find_min_dif(node: TreeNode) -> int:
            left = node.left
            right = node.right

            left_last = sys.maxsize
            right_last = sys.maxsize

            while left and left_last > node.val - left.val:
                left_last = node.val - left.val
                left = left.right

            while right and right_last > right.val - node.val:
                right_last = right.val - node.val
                right = right.left

            return min(left_last, right_last)

        stack = [root]
        min_diff = sys.maxsize

        while stack:
            cur_node = stack.pop()

            if cur_node:
                stack.append(cur_node.left)
                stack.append(cur_node.right)

                min_diff = min(min_diff, find_min_dif(cur_node))

        return min_diff

    prev = -sys.maxsize
    result = sys.maxsize

    def sol1(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.sol1(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.sol1(root.right)

        return self.result

    def sol2(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result
