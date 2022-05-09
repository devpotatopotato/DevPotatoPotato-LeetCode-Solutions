from typing import List


class Solution:
    def my_sol(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)
        result = [intervals.pop()]

        while intervals:
            last = result[-1]
            cur = intervals.pop()

            if last[0] <= cur[0] and last[1] >= cur[1]:
                pass
            elif last[1] >= cur[0]:
                result.pop()
                result.append([last[0], cur[1]])
            else:
                result.append(cur)

        return result

    def sol1(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += (i,)
        return merged
