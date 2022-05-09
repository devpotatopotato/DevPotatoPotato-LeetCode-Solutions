from typing import List
from unicodedata import digit


class Solution:
    def number_to_word(self, n: int) -> List[str] or None:
        if 2 <= n <= 6:
            return [chr(3 * n + 91 + i) for i in range(3)]
        elif n == 7:
            return [chr(3 * n + 91 + i) for i in range(4)]
        elif n == 8:
            return [chr(3 * n + 92 + i) for i in range(3)]
        elif n == 9:
            return [chr(3 * n + 92 + i) for i in range(4)]
        else:
            return []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = [""]
        for x in digits:
            temp = []
            words = self.number_to_word(int(x))
            for chr1 in result:
                for chr2 in words:
                    temp.append(chr1 + chr2)
            result = temp
        return result

    def sol1(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for j in dic[digits[index]]:
                dfs(index + 1, path + j)

        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        dfs(0, "")

        return result
