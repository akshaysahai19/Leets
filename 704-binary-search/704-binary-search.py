class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findTarget(left, right):
            mid = left + (right - left) // 2
            if left>right:
                return -1
            if target<nums[mid]:
                right = mid-1
            elif target==nums[mid]:
                return mid
            else:
                left = mid+1
            
            return findTarget(left, right)
        
        return findTarget(0, len(nums)-1) 
        