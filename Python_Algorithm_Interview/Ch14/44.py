from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    length = 0
    result: int = 0

    def my_sol(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent_val: int = None) -> int:
            if node is None:
                return -1

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)

            self.length = max(self.length, left + right + 2)

            if parent_val is not None and parent_val != node.val:
                return -1

            else:
                return max(left, right) + 1

        dfs(root)

        return self.length

    def sol1(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        dfs(root)
        return self.result
