from typing import List
import sys


def my_sol(prices: List[int]) -> int:
    # failed to solve
    pass


def sol1(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


def sol2(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
