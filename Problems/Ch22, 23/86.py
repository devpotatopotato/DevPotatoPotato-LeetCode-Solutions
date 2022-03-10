import sys
from typing import List


class Solution:
    def sol1(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
            print(nums[i], end=" ")
        return max(nums)

    def sol2(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(current_sum, best_sum)

        return best_sum
