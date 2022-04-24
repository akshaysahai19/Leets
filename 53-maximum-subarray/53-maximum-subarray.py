class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        # currentMaxValue = nums[0]
        
        def maxSumArray(n):
            nonlocal maxSum
            
            if(n==0):
                return nums[0]
            
            currentMaxValue = max(maxSumArray(n-1)+nums[n], nums[n])
            maxSum = max(maxSum, currentMaxValue)
            
            return currentMaxValue
            
        
        maxSumArray(len(nums)-1)   
    
        return maxSum
        