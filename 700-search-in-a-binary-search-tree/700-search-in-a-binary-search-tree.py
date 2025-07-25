# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def searchBSTVal(root):
            if(root==None or root.val==val):
                return root
            
            if val<root.val:
                return searchBSTVal(root.left)
            if val>root.val:
                return searchBSTVal(root.right)
            
            return None
        
        return searchBSTVal(root)
        