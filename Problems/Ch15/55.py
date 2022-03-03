import heapq
from typing import List


class Solution:
    def my_sol(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -n)

        for _ in range(k):
            result = heapq.heappop(pq)

        return -result

    def sol1(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

    def sol2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def sol3(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
