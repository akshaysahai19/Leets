# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def findMirror(nodeL, nodeR):
            if not nodeL and not nodeR:
                return True
            
            if nodeL and nodeR and nodeL.val==nodeR.val:
                return findMirror(nodeL.left, nodeR.right) and findMirror(nodeR.left, nodeL.right)
            return False
            
        
        return findMirror(root, root)
        