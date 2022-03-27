class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = left+(right)
            if left>right:
                return -1
            if target<nums[mid]:
                right = mid-1
            elif target==nums[mid]:
                return mid
            else:
                left = mid+1
        
        return -1
        