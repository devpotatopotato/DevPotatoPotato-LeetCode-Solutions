import collections
from typing import List


class Solution:
    def my_sol(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(diff) < 0:
            return -1

        candidates = collections.deque()

        total = 0
        start_idx = None
        for i, val in enumerate(diff):
            if val >= 0 and start_idx is None:
                start_idx = i
                total += val
            elif val >= 0 and start_idx is not None:
                total += val
            elif val < 0 and start_idx is not None:
                total += val
                candidates.append([start_idx, total])
                start_idx = None
                total = 0

        if start_idx is not None:
            if candidates and candidates[0][0] == 0:
                temp = candidates.popleft()
                total += temp[1]
            candidates.append([start_idx, total])

        return max(candidates, key=lambda x: x[1])[0]

    def sol2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start
