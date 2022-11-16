# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def binary(low, hi):
            
            if low>=hi:
                return int(low)
            
            mid = low+(hi-low)/2
            
            res = isBadVersion(mid)
            if res:
                return binary(low, mid)
            
            return binary(mid+1, hi)
        
        return binary(1, n)