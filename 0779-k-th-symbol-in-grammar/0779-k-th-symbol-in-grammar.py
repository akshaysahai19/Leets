class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        elif n==2:
            if k==1:
                return 0
            elif k==2:
                return 1
        
        total = 2**(n-1)/2
        if k<=total:
            return self.kthGrammar(n-1, k)
        else:
            return 1-self.kthGrammar(n-1, k-total)
        
        
                    
            