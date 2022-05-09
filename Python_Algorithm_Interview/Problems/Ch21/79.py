import heapq
from typing import List


class Solution:
    def my_sol(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: x[1], reverse=True)
        people.sort(key=lambda x: x[0])

        result = []
        while people:
            person = people.pop()
            result.insert(person[1], person)

        return result

    def sol1(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result
