# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        bfs = []
        q = deque([root])
        
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            bfs.append(level[-1])
                    
        return bfs
        