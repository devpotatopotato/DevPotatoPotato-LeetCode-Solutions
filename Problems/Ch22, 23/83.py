import collections
from typing import List


class Solution:
    def my_sol(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]

    def sol3(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.sol3(nums[:half])
        b = self.sol3(nums[half:])

        return [b, a][nums.count(a) > half]

    def sol4(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
