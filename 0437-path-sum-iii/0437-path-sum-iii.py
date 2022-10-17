# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        
        def findPairs(node, curr):
            
            if not node:
                return 0
            
            if node.val==curr:
                return 1 + findPairs(node.left, curr-node.val) + findPairs(node.right, curr-node.val)
            else:
                return findPairs(node.left, curr-node.val) + findPairs(node.right, curr-node.val)
        
        
        return findPairs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        
        
                    
                
            
            