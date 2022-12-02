class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
#         because it is 1-indexed
        if n==1:
            return 0
        elif n==2:
            if k==1:
                return 0
            elif k==2:
                return 1
        
#         n is formed by 1 half of n-1 + flipped n-1
        total = 2**(n-1)/2
        if k<=total:
#             if k lies on the original n-1 half
            return self.kthGrammar(n-1, k)
        else:
#             if k lies on the flipped n-1 half
#             (1-) because it is flipped
            return 1-self.kthGrammar(n-1, k-total)
        
        
                    
            