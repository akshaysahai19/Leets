class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        gmax = 0      
        d = defaultdict(list)       
        
        for i,j in stones:
#           Creating ajacency matrix 
            for x,y in stones:
                if i == x and j == y:
                    continue
                elif i == x or j==y:
                    d[(i,j)].append((x,y))        
#       DFS function will go until the end when no nodes of connected nodes are left, then will keep adding 1 as it goes back
        def dfs(i,j):
            nonlocal gmax
            if (i,j) not in visited:
                visited.append((i,j))
                for (m,n) in d[(i,j)]:
                    if (m,n) not in visited:
                        dfs(m,n)
                gmax+=1            
            
        visited = []   
#       For every node not in visted we do dfs, we want to count the number of connected nodes in every "island". All connected nodes except the first node will count towards it.
        for (x,y) in d:
            if (x,y) not in visited:
                visited.append((x,y))
                for (m,n) in d[(x,y)]:
                    if (m,n) not in visited:
                        dfs(m,n)
                
        return gmax