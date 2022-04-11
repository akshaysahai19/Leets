class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = min(height[0], height[right])*(right-left)
        while left<right:
            calArea = (min(height[left], height[right])*(right-left))
            if maxArea<calArea:
                maxArea = calArea
            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
                right-=1
        return maxArea
            
        
        