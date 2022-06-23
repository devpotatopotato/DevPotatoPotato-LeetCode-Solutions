import itertools
from typing import List


class Solution:
    def my_sol(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            for permutation in self.my_sol(nums[:i] + nums[i + 1 :]):
                result.append([nums[i]] + permutation)
        return result

    def sol1(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elemets = elements[:]
                next_elemets.remove(e)

                prev_elements.append(e)
                dfs(next_elemets)
                prev_elements.pop()

        dfs(nums)
        return results

    def sol2(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
