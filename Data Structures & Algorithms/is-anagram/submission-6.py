class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True

        for char in s if len(s) >= len(t) else t:
            if s.count(char) != t.count(char):
                result = False

        return result