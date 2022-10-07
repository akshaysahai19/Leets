# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        bfs = []
        
        q = deque([root])
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                temp = q.popleft()
                if temp:
                    level.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
            
            bfs.append(level)
            
        return bfs[::-1]
            
            
        