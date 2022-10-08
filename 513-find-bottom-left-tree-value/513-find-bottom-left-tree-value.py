# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return []
        bfs = []
        q = deque([root])
        
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            bfs.append(level)
        
        
        print(bfs)
        return bfs[-1][0]