class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 1
        k=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                nums[slow+1], nums[fast] = nums[fast], nums[slow+1]
                fast+=1
                slow+=1
                k+=1
        return k
            
            
        