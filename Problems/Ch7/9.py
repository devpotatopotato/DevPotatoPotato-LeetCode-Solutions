from operator import le
from typing import List
from unittest import result


def my_sol(nums: List[int]) -> List[List[int]]:
    result = []

    if len(nums) < 3:
        return result

    nums.sort()
    target_list = []
    for target_idx in range(len(nums)):

        if nums[target_idx] in target_list:
            continue
        target_list.append(nums[target_idx])

        left, right = target_idx + 1, len(nums) - 1

        while left < right:
            if left == target_idx:
                left += 1
            elif right == target_idx:
                right -= 1
            elif left != target_idx + 1 and nums[left] == nums[left - 1]:
                left += 1
            elif right != len(nums) - 1 and nums[right] == nums[right + 1]:
                right -= 1
            elif nums[left] + nums[right] + nums[target_idx] < 0:
                left += 1
            elif nums[left] + nums[right] + nums[target_idx] > 0:
                right -= 1
            else:
                result.append([nums[target_idx], nums[left], nums[right]])
                left += 1

    return result


def sol1(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result


def sol2(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result
