import collections

class Solution:
    def my_sol(self, s: str, k: int) -> bool:
        hasList = [False] * 2**k

        p1 = 0
        p2 = k

        while p2 <= len(s):
            hasList[int(s[p1 : p2], 2)] = True
            
            p1 += 1
            p2 += 1
        
        return sum(hasList) == 2**k
    
    def sol1(self, s: str, k: int) -> bool:
        seen = set()
        q = collections.deque()
        for c in s:
            q.append(c)
            if len(q) == k: seen.add(''.join(q)); q.popleft()
        return len(seen) == 1 << k
