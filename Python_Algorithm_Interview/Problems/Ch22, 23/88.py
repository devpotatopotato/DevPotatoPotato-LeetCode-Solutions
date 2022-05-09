import collections
from typing import List


class Solution:
    def sol1(self, nums: List[int]) -> int:
        dp = {}

        def _rob(i: int) -> int:
            if i < 0:
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(_rob(i - 1), _rob(i - 2) + nums[i])
            return dp[i]

        return _rob(len(nums) - 1)
