class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        wordPos = {}
        for i,n in enumerate(nums):
            if n in wordPos:
                if abs(wordPos[n]-i)<=k:
                    return True
            wordPos[n] = i

        return False
        