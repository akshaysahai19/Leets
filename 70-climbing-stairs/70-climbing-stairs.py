class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.differentClimbs(n,{})
    
    def differentClimbs(self,n, mapp):
        if n in mapp:
            return mapp[n]
        if n<0:
            return 0
        if n==0:
            return 1
        mapp[n-1] = self.differentClimbs(n-1, mapp)
        mapp[n-2] = self.differentClimbs(n-2, mapp)
        return mapp[n-1]+mapp[n-2]
            
        