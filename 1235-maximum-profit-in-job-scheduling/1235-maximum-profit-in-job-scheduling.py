class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        maxVal = 0
        
        @lru_cache(None)
        def schedule(n):
            nonlocal maxVal
            if n>=len(startTime):
                return 0
            
            currProfit = jobs[n][2]
            for i in range(n+1, len(startTime)):
                if jobs[n][1]<=jobs[i][0]:
                    currProfit += schedule(i)
                    break
            
            nextProf = schedule(n + 1)
            return max(nextProf, currProfit)
            
        return schedule(0)
        
        