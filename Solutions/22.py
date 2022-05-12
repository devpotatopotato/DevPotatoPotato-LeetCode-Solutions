from typing import List


class Solution:
    def my_sol(self, n: int) -> List[str]:
        result = []
        added = set()

        def dfs(left_count, right_count, last):
            if left_count == n and right_count == n:
                added.add(last)
                result.append(last)
                return

            leftAdded = last + "("
            rightAdded = last + ")"

            if left_count < n and left_count == right_count:
                if leftAdded not in added:
                    added.add(leftAdded)
                    dfs(left_count + 1, right_count, leftAdded)

            elif left_count < n and left_count > right_count:
                if leftAdded not in added:
                    added.add(leftAdded)
                    dfs(left_count + 1, right_count, leftAdded)

                if rightAdded not in added:
                    added.add(rightAdded)
                    dfs(left_count, right_count + 1, rightAdded)

            elif left_count == n and left_count > right_count:
                if rightAdded not in added:
                    added.add(rightAdded)
                    dfs(left_count, right_count + 1, rightAdded)

        dfs(0, 0, "")

        return result

    def sol1(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + "(", left - 1, right)
            if right > left:
                generate(p + ")", left, right - 1)
            if not right:
                parens += [p]
            return parens

        return generate("", n, n)
    
    def sol3(self, n, open=0):
        if n > 0 and open >= 0:
            temp = ['(' + p for p in self.sol3(n-1, open+1)] + \
                   [')' + p for p in self.sol3(n, open-1)]
            return temp
        return [')' * open] * (not n)
