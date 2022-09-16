class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        countMap = defaultdict(int)
        
        for n in nums:
            if n in countMap:
                countMap[n]+=n
            else:
                countMap[n] = n
                
        mem = {}
        def earn(n):
            if n in mem:
                return mem[n]
            
            if n==0:
                return 0
            if n==1:
                return countMap[1]
            
            mem[n] = max(earn(n-1), earn(n-2)+countMap[n])
            return mem[n]
       
        return earn(max(nums))
            
            
            
            
            
            
            
                
        