class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        dp = {}
        
        def schedule(n):
            
            if n in dp:
                return dp[n]
            
            if n>=len(startTime):
                return 0
            
            currProfit = jobs[n][2]
            for i in range(n+1, len(startTime)):
                if jobs[n][1]<=jobs[i][0]:
                    currProfit += schedule(i)
                    break
            
            nextProf = schedule(n + 1)
            dp[n] = max(nextProf, currProfit)
            return dp[n]
            
        return schedule(0)
        
        