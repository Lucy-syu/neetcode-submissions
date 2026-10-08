class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        last = -1
        max = 0

        for n in sorted(nums):
            if count == 0:
                count = 1
                max = 1
            elif n - last == 1:
                count = count + 1
                if count > max:
                    max = count
            elif n != last and n - last != 1:
                if count > max:
                    max = count
                count = 1


            last = n
        
        return max