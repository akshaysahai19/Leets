# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root

        def findLCA(node):
            if not node:
                return False
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            mid = node==p or node==q
            
            if (mid and right) or (left and mid) or (left and right):
                return node

            return left or right or mid
        
        return findLCA(root)


            
        