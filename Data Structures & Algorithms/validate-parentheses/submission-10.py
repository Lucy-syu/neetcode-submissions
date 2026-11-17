class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0 or (s[0] != '(' and s[0] != '{' and s[0] != '['): return False

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack or (c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()

        return True if not stack else False