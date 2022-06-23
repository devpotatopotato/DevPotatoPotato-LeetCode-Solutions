from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def my_sol(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        result = 0
        if root.val < low:
            result += self.my_sol(root.right, low, high)
        elif low <= root.val <= high:
            result += root.val
            result += self.my_sol(root.right, low, high)
            result += self.my_sol(root.left, low, high)
        else:
            result += self.my_sol(root.left, low, high)

        return result

    def sol3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop()

            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val

        return sum
