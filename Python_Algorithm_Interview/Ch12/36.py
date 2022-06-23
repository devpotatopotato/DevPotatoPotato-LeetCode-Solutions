from typing import List


class Solution:
    def my_sol(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        prev = []

        def dfs(nums: list, t: int) -> bool or None:
            print(prev, t)
            if t < 0:
                return
            elif t == 0:
                result.append(prev[:])
                return

            for i, n in enumerate(nums):
                prev.append(n)
                dfs(nums[i:], t - n)
                prev.pop()

        dfs(candidates, target)
        return result
