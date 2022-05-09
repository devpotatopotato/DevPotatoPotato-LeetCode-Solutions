from typing import List


class Solution:
    def my_sol(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = []

        def dfs(nums):
            result.append(prev[:])

            for i, n in enumerate(nums):
                prev.append(n)
                dfs(nums[i + 1 :])
                prev.pop()

        dfs(nums)
        return result
