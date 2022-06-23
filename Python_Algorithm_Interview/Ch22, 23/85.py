class Solution:
    fib_dict = {}

    def my_sol(self, n: int) -> int:
        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n in self.fib_dict:
            return self.fib_dict[n]

        else:
            result = self.my_sol(n - 1) + self.my_sol(n - 2)
            self.fib_dict[n] = result
            return result

    def my_sol2(self, n: int) -> int:
        fib_list = [0, 1]

        i = 2
        while i <= n:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            i += 1

        return fib_list[n]

    def sol3(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y

        return x
