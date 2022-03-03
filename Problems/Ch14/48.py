from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def my_sol(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1
