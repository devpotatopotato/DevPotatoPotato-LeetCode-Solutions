from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def my_sol(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result