class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        mem = []
        currentMax = 0
        
        for i in range(len(s)):
            if(s[i] in mem):
                mem = mem[mem.index(s[i])+1:]
            mem.append(s[i])
            currentMax = max(len(mem), currentMax)
        return currentMax
        
                
                
                
            