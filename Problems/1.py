import collections
import re
from typing import Deque


def my_sol(s: str) -> bool:
    s = s.upper()
    i = 0
    j = len(s) - 1
    is_palinrome = True

    while i < j:
        if s[i] == " " or not s[i].isalnum():
            i += 1
        elif s[j] == " " or not s[j].isalnum():
            j -= 1
        elif s[i] == s[j]:
            i += 1
            j -= 1
        else:
            is_palinrome = False
            break

    return is_palinrome


def sol2(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def sol3(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]
