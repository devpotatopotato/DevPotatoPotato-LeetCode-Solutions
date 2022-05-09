import collections
from typing import Counter


class Solution:
    def my_sol(self, jewels: str, stones: str) -> int:
        stones = collections.Counter(stones)
        result = 0
        for x in jewels:
            result += stones[x]

        return result

    def sol4(self, jewels: str, stones: str) -> int:
        return sum([s in jewels for s in stones])
