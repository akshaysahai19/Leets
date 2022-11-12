class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        left = 0
        res = []
        
        while left+k<=len(nums):
            part = nums[left:left+k]
            part.sort()
            mid = len(part)//2
            if len(part)%2==0:
                res.append((part[mid-1]+part[mid])/2)
            else:
                res.append(part[mid])
            left+=1
        return res
            