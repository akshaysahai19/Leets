# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def findTrees(node):
            if not node:
                return None
            
            node.left = findTrees(node.left)
            node.right = findTrees(node.right)
            
            if node.val==0 and not node.left and not node.right:
                return None
            else:
                return node
        
        
        return findTrees(root)
            
        