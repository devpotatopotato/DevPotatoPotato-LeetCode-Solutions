import itertools
from typing import List


class Solution:
    def my_sol(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, depth):
            if depth == 0:
                result.append(prev[:])
                return

            for i, num in enumerate(nums):
                prev.append(num)
                if len(nums) - i >= depth:
                    dfs(nums[i + 1 :], depth - 1)
                prev.pop()

        result = []
        prev = []

        dfs([i for i in range(1, n + 1)], k)

        return result

    def sol1(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    def sol2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))
