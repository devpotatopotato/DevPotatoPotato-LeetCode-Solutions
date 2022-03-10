from typing import List


class Solution:
    def is_bigger(self, word1: str, word2: str) -> int:
        if word1 + word2 > word2 + word1:
            return 1
        elif word1 + word2 < word2 + word1:
            return -1
        return 0

    def modified_merge(self, l1: List[str], l2: List[str]):
        i = j = 0
        result = []
        while i < len(l1) and j < len(l2):
            if self.is_bigger(l1[i], l2[j]) >= 0:
                result.append(l1[i])
                i += 1

            else:
                result.append(l2[j])
                j += 1

        if i <= len(l1):
            result.extend(l1[i:])

        if j <= len(l1):
            result.extend(l2[j:])

        return result

    def modified_merge_sort(self, lst: List[str]):
        if len(lst) <= 1:
            return lst

        piv = len(lst) // 2
        left = self.modified_merge_sort(lst[:piv])
        right = self.modified_merge_sort(lst[piv:])

        return self.modified_merge(left, right)

    def my_sol(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return "0"

        return "".join(self.modified_merge_sort([str(n) for n in nums]))

    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def sol1(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int("".join(map(str, nums))))
