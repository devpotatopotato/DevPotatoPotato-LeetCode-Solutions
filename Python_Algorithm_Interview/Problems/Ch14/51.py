import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    saved: int = 0
    val: int = 0

    def my_sol(self, root: TreeNode) -> TreeNode:
        def add_num(node: TreeNode):
            if node is None:
                return

            add_num(node.right)
            self.saved += node.val
            node.val = self.saved
            add_num(node.left)

        add_num(root)
        return root

    def sol1(self, root: TreeNode) -> TreeNode:
        if root:
            self.sol1(root.right)
            self.val += root.val
            root.val = self.val
            self.sol1(root.left)

        return root
