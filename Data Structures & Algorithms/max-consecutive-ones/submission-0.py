class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0

        for num in nums:
            if num == 0:
                if maximum < count:
                    maximum = count
                count = 0
            else:
                count += 1

        if maximum < count:
                maximum = count
        
        return maximum