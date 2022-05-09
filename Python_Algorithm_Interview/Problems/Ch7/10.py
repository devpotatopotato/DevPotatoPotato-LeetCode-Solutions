from typing import List
from unittest import result


def my_sol(nums: List[int]) -> int:
    nums.sort()
    result = 0

    for i in range(0, len(nums), 2):
        result += nums[i]

    return result


def sol3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
