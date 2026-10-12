class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            if max < width * height:
                max = width * height
            elif min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1

        return max