class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = float('-inf')
        currentMaxValue = float('-inf')
        
        for num in nums:
            currentMaxValue = max(num, num+currentMaxValue)
            maxSum = max(currentMaxValue, maxSum)
    
        return maxSum
        