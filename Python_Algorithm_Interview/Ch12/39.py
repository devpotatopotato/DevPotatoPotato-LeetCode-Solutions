import collections
from copy import deepcopy
from typing import List


class Solution:
    # Time exceed
    def my_sol(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(now, g_dict, visited):
            if now in visited:
                return True
            for i, next in enumerate(g_dict[now]):
                visited.add(now)
                g_dict[now] = g_dict[now][:i] + g_dict[now][i + 1 :]
                if dfs(next, g_dict, visited):
                    return True
                else:
                    visited.remove(now)
                    g_dict[now] = g_dict[now][:i] + [next] + g_dict[now][i:]
            return False

        for i in graph:
            if dfs(i, deepcopy(graph), set()):
                return False
        return True

    def sol2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False

            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


print(Solution().my_sol(2, [[1, 0], [0, 1]]))
