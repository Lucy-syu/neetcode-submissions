class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        result = False
        for num in nums:
            if dictionary.get(num) is not None:
                result = True
            dictionary[num] = 1
        return result