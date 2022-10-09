class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        mem = {}
        
        def schedule(n):
            
            if n in mem:
                return mem[n]
            
            if n>=len(startTime):
                return 0
            
            currProfit = jobs[n][2]
            for i in range(n+1, len(startTime)):
                if jobs[n][1]<=jobs[i][0]:
                    currProfit += schedule(i)
                    break
            
            mem[n] = max(schedule(n + 1), currProfit)
            
            return mem[n]
            
        return schedule(0)
        
        