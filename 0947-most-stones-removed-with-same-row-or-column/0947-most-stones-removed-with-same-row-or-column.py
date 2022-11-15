class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        visited = {}
        
        def findPairs(i):
            
            if i in visited:
                return
            
            visited[i]=1
            
            for j in range(len(stones)):
                if (stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]) and j not in visited:
                    findPairs(j)
        
        ans = 0
        for i in range(len(stones)):
            if i not in visited:
                findPairs(i)
                ans+=1
        
        return len(stones)-ans
                
                
        