class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        reps = {}
        result = []

        for num in nums:
            if num not in reps:
                reps[num] = 1
            else:
                reps[num] += 1
        
        for i in range(k):
            result.append(max(reps, key = reps.get))
            reps.pop(max(reps, key = reps.get))

        return result