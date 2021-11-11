import typing
from typing import List


def my_sol(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def sol2(s: List[str]) -> None:
    s.reverse()
