class UnionFind():

        def __init__(self, n) -> None:
            self.parents = [i for i in range(n)]
        
        def find(self, x):
            if self.parents[x]!=x:
                return self.find(self.parents[x])
            return self.parents[x]
        
        def union(self, x,y):
            self.parents[self.find(y)] = self.find(x)

class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        unionFind = UnionFind(n)

        for u,v in edges:
            unionFind.union(u,v)
        
        if unionFind.find(source)==unionFind.find(destination):
            return True
        return False
        


