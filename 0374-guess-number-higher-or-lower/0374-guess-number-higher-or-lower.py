# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def binary(low, hi):
            
            mid = low+(hi-low)/2
            
            res = guess(mid)
            if res == 0:
                return int(mid)
            
            if res==1:
                return binary(mid+1, hi)
            else:
                return binary(low, mid-1)
        
        return binary(1, n)