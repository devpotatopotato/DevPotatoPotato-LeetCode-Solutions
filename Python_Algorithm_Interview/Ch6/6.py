from cmath import exp
from unittest import result


def check_is_palindrome(idx1: int, idx2: int, s: str) -> bool:
    # works only if idx1 <= idx2
    piv = (idx1 + idx2) // 2
    if idx1 == idx2:
        return True
    elif (idx2 - idx1 + 1) % 2 == 0:
        return s[idx1 : piv + 1] == s[piv + 1 : idx2 + 1][::-1]
    else:
        return s[idx1:piv] == s[piv + 1 : idx2 + 1][::-1]


# wrong answer
def my_sol(s: str) -> str:
    for length in range(len(s), 0, -1):
        for idx in range(len(s) - length + 1):
            if check_is_palindrome(idx, idx + length - 1, s):
                return s[idx : idx + length]


def sol1(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result
