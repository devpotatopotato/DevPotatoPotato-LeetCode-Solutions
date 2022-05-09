import collections


class Solution:
    def my_sol(self, s: str) -> str:
        # wrong answer
        used_char = []

        def find_chr(s: str, type: str = "small") -> str:
            for remove_chr in used_char:
                s = s.replace(remove_chr, "")

            if len(s) < 2:
                used_char.append(s)
                return s

            elif type == "small":
                piv_chr = min(s)
                piv_chr_idx = s.index(piv_chr)
                used_char.append(piv_chr)

                back = find_chr(s[piv_chr_idx + 1 :], "big")
                front = find_chr(s[:piv_chr_idx], "small")

                return front + piv_chr + back

            elif type == "big":
                piv_chr = max(s)
                piv_chr_idx = s.rindex(piv_chr)
                used_char.append(piv_chr)

                front = find_chr(s[:piv_chr_idx], "small")
                back = find_chr(s[piv_chr_idx + 1 :], "big")

                return front + piv_chr + back

        return find_chr(s)

    def sol1(self, s: str) -> str:
        for chr in sorted(set(s)):
            suffix = s[s.index(chr) :]
            if set(s) == set(suffix):
                return chr + self.sol1(suffix.replace(chr, ""))
        return ""

    def sol2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return "".join(stack)
