import collections
from inspect import stack
from typing import List


class Solution:
    def my_sol(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = collections.defaultdict(list)
        tickets.sort(key=lambda x: x[1])
        for t in tickets:
            ticket_dict[t[0]].append(t[1])

        result = ["JFK"]

        def dfs(t_dict):
            if len(result) == len(tickets) + 1:
                return True

            now = result[-1]

            for i, next in enumerate(t_dict[now]):
                result.append(next)
                t_dict[now] = t_dict[now][:i] + t_dict[now][i + 1 :]
                if dfs(t_dict):
                    return True
                else:
                    t_dict[now] = t_dict[now][:i] + [next] + t_dict[now][i:]
                    result.pop()
            return False

        dfs(ticket_dict)
        return result

    def sol2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(now):
            while graph[now]:
                dfs(graph[now].pop())
            route.append(now)

        dfs("JFK")
        return route[::-1]

    def sol3(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
