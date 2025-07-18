"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        bfs = []
        q = deque([root])
        
        while q:
            level = []
            
            for i in range(len(q)):
                temp = q.popleft()
                level.append(temp.val)
                q.extend(temp.children)
            
            bfs.append(level)
        
        return bfs