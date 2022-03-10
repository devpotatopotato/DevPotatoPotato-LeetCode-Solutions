from typing import List


class Solution:
    def my_sol(self, prices: List[int]) -> int:
        stock = None
        profit = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]

            if stock is None and diff > 0:
                stock = prices[i]

            elif stock is not None and diff < 0:
                profit += prices[i] - stock
                stock = None

        if stock is not None:
            profit += prices[-1] - stock
            stock = None

        return profit

    def sol1(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result

    def sol2(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
