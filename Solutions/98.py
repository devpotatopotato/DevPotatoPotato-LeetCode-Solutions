from typing import Optional

from regex import D

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def my_sol(self, root: Optional[TreeNode]) -> bool:
        sorted_list = []

        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            
            dfs(node.left)
            sorted_list.append(node.val)
            dfs(node.right)
        
        dfs(root)

        for i in range(len(sorted_list) - 1):
            if sorted_list[i] >= sorted_list[i + 1]:
                return False
        
        return True

    def sol1(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root: 
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        return self.sol1(root.left, floor, root.val) and self.sol1(root.right, root.val, ceiling)
