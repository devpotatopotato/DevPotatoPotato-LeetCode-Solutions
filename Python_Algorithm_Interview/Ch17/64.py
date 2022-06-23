import heapq
from typing import List


class Solution:
    def my_sol(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        result = []

        for idx, point in enumerate(points):
            x, y = point
            heapq.heappush(pq, (x ** 2 + y ** 2, idx))

        for _ in range(k):
            result.append(points[heapq.heappop(pq)[1]])

        return result
