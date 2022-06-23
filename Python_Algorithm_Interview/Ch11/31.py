import collections
import heapq
from typing import List


class Solution:
    def my_sol(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in collections.Counter(nums).most_common(k)]

    def sol1(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
