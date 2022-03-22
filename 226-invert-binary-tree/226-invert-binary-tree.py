# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recursiveInvertTree(root):
            if root==None:
                return

            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
            elif root.right and not root.left:
                root.left = root.right
                root.right = None
            
            recursiveInvertTree(root.left)
            recursiveInvertTree(root.right)
            return root
        
        print(recursiveInvertTree(root))
        
        return root
            
        
        
        