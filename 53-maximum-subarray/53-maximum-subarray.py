class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        currentMaxValue = maxSum
        
        for n in range(1, len(nums)):
            if currentMaxValue+nums[n]<nums[n]:
                currentMaxValue = nums[n]
            else:
                currentMaxValue+=nums[n]
            
            if maxSum<currentMaxValue:
                maxSum = currentMaxValue
    
        return maxSum
        