class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if self.alphaNum(s[left]) and self.alphaNum(s[right]) and s[left].upper() != s[right].upper():
                return False
            elif not self.alphaNum(s[left]):
                left += 1
            elif not self.alphaNum(s[right]):
                right -= 1
            else:
                left += 1
                right -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))