class Solution:
    def my_sol(self, s: str) -> bool:
        s_list = list(s)
        stack = []

        while s_list:
            stack.append(s_list.pop())
            if len(stack) < 2:
                pass
            elif stack[-1] == "{" and stack[-2] == "}":
                stack.pop()
                stack.pop()
            elif stack[-1] == "[" and stack[-2] == "]":
                stack.pop()
                stack.pop()
            elif stack[-1] == "(" and stack[-2] == ")":
                stack.pop()
                stack.pop()

        return len(stack) == 0

    def sol1(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0
