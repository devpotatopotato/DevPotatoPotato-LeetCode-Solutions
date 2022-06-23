import bisect
from typing import List


class Solution:
    def my_sol(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            j = bisect.bisect_left(numbers, target - num)

            if 0 <= j < len(numbers) and j != i and numbers[j] == target - num:
                return sorted([i + 1, j + 1])

    def sol1(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    def sol2(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [k + 1, mid + 1]

    def sol3(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]
