import collections
from curses import window
import heapq
from typing import List


class Solution:
    def my_sol(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        right = k

        heap = []
        for i, num in enumerate(nums[left:right]):
            heapq.heappush(heap, (-num, i))

        result.append(-heap[0][0])

        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            left += 1
            right += 1

            while heap[0][1] < left:
                heapq.heappop(heap)
            num = -heap[0][0]
            result.append(num)

        return result

    def sol1(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i : i + k]))

        return r

    def sol2(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float("-inf")

        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float("-inf"):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            if current_max == window.popleft():
                current_max = float("-inf")

        return results
