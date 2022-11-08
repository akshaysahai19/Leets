class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for i in range(numCourses)]
        in_order = [0]*numCourses
        
        for c,r in prerequisites:
            graph[c].append(r)
            in_order[r]+=1
        
        stack = []
        for i in range(numCourses):
            if in_order[i]==0:
                stack.append(i)
        
        print(stack)
        if not stack:
            return False
        
        while stack:
            course = stack.pop()
            for req in graph[course]:
                in_order[req]-=1
                if in_order[req]==0:
                    stack.append(req)
        print('in_order = ',in_order)
        return sum(in_order)==0
                