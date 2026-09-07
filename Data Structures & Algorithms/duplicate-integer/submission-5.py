class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for num in nums:
            if dictionary.get(num) is not None:
                return True
            dictionary[num] = 1
        return False