class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        register = {}
        i = 0

        for num in nums:
            if num in register:
                return True
            else:
                register[num] = i
            i += 1
        
        return False
        