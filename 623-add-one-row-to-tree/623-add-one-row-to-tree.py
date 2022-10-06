# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
       
        rRoot = TreeNode(0)
        output = rRoot
        rRoot.left = root
        
        def addNode(node, i):
            
            if not node:
                return
            
            i+=1
            if i==depth+1:
                if node.left:
                    tempLeft = TreeNode(val)
                    tempLeft.left = node.left
                    node.left = tempLeft
                if node.right:
                    tempRight = TreeNode(val)
                    tempRight.right = node.right
                    node.right = tempRight
                if not node.left:
                    node.left = TreeNode(val)
                if not node.right:
                    node.right = TreeNode(val)
            else:
                addNode(node.left, i)
                addNode(node.right, i)
            
            
        addNode(rRoot, 1)
        
        return output.left