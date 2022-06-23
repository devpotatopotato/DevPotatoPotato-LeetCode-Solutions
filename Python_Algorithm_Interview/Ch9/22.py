from itertools import count
from typing import List


class Solution:
    def my_sol(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        while temperatures:
            temp = temperatures.pop()
            count = 1
            while stack and temp >= stack[-1][0]:
                count += stack.pop()[1]
            if not stack:
                stack.append((temp, 0))
                result.append(0)
            else:
                stack.append((temp, count))
                result.append(count)
        result.reverse()
        return result

    def sol1(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
