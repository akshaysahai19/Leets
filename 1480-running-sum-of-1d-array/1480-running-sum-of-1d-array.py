class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        for i, num in enumerate(nums):
            runningSum+=num
            nums[i] = runningSum
        return nums
            