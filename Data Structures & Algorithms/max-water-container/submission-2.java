class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1, max = 0, area = -1;

        while (left < right) {
            area = (right - left) * Math.min(heights[left], heights[right]);

            if (area > max) {
                max = area;
            } else if (heights[left] < heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return max;
    }
}
