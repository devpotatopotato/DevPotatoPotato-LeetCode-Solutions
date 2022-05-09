import collections
from typing import List


class Solution:
    def my_sol(self, tasks: List[str], n: int) -> int:
        task_counter = collections.Counter(tasks)
        task_num = len(tasks)
        result = []
        while task_num > 0:
            most = task_counter.most_common(n + 1)
            for task, count in most:
                if count == 0:
                    result.append("#")
                else:
                    result.append(task)
                    task_counter[task] -= 1
                    task_num -= 1
            result.extend(["#"] * (n + 1 - len(most)))

        while result[-1] == "#":
            result.pop()

        return len(result)

    def sol1(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result
