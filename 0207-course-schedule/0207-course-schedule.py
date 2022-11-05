class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        in_degree = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        
        for c,r in prerequisites:
            graph[c].append(r)
            in_degree[r]+=1
        
        queue = []
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
                
        while queue:
            course = queue.pop(0)
            for prereq in graph[course]:
                in_degree[prereq]-=1
                if in_degree[prereq]==0:
                    queue.append(prereq)
                    
        if sum(in_degree)==0:
            return True
        return False
                