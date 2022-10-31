# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        startPath,destPath, path = [], [], []
        
        def dfs(node):
            
            nonlocal path, startPath, destPath
            
            if not node:
                return ''
            
            if node.val==startValue:
                startPath[:] = path
            
            if node.val==destValue:
                destPath[:] = path
            
            path.append('L')
            dfs(node.left)
            path.pop()
            
            path.append('R')
            dfs(node.right)
            path.pop()
        
        dfs(root)
        
        s = ''.join(startPath)
        d = ''.join(destPath)
        
        def commonPrefix(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return s1[i:], s2[i:]
        
        s,d = commonPrefix(s,d)
        return "".join("U" * len(s)) + "".join(d)