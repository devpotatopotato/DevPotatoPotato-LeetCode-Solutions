import bisect
import heapq
from typing import List


class Solution:
    def my_sol(self, g: List[int], s: List[int]) -> int:
        children_heap = [-n for n in g]
        cookie_heap = [-n for n in s]

        heapq.heapify(cookie_heap)
        heapq.heapify(children_heap)

        count = 0
        while cookie_heap and children_heap:
            cookie = -cookie_heap[0]
            child = -heapq.heappop(children_heap)

            if cookie >= child:
                heapq.heappop(cookie_heap)
                count += 1

        return count

    def sol1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

    def sol2(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result
