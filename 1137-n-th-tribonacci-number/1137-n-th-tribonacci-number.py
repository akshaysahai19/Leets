class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = {}
        
        def result(n):
            
            if n in dp:
                return dp[n]
            
            if n==0:
                return 0

            if n==1 or n==2:
                return 1

            dp[n] = result(n-3)+result(n-3+1)+result(n-3+2)
            
            return dp[n]
        
        return result(n)
    
