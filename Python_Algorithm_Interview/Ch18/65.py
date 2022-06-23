import bisect
from typing import List


class Solution:
    def my_sol(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        piv = len(nums) // 2

        if nums[piv] < target:
            next = self.my_sol(nums[piv + 1 :], target)
            return next if next == -1 else piv + next + 1
        elif nums[piv] > target:
            return self.my_sol(nums[:piv], target)
        else:
            return piv

    def sol1(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    def sol2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

    def sol3(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
