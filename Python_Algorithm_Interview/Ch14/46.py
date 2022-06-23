import collections
from logging import root
import queue
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def my_sol(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 and root2:
            return TreeNode(
                root1.val + root2.val,
                self.my_sol(root1.left, root2.left),
                self.my_sol(root1.right, root2.right),
            )
        else:
            return root1 or root2
