from typing import List


class Solution:
    def my_sol(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for i in left:
                for j in right:
                    results.append(eval(str(i) + op + str(j)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for i, val in enumerate(expression):
            if val in {"-", "+", "*"}:
                left = self.my_sol(expression[:i])
                right = self.my_sol(expression[i + 1 :])

                results.extend(compute(left, right, val))

        return results


Solution().my_sol("2*3-4*5")
