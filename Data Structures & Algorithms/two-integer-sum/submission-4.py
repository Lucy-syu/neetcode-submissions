class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reg = {}

        for i in range(len(nums)):
            if reg.get(target - nums[i], -1) != -1:
                return [reg[target - nums[i]], i]
            else:
                reg[nums[i]] = i
            i +=  1
            
        return 0