class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []

        while len(result) < 2:
            if left < right and numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
            elif numbers[left] + numbers[right] < target: 
                left += 1
            else:
                right -= 1

        return result