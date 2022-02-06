class Solution:
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        return self.openOptions(m, n, 0, 0, mem)
        
    
    def openOptions(self, m, n, cm,cn, mem):
        
        if (cm,cn) in mem:
            return mem[(cm,cn)]
        
        if cm==m-1 and cn==n-1:
            return 1 
        
        if cm>m or cn>n:
            return 0
        
        mem[(cm,cn)] = self.openOptions(m, n, cm+1,cn, mem) + self.openOptions(m, n, cm,cn+1, mem)
        
        return mem[(cm,cn)]