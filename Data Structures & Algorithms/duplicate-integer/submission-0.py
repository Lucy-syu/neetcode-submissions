class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = []
        result = False
        for num in nums:
            if counter.count(num) != 0:
                result = True
            counter.append(num)
        return result