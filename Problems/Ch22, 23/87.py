import collections


class Solution:
    dp = collections.defaultdict(int)

    def sol1(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.sol1(n - 1) + self.sol1(n - 2)
        return self.dp[n]
