class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binary(low, hi):
            
            if low>hi:
                return low
            
            mid = (hi+low)//2
            
            if nums[mid]==target:
                return mid
            
            if target<nums[mid]:
                return binary(low, mid-1)
            
            return binary(mid+1, hi)
        
        return binary(0, len(nums)-1)
        