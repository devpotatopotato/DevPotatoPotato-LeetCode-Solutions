from typing import List


class Solution:
    def my_sol(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] == target:
                return True
            elif row[0] > target:
                break

            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2

                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
                else:
                    return True

        return False

    def sol1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False

    def sol2(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
