from cmath import pi
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sol1(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sol1(nums[:mid])
        node.right = self.sol1(nums[mid + 1 :])

        return node
