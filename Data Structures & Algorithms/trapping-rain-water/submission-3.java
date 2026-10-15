class Solution {
    public int trap(int[] height) {
        
        if(height == null || height.length <= 2)
        return 0;
        int leftIndex = 0, rightIndex = height.length-1;
        int leftMax = 0, rightMax = 0;
        int trappedWater = 0;
        while(leftIndex < rightIndex)
        {

            if(height[rightIndex] > height[leftIndex])
            {
                if(leftMax > height[leftIndex])
                {
                    trappedWater += leftMax-height[leftIndex];
                }
                else
                leftMax = height[leftIndex];

                leftIndex++;

            }
            else
            {
                if(rightMax > height[rightIndex])
                {
                    trappedWater += rightMax-height[rightIndex];
                }
                else
                rightMax = height[rightIndex];
                rightIndex--;
            }
            
        }
        return trappedWater;
    }
}