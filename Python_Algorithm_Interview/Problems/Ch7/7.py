import imp
from typing import List


def my_sol(nums: List[int], target: int) -> List[int]:
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [i, j]


def my_sol2(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        if target - nums[i] in nums:
            j = nums.index(target - nums[i])
            if i != j:
                return [i, j]


def sol1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def sol2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1 :]:
            return [nums.index(n), nums[i + 1 :].index(complement) + (i + 1)]


def sol3(nums: List[int], target: int) -> List[int]:
    num_maps = {}
    for i, n in enumerate(nums):
        num_maps[n] = i

    for i, n in enumerate(nums):
        if target - n in num_maps and i != num_maps[target - n]:
            return [i, num_maps[target - n]]


def sol4(nums: List[int], target: int) -> List[int]:
    num_maps = {}
    for i, n in enumerate(nums):
        if target - n in num_maps:
            return [i, num_maps[target - n]]
        num_maps[n] = i


def sol5(nums: List[int], target: int) -> List[int]:
    # wrong answer / 정렬된 input에 대해서만 작동 / index return 하는 문제라 정렬해버리면 안됨
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
