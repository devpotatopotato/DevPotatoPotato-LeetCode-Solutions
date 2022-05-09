import collections


class Solution:
    def my_sol(self, s: str) -> int:
        word_queue = collections.deque()
        word_idx = collections.defaultdict(int)
        result = 0

        for x in s:
            if word_idx[x]:
                result = max(result, len(word_queue))
                temp = None
                while temp != x:
                    temp = word_queue.popleft()
                    word_idx[temp] = 0

            word_queue.append(x)
            word_idx[x] = 1

        return max(result, len(word_queue))

    def sol1(self, s: str) -> str:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
