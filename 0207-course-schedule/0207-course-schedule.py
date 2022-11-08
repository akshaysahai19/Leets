class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for i in range(numCourses)]
        out_order = [0]*numCourses
        
        for c,r in prerequisites:
            graph[c].append(r)
            out_order[r]+=1
        
        stack = []
        for i in range(numCourses):
            if out_order[i]==0:
                stack.append(i)
        
        if not stack:
            return False
        
        while stack:
            course = stack.pop()
            for req in graph[course]:
                out_order[req]-=1
                if out_order[req]==0:
                    stack.append(req)
                    
        return sum(out_order)==0
                