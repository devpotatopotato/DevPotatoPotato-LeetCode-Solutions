import collections
from typing import List


class Solution:
    def my_sol(self, grid: List[List[str]]) -> int:
        discoverd = collections.defaultdict(int)
        count = 0

        def dfs(i, j) -> int:
            discoverd[(i, j)] = 1
            if (
                i + 1 < len(grid)
                and grid[i + 1][j] == "1"
                and not discoverd[(i + 1, j)]
            ):
                dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == "1" and not discoverd[(i, j - 1)]:
                dfs(i, j - 1)
            if i - 1 >= 0 and grid[i - 1][j] == "1" and not discoverd[(i - 1, j)]:
                dfs(i - 1, j)
            if (
                j + 1 < len(grid[0])
                and grid[i][j + 1] == "1"
                and not discoverd[(i, j + 1)]
            ):
                dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not discoverd[(i, j)]:
                    dfs(i, j)
                    count += 1
        return count

    def sol1(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return
            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
