class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range(len(nums)):
            if (target - nums[i]) in dictionary:
                indices = [i, dictionary.get(target-nums[i])]
                indices.sort()
                return indices
            elif nums[i] not in dictionary:
                dictionary[nums[i]] = i

        return []