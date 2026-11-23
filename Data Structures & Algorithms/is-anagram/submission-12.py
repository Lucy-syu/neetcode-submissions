class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}

        for c1 in s:
            if c1 not in m1:
                m1[c1] = 1
            else:
                m1[c1] += 1

        for c2 in t:
            if c2 not in m2:
                m2[c2] = 1
            else:
                m2[c2] += 1
        
        if len(m1) > len(m2):
            for el in m1:
                if (el in m2 and m2[el] != m1[el]) or el not in m2:
                    return False
        else:
            for el in m2:
                if (el in m1 and m2[el] != m1[el]) or el not in m1:
                    return False
        
        return True