# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        bfs = []
        q = deque([root])
        i = 0
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
                        
            if len(bfs)%2!=0:
                bfs.append(level[::-1])
            else:
                bfs.append(level)
        
        return bfs
                    
            
        