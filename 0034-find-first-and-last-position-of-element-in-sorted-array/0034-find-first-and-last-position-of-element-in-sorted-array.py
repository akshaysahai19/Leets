class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        def binarySearch(low, high, lastMid, isFirst):
            
            if low>high:
                return lastMid
            
            mid = int((high+low)/2)
            
            if mid<0 or mid==len(nums):
                return lastMid
            
            if target==nums[mid]:
                if isFirst:
                    lastMid = min(lastMid, mid)
                    return binarySearch(low, mid-1, lastMid, isFirst)
                else:
                    lastMid = max(lastMid, mid)
                    return binarySearch(mid+1, high, lastMid, isFirst)
            
            elif target>nums[mid]:
                return binarySearch(mid+1, high, lastMid, isFirst)
            else:
                return binarySearch(low, mid-1, lastMid, isFirst)
        
        
        start = binarySearch(0, len(nums), float('inf'), True)
        end = binarySearch(0, len(nums), float('-inf'), False)
        
        if start==float('inf') and end==float('-inf'):
            return [-1,-1]
        
        return [start, end]