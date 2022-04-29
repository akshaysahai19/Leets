class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentNegative = nums[0]
        maxSum = nums[0]
        for n in range(1,len(nums)):
            localMax = currentMax*nums[n]
            localMin = currentNegative*nums[n]
            currentNegative = min(min(localMax, localMin), nums[n])
            currentMax = max(max(localMax, localMin), nums[n])
            maxSum = max(maxSum, currentMax)
        
        return maxSum
            
            
        