# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def findCompleteTree(node):
            if not node:
                return 0
            
            left = findCompleteTree(node.left)
            right = findCompleteTree(node.right)
            
            
            return 1+left+right
        
        return findCompleteTree(root)